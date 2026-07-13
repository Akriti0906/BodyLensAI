/* ============================================================
   BodyLens AI — AI Exercise Coach (mirror + performance fixes)
   ============================================================ */

const video   = document.getElementById("cam-video");
const canvas  = document.getElementById("cam-canvas");
const ctx     = canvas.getContext("2d");
const repsEl  = document.getElementById("cam-reps");
const stageEl = document.getElementById("cam-stage");
const scoreEl = document.getElementById("cam-score");
const fbEl    = document.getElementById("cam-feedback");
const checkEl = document.getElementById("cam-check");
const startBtn = document.getElementById("cam-start");
const stopBtn  = document.getElementById("cam-stop");
const switchBtn = document.getElementById("cam-switch");
const resetBtn = document.getElementById("cam-reset");

const EXERCISES = {
    squat: {
        name: "Squat",
        landmarks: { hip: 23, knee: 25, ankle: 27, shoulder: 11 },
        downAngle: 95,
        upAngle: 160,
        checks: [
            { name: "back",  test: (a) => a.back >= 150,  msg: "Straighten your back",  penalty: 20 },
            { name: "lean",  test: (a) => a.lean <= 45,   msg: "Don't lean forward",     penalty: 15 }
        ]
    }
};
let current = EXERCISES.squat;

let reps = 0;
let stage = "up";
let camera = null;
let pose = null;
let running = false;
let facingMode = "user";
let repScores = [];
let currentRepFaults = new Set();
let busy = false;   // prevents overlapping frame processing

function calcAngle(a, b, c) {
    const rad = Math.atan2(c.y - b.y, c.x - b.x) - Math.atan2(a.y - b.y, a.x - b.x);
    let deg = Math.abs(rad * 180 / Math.PI);
    if (deg > 180) deg = 360 - deg;
    return deg;
}

function setFeedback(msg, type) {
    fbEl.textContent = msg;
    fbEl.className = "cam-feedback" + (type ? " cam-fb-" + type : "");
}

function showCheck(show) {
    checkEl.style.opacity = show ? "1" : "0";
}

function onResults(results) {
    canvas.width = video.videoWidth || 640;
    canvas.height = video.videoHeight || 480;

    ctx.save();
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    // Mirror horizontally for a natural selfie view
    ctx.translate(canvas.width, 0);
    ctx.scale(-1, 1);
    ctx.drawImage(results.image, 0, 0, canvas.width, canvas.height);

    if (!results.poseLandmarks) {
        setFeedback("No person detected — step back", "warn");
        showCheck(false);
        ctx.restore();
        return;
    }

    if (window.drawConnectors && window.POSE_CONNECTIONS) {
        drawConnectors(ctx, results.poseLandmarks, POSE_CONNECTIONS, { color: "#7C3AED", lineWidth: 4 });
        drawLandmarks(ctx, results.poseLandmarks, { color: "#10B981", fillColor: "#34D399", lineWidth: 2, radius: 5 });
    }

    const lm = results.poseLandmarks;
    const L = current.landmarks;
    const hip = lm[L.hip], knee = lm[L.knee], ankle = lm[L.ankle], shoulder = lm[L.shoulder];

    if (!(hip && knee && ankle && shoulder &&
          hip.visibility > 0.5 && knee.visibility > 0.5 && ankle.visibility > 0.5 && shoulder.visibility > 0.5)) {
        setFeedback("Step back — make sure your full body is visible", "warn");
        showCheck(false);
        ctx.restore();
        return;
    }

    const kneeAngle = calcAngle(hip, knee, ankle);
    const backAngle = calcAngle(shoulder, hip, knee);
    const leanAngle = Math.abs(Math.atan2(shoulder.x - hip.x, hip.y - shoulder.y) * 180 / Math.PI);

    const angles = { knee: kneeAngle, back: backAngle, lean: leanAngle };

    const faults = [];
    let penalty = 0;
    current.checks.forEach(c => {
        if (!c.test(angles)) { faults.push(c.msg); penalty += c.penalty; }
    });

    stageEl.textContent = kneeAngle < current.downAngle ? "Down" : (kneeAngle > current.upAngle ? "Up" : "Mid");

    if (kneeAngle < current.downAngle) {
        stage = "down";
        faults.forEach(f => currentRepFaults.add(f));
        if (penalty > 0) {
            setFeedback(faults[0], "warn");
            showCheck(false);
        } else {
            setFeedback("Perfect Form! Hold it 💪", "good");
            showCheck(true);
        }
    } else if (kneeAngle > current.upAngle) {
        showCheck(false);
        if (stage === "down") {
            let repPenalty = 0;
            current.checks.forEach(c => { if (currentRepFaults.has(c.msg)) repPenalty += c.penalty; });
            const score = Math.max(0, 100 - repPenalty);
            reps++;
            repScores.push(score);
            repsEl.textContent = reps;
            scoreEl.textContent = score + "%";
            setFeedback(score >= 85 ? "✅ Great rep!" : "Rep counted — improve form", score >= 85 ? "good" : "warn");
            currentRepFaults.clear();
        }
        stage = "up";
    } else {
        showCheck(false);
        setFeedback(stage === "up" ? "Go lower..." : (faults[0] || "Push up!"), "warn");
    }

    ctx.restore();
}

function initPose() {
    pose = new Pose({ locateFile: (f) => `https://cdn.jsdelivr.net/npm/@mediapipe/pose/${f}` });
    pose.setOptions({
        modelComplexity: 1,
        smoothLandmarks: true,
        minDetectionConfidence: 0.6,
        minTrackingConfidence: 0.6
    });
    pose.onResults(onResults);
}

async function startCamera() {
    if (running) return;
    if (!pose) initPose();
    setFeedback("Starting camera...", "");
    camera = new Camera(video, {
        onFrame: async () => { if (running && !busy) { busy = true; await pose.send({ image: video }); busy = false; } },
        width: 640, height: 480, facingMode: facingMode
    });
    try {
        await camera.start();
        running = true;
        startBtn.style.display = "none";
        stopBtn.style.display = "inline-flex";
        setFeedback("Stand back — match the squat position!", "good");
    } catch (e) {
        setFeedback("Camera access denied. Please allow the camera.", "warn");
    }
}

function stopCamera() {
    running = false;
    if (camera) camera.stop();
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    startBtn.style.display = "inline-flex";
    stopBtn.style.display = "none";
    showCheck(false);
    setFeedback("Camera stopped", "");
}

async function switchCamera() {
    facingMode = (facingMode === "user") ? "environment" : "user";
    if (running) { stopCamera(); await startCamera(); }
}

startBtn.addEventListener("click", startCamera);
stopBtn.addEventListener("click", stopCamera);
switchBtn.addEventListener("click", switchCamera);
resetBtn.addEventListener("click", () => {
    reps = 0; stage = "up"; repScores = []; currentRepFaults.clear();
    repsEl.textContent = "0"; stageEl.textContent = "—"; scoreEl.textContent = "—";
    showCheck(false);
    setFeedback("Reset. Keep going!", "");
});