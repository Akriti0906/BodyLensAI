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

function renderResult(data) {

    const badge = getBadge(data.category);
    const riskClass = getRiskClass(data.risk_level);

    document.getElementById("result").innerHTML = `

<div id="pdf-content">

<h2 class="report-title">📊 Your Health Report</h2>

<div class="dashboard">

    <div class="info-card score-card">

        <h3>❤️ Health Score</h3>

        <div class="progress-circle">

            <svg width="140" height="140">

                <circle
                    cx="70"
                    cy="70"
                    r="55"
                    class="circle-bg"
                />

                <circle
                    cx="70"
                    cy="70"
                    r="55"
                    class="circle-progress"
                    stroke-dasharray="${healthProgress(data.health_score)} 360"
                />

            </svg>

            <div class="circle-text">

                ${data.health_score}

            </div>

        </div>

        <small>${data.risk_level}</small>

    </div>

    <div class="info-card">

        <h3>📊 BMI</h3>

        <h1>${data.bmi}</h1>

        <div class="bmi-bar">

            <div
                class="bmi-fill"
                style="width:${bmiProgress(data.bmi)}%">
            </div>

        </div>

        <p>${data.category}</p>

    </div>

    <div class="info-card">

        <h3>🔥 Daily Targets</h3>

        <p>Calories : <b>${data.target_calories}</b></p>

        <p>Protein : <b>${data.protein_g} g</b></p>

        <p>Water : <b>${data.water_liters} L</b></p>

    </div>

</div>

<div class="card">

<div class="badge ${badge}">
${data.category}
</div>

<p><b>🎯 Goal:</b> ${data.goal}</p>

<p><b>🏋 Workout Type:</b> ${data.workout_type}</p>

<p><b>❤️ Advice:</b> ${data.condition_advice}</p>

</div>


<div class="card">

<h2>🥗 Personalized Diet Plan</h2>

${Object.entries(data.diet_plan).map(([meal, foods]) => {

let totalCalories = 0;
let totalProtein = 0;
let totalCarbs = 0;
let totalFat = 0;

foods.forEach(food => {
    totalCalories += food.calories;
    totalProtein += food.protein;
    totalCarbs += food.carbs;
    totalFat += food.fat;
});

return `

<h3 style="margin-top:30px;">
${meal.charAt(0).toUpperCase() + meal.slice(1)}
</h3>

<table class="diet-table">

<tr>

<th>Food</th>

<th>Calories</th>

<th>Protein</th>

<th>Carbs</th>

<th>Fat</th>

</tr>

${foods.map(food => `

<tr>

<td>${food.food}</td>

<td>${food.calories}</td>

<td>${food.protein} g</td>

<td>${food.carbs} g</td>

<td>${food.fat} g</td>

</tr>

`).join("")}

<tr class="total-row">

<td><b>Total</b></td>

<td><b>${totalCalories}</b></td>

<td><b>${totalProtein} g</b></td>

<td><b>${totalCarbs} g</b></td>

<td><b>${totalFat} g</b></td>

</tr>

</table>

`;

}).join("")}

</div>



<div class="card">

<h2>💪 Weekly Exercise Guide</h2>

${Object.entries(data.workout_plan).map(([day, exercise]) => `

<div class="exercise-card">

<h3>${day.charAt(0).toUpperCase() + day.slice(1)}</h3>

<h2>${exercise.name}</h2>

${exercise.image ? `
<img src="${exercise.image}" class="exercise-img" alt="${exercise.name}">
` : ""}

${exercise.video ? `
<div style="text-align:center; margin:15px 0;">
    <a href="${exercise.video}"
       target="_blank"
       class="video-btn">
       ▶ Watch Exercise Demo
    </a>
</div>
` : ""}

<div class="exercise-details">

<p><b>🎯 Target Muscle:</b> ${exercise.target_muscle}</p>

<p><b>⭐ Difficulty:</b> ${exercise.difficulty}</p>

<p><b>🔥 Calories Burn:</b> ${exercise.calories}</p>

</div>

${exercise.steps.length ? `

<h4>📋 Steps</h4>

<ol>

${exercise.steps.map(step => `
<li>${step}</li>
`).join("")}

</ol>

` : ""}

${exercise.benefits.length ? `

<h4>✅ Benefits</h4>

<ul>

${exercise.benefits.map(item => `
<li>${item}</li>
`).join("")}

</ul>

` : ""}

</div>

`).join("")}

</div>



<div class="card">

<h2>🤖 AI Health Insights</h2>

<ul>

${data.ai_report.map(item => `
<li>${item}</li>`).join("")}

</ul>

</div>

</div>   <!-- pdf-content closes here -->

<div style="text-align:center;margin-top:30px;">
<button
    id="downloadBtn"
    onclick="downloadPDF()"
    class="pdf-btn">

📄 Download Report PDF

</button>

</div>
<div class="card">
        <p style="font-size:14px;color:gray;">
            ⚠️ ${data.disclaimer}
        </p>
    </div>

`;

}