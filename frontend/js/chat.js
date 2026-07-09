/* ============================================================
   BodyLens AI — Floating Chat Assistant (with Voice)
   ============================================================ */

(function () {

    const API_URL = "http://127.0.0.1:8000/chat";

    const SR = window.SpeechRecognition || window.webkitSpeechRecognition;
    const voiceInputSupported = !!SR;
    const voiceOutputSupported = "speechSynthesis" in window;
    let speakOn = true;

    const widget = document.createElement("div");
    widget.id = "blai-chat";
    widget.innerHTML = `
        <button id="blai-chat-toggle" aria-label="Open chat">
            <i data-lucide="message-circle"></i>
        </button>

        <div id="blai-chat-window" class="blai-hidden">
            <div class="blai-chat-header">
                <div class="blai-chat-title">
                    <span class="blai-dot"></span>
                    <div>
                        <strong>Health Assistant</strong>
                        <small>Ask me anything about fitness</small>
                    </div>
                </div>
                <div class="blai-header-actions">
                    <button id="blai-chat-speak" aria-label="Toggle voice" title="Toggle voice reply">
                        <i data-lucide="volume-2"></i>
                    </button>
                    <button id="blai-chat-close" aria-label="Close chat">
                        <i data-lucide="x"></i>
                    </button>
                </div>
            </div>

            <div id="blai-chat-body">
                <div class="blai-msg blai-bot">Hi! 👋 I'm your health assistant. Ask me about diet, workouts, BMI, protein, or anything fitness-related.</div>
            </div>

            <div class="blai-chat-input">
                <button id="blai-chat-mic" aria-label="Speak" title="Speak your question">
                    <i data-lucide="mic"></i>
                </button>
                <input type="text" id="blai-chat-text" placeholder="Type your question..." autocomplete="off">
                <button id="blai-chat-send" aria-label="Send">
                    <i data-lucide="send"></i>
                </button>
            </div>
        </div>
    `;
    document.body.appendChild(widget);

    const toggleBtn = document.getElementById("blai-chat-toggle");
    const closeBtn  = document.getElementById("blai-chat-close");
    const speakBtn  = document.getElementById("blai-chat-speak");
    const micBtn    = document.getElementById("blai-chat-mic");
    const windowEl  = document.getElementById("blai-chat-window");
    const bodyEl    = document.getElementById("blai-chat-body");
    const inputEl   = document.getElementById("blai-chat-text");
    const sendBtn   = document.getElementById("blai-chat-send");

    if (!voiceInputSupported && micBtn) micBtn.style.display = "none";
    if (!voiceOutputSupported && speakBtn) speakBtn.style.display = "none";

    function openChat() {
        windowEl.classList.remove("blai-hidden");
        toggleBtn.classList.add("blai-open");
        inputEl.focus();
    }
    function closeChat() {
        windowEl.classList.add("blai-hidden");
        toggleBtn.classList.remove("blai-open");
        if (voiceOutputSupported) window.speechSynthesis.cancel();
    }

    toggleBtn.addEventListener("click", () => {
        windowEl.classList.contains("blai-hidden") ? openChat() : closeChat();
    });
    closeBtn.addEventListener("click", closeChat);

    speakBtn.addEventListener("click", () => {
        speakOn = !speakOn;
        speakBtn.classList.toggle("blai-off", !speakOn);
        speakBtn.innerHTML = speakOn
            ? '<i data-lucide="volume-2"></i>'
            : '<i data-lucide="volume-x"></i>';
        if (!speakOn && voiceOutputSupported) window.speechSynthesis.cancel();
        if (window.lucide) lucide.createIcons();
    });

    function speak(text) {
        if (!speakOn || !voiceOutputSupported) return;
        window.speechSynthesis.cancel();
        const u = new SpeechSynthesisUtterance(text);
        u.rate = 1;
        u.pitch = 1;
        window.speechSynthesis.speak(u);
    }

    function getSavedProfile() {
        try {
            const saved = sessionStorage.getItem("lastReport");
            return saved ? JSON.parse(saved) : null;
        } catch (e) {
            return null;
        }
    }

    function addMessage(text, who) {
        const msg = document.createElement("div");
        msg.className = "blai-msg " + (who === "user" ? "blai-user" : "blai-bot");
        msg.textContent = text.trim();
        bodyEl.appendChild(msg);
        bodyEl.scrollTop = bodyEl.scrollHeight;
        return msg;
    }

    function addTyping() {
        const t = document.createElement("div");
        t.className = "blai-msg blai-bot blai-typing";
        t.innerHTML = "<span></span><span></span><span></span>";
        bodyEl.appendChild(t);
        bodyEl.scrollTop = bodyEl.scrollHeight;
        return t;
    }

    async function sendMessage() {
        const text = inputEl.value.trim();
        if (!text) return;

        addMessage(text, "user");
        inputEl.value = "";
        sendBtn.disabled = true;

        const typing = addTyping();

        try {
            const res = await fetch(API_URL, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ message: text, profile: getSavedProfile() })
            });
            const data = await res.json();
            typing.remove();
            const reply = data.reply || "Sorry, I couldn't respond.";
            addMessage(reply, "bot");
            speak(reply);
        } catch (err) {
            typing.remove();
            addMessage("Cannot reach the assistant. Make sure the server is running.", "bot");
        } finally {
            sendBtn.disabled = false;
            inputEl.focus();
        }
    }

    sendBtn.addEventListener("click", sendMessage);
    inputEl.addEventListener("keydown", (e) => {
        if (e.key === "Enter") sendMessage();
    });

    if (voiceInputSupported) {
        const recognition = new SR();
        recognition.lang = "en-US";
        recognition.interimResults = false;
        recognition.maxAlternatives = 1;
        let listening = false;

        micBtn.addEventListener("click", () => {
            if (listening) { recognition.stop(); return; }
            try { recognition.start(); } catch (e) {}
        });

        recognition.onstart = () => { listening = true; micBtn.classList.add("blai-listening"); };
        recognition.onend = () => { listening = false; micBtn.classList.remove("blai-listening"); };
        recognition.onerror = () => { listening = false; micBtn.classList.remove("blai-listening"); };
        recognition.onresult = (event) => {
            const transcript = event.results[0][0].transcript;
            inputEl.value = transcript;
            sendMessage();
        };
    }

    if (window.lucide) lucide.createIcons();

})();