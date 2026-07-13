/* ============================================================
   BodyLens AI — AI Camera v2 (Full-body 33-landmark tracking)
   ============================================================ */

const video   = document.getElementById("cam-video");
const canvas  = document.getElementById("cam-canvas");
const ctx     = canvas.getContext("2d");
const repsEl  = document.getElementById("cam-reps");
const stageEl = document.getElementById("cam-stage");
const angleEl = document.getElementById("cam-angle");
const fbEl    = document.getElementById("cam-feedback");
const startBtn = document.getElementById("cam-start");
const stopBtn  = document.getElementById("cam-stop");
const switchBtn = document.getElementById("cam-switch");
const resetBtn = document.getElementById("cam-reset");

let reps = 0;
let stage = "up";
let camera = null;
let pose = null;
let running = false;
let facingMode = "user";

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

function onResults(results) {
    canvas.width = video.videoWidth || 1280;
    canvas.height = video.videoHeight || 720;

    ctx.save();
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.drawImage(results.image, 0, 0, canvas.width, canvas.height);

    if (results.poseLandmarks) {
        if (window.drawConnectors && window.POSE_CONNECTIONS) {
            drawConnectors(ctx, results.poseLandmarks, POSE_CONNECTIONS,
                { color: "#7C3AED", lineWidth: 4 });
            drawLandmarks(ctx, results.poseLandmarks,
                { color: "#10B981", fillColor: "#34D399", lineWidth: 2, radius: 5 });
        }

        const lm = results.poseLandmarks;
        const hip = lm[23], knee = lm[25], ankle = lm[27];

        if (hip && knee && ankle && hip.visibility > 0.5 && knee.visibility > 0.5 && ankle.visibility > 0.5) {
            const kneeAngle = calcAngle(hip, knee, ankle);
            angleEl.textContent = Math.round(kneeAngle) + "°";

            if (kneeAngle > 160) {
                if (stage === "down") {
                    reps++;
                    repsEl.textContent = reps;
                    setFeedback("Good rep! 💪", "good");
                }
                stage = "up";
                stageEl.textContent = "Up";
            } else if (kneeAngle < 90) {
                stage = "down";
                stageEl.textContent = "Down";
                setFeedback("Great depth! Now push up", "good");
            } else {
                stageEl.textContent = "Mid";
                setFeedback(stage === "up" ? "Go lower..." : "Push up!", "warn");
            }
        } else {
            setFeedback("Step back — make sure your full body is visible", "warn");
            angleEl.textContent = "—";
        }
    } else {
        setFeedback("No person detected — step back", "warn");
    }
    ctx.restore();
}

function initPose() {
    pose = new Pose({
        locateFile: (file) => `https://cdn.jsdelivr.net/npm/@mediapipe/pose/${file}`
    });
    pose.setOptions({
        modelComplexity: 2,
        smoothLandmarks: true,
        enableSegmentation: false,
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
        onFrame: async () => { if (running) await pose.send({ image: video }); },
        width: 1280,
        height: 720,
        facingMode: facingMode
    });
    try {
        await camera.start();
        running = true;
        startBtn.style.display = "none";
        stopBtn.style.display = "inline-flex";
        setFeedback("Stand back so your whole body is visible!", "good");
    } catch (e) {
        setFeedback("Camera access denied. Please allow the camera.", "warn");
    }
}

function stopCamera() {
    running = false;
    if (camera) { camera.stop(); }
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    startBtn.style.display = "inline-flex";
    stopBtn.style.display = "none";
    setFeedback("Camera stopped", "");
}

async function switchCamera() {
    facingMode = (facingMode === "user") ? "environment" : "user";
    if (running) {
        stopCamera();
        await startCamera();
    }
    setFeedback("Switched camera", "");
}

startBtn.addEventListener("click", startCamera);
stopBtn.addEventListener("click", stopCamera);
switchBtn.addEventListener("click", switchCamera);
resetBtn.addEventListener("click", () => {
    reps = 0;
    stage = "up";
    repsEl.textContent = "0";
    stageEl.textContent = "—";
    setFeedback("Reps reset. Keep going!", "");
});