function bmiProgress(bmi) {
    let percent = (bmi / 40) * 100;
    if (percent > 100) percent = 100;
    return percent;
}

function healthProgress(score) {
    return score * 3.6;
}

function getBadge(category) {
    if (category === "Underweight") return "underweight";
    if (category === "Normal Weight") return "normal";
    if (category === "Overweight") return "overweight";
    return "obese";
}

function getRiskClass(risk) {
    if (risk === "Low Risk") return "low-risk";
    if (risk === "Moderate Risk") return "moderate-risk";
    return "high-risk";
}

/* Animate any number from 0 to its target value */
function animateCounters() {
    document.querySelectorAll("[data-count]").forEach(el => {
        const target = parseFloat(el.getAttribute("data-count"));
        const decimals = (el.getAttribute("data-decimals") === "1") ? 1 : 0;
        const duration = 900;
        const start = performance.now();
        function step(now) {
            const p = Math.min((now - start) / duration, 1);
            const eased = 1 - Math.pow(1 - p, 3);
            el.textContent = (target * eased).toFixed(decimals);
            if (p < 1) requestAnimationFrame(step);
            else el.textContent = target.toFixed(decimals);
        }
        requestAnimationFrame(step);
    });
}

/* Accordion toggle */
function toggleAccordion(headerEl) {
    const body = headerEl.nextElementSibling;
    const open = body.classList.toggle("open");
    headerEl.classList.toggle("active", open);
}

function renderResult(data) {

    const badge = getBadge(data.category);
    const riskClass = getRiskClass(data.risk_level);
    const scoreDash = healthProgress(data.health_score);

    document.getElementById("result").innerHTML = `

<div id="pdf-content" class="fade-in">

<h2 class="report-title">Your Health Report</h2>
<p class="report-sub">AI-generated analysis based on your profile</p>

<div class="dashboard">

    <div class="stat-card stat-score">
        <span class="stat-label">Health Score</span>
        <div class="progress-circle">
            <svg width="130" height="130" viewBox="0 0 130 130">
                <defs>
                    <linearGradient id="scoreGrad" x1="0" y1="0" x2="1" y2="1">
                        <stop offset="0%" stop-color="#7C3AED"/>
                        <stop offset="100%" stop-color="#4F46E5"/>
                    </linearGradient>
                </defs>
                <circle cx="65" cy="65" r="55" class="circle-bg"/>
                <circle cx="65" cy="65" r="55" class="circle-progress"
                        stroke-dasharray="${scoreDash} 360"/>
            </svg>
            <div class="circle-text"><span data-count="${data.health_score}">0</span></div>
        </div>
        <span class="risk-pill ${riskClass}">${data.risk_level}</span>
    </div>

    <div class="stat-card">
        <div class="stat-ico"><i data-lucide="scale"></i></div>
        <span class="stat-label">BMI</span>
        <div class="stat-num"><span data-count="${data.bmi}" data-decimals="1">0</span></div>
        <div class="bmi-bar"><div class="bmi-fill" style="width:${bmiProgress(data.bmi)}%"></div></div>
        <span class="badge ${badge}">${data.category}</span>
    </div>

    <div class="stat-card">
        <div class="stat-ico"><i data-lucide="flame"></i></div>
        <span class="stat-label">Calories</span>
        <div class="stat-num"><span data-count="${data.target_calories}">0</span></div>
        <span class="stat-unit">kcal / day</span>
    </div>

    <div class="stat-card">
        <div class="stat-ico"><i data-lucide="beef"></i></div>
        <span class="stat-label">Protein</span>
        <div class="stat-num"><span data-count="${data.protein_g}">0</span><small>g</small></div>
        <span class="stat-unit">daily target</span>
    </div>

    <div class="stat-card">
        <div class="stat-ico"><i data-lucide="droplet"></i></div>
        <span class="stat-label">Water</span>
        <div class="stat-num"><span data-count="${data.water_liters}" data-decimals="1">0</span><small>L</small></div>
        <span class="stat-unit">daily target</span>
    </div>

    <div class="stat-card">
        <div class="stat-ico"><i data-lucide="target"></i></div>
        <span class="stat-label">Goal</span>
        <div class="stat-goal">${data.goal.replace(/_/g, " ")}</div>
        <span class="stat-unit">${data.workout_type}</span>
    </div>

</div>

<div class="card advice-card">
    <div class="advice-ico"><i data-lucide="heart-pulse"></i></div>
    <div>
        <h3>Personalized Advice</h3>
        <p>${data.condition_advice}</p>
    </div>
</div>

<div class="accordion">
    <div class="acc-head active" onclick="toggleAccordion(this)">
        <span><i data-lucide="salad"></i> Personalized Diet Plan</span>
        <i data-lucide="chevron-down" class="acc-arrow"></i>
    </div>
    <div class="acc-body open">
    ${Object.entries(data.diet_plan).map(([meal, foods]) => {
        let tC=0,tP=0,tCa=0,tF=0;
        foods.forEach(f => { tC+=f.calories; tP+=f.protein; tCa+=f.carbs; tF+=f.fat; });
        return `
        <h3 class="meal-title">${meal.charAt(0).toUpperCase()+meal.slice(1)}</h3>
        <table class="diet-table">
        <tr><th>Food</th><th>Cal</th><th>Protein</th><th>Carbs</th><th>Fat</th></tr>
        ${foods.map(f => `
        <tr><td>${f.food}</td><td>${f.calories}</td><td>${f.protein} g</td><td>${f.carbs} g</td><td>${f.fat} g</td></tr>
        `).join("")}
        <tr class="total-row"><td><b>Total</b></td><td><b>${tC}</b></td><td><b>${tP} g</b></td><td><b>${tCa} g</b></td><td><b>${tF} g</b></td></tr>
        </table>`;
    }).join("")}
    </div>
</div>

<div class="accordion">
    <div class="acc-head active" onclick="toggleAccordion(this)">
        <span><i data-lucide="dumbbell"></i> Weekly Exercise Guide</span>
        <i data-lucide="chevron-down" class="acc-arrow"></i>
    </div>
    <div class="acc-body open">
    ${Object.entries(data.workout_plan).map(([day, session]) => `
        <div class="day-block">
            <div class="day-head">
                <h3>${day.charAt(0).toUpperCase()+day.slice(1)}</h3>
                <span class="day-focus">${session.focus}</span>
            </div>
            ${session.exercises.map(ex => `
            <div class="ex-card">
                ${ex.image ? `<img src="${ex.image}" class="exercise-img" alt="${ex.name}" onerror="this.style.display='none'">` : ""}
                <div class="ex-body">
                    <h4>${ex.name}</h4>
                    <div class="ex-tags">
                        <span class="ex-tag"><i data-lucide="crosshair"></i> ${ex.target_muscle}</span>
                        <span class="ex-tag"><i data-lucide="signal"></i> ${ex.difficulty}</span>
                        <span class="ex-tag"><i data-lucide="flame"></i> ${ex.calories}</span>
                        <span class="ex-tag ex-tag-strong"><i data-lucide="repeat"></i> ${ex.prescription}</span>
                    </div>
                    ${ex.video ? `<a href="${ex.video}" target="_blank" class="video-btn"><i data-lucide="play"></i> Watch Demo</a>` : ""}
                    ${ex.steps.length ? `<details class="ex-more"><summary>Steps</summary><ol>${ex.steps.map(s=>`<li>${s}</li>`).join("")}</ol></details>` : ""}
                    ${ex.benefits.length ? `<details class="ex-more"><summary>Benefits</summary><ul>${ex.benefits.map(b=>`<li>${b}</li>`).join("")}</ul></details>` : ""}
                </div>
            </div>
            `).join("")}
        </div>
    `).join("")}
    </div>
</div>

<div class="card insights-card">
    <h2><i data-lucide="sparkles"></i> AI Health Insights</h2>
    <ul class="insights-list">
        ${data.ai_report.map(item => `<li><i data-lucide="check-circle"></i><span>${item}</span></li>`).join("")}
    </ul>
</div>

</div>

<div class="report-actions">
    <button id="downloadBtn" onclick="downloadPDF()" class="pdf-btn">
        <i data-lucide="download"></i> Download Report PDF
    </button>
</div>

<div class="disclaimer-note">
    <i data-lucide="info"></i>
    <span>${data.disclaimer}</span>
</div>
`;

    if (window.lucide) lucide.createIcons();
    animateCounters();
}