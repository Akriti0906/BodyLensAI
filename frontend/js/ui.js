function getBadge(category) {

    if (category === "Underweight") return "underweight";

    if (category === "Normal Weight") return "normal";

    if (category === "Overweight") return "overweight";

    return "obese";

}

function renderResult(data) {

    const badge = getBadge(data.category);

    document.getElementById("result").innerHTML = `

    <h2 class="report-title">📊 Your Health Report</h2>

    <div class="dashboard">

        <div class="info-card">
            <h3>📊 BMI</h3>
            <p>${data.bmi}</p>
        </div>

        <div class="info-card">
            <h3>🔥 Calories</h3>
            <p>${data.target_calories} kcal</p>
        </div>

        <div class="info-card">
            <h3>🍗 Protein</h3>
            <p>${data.protein_g} g</p>
        </div>

        <div class="info-card">
            <h3>💧 Water</h3>
            <p>${data.water_liters} L</p>
        </div>

    </div>

    <div class="card">

        <div class="badge ${badge}">
            ${data.category}
        </div>

        <p><b>🎯 Goal:</b> ${data.goal}</p>

        <p><b>🏋 Workout:</b> ${data.workout_type}</p>

        <p><b>❤️ Advice:</b> ${data.condition_advice}</p>

    </div>

    <div class="card">

        <h3>🥗 Diet Plan</h3>

        <h4>Breakfast</h4>

        <ul>

        ${data.diet_plan.breakfast.map(item=>`<li>${item}</li>`).join("")}

        </ul>

        <h4>Lunch</h4>

        <ul>

        ${data.diet_plan.lunch.map(item=>`<li>${item}</li>`).join("")}

        </ul>

        <h4>Dinner</h4>

        <ul>

        ${data.diet_plan.dinner.map(item=>`<li>${item}</li>`).join("")}

        </ul>

    </div>

    <div class="card">

        <h3>💪 Weekly Workout</h3>

        <ul>

            <li>Monday : ${data.workout_plan.monday}</li>

            <li>Tuesday : ${data.workout_plan.tuesday}</li>

            <li>Wednesday : ${data.workout_plan.wednesday}</li>

            <li>Thursday : ${data.workout_plan.thursday}</li>

            <li>Friday : ${data.workout_plan.friday}</li>

            <li>Saturday : ${data.workout_plan.saturday}</li>

            <li>Sunday : ${data.workout_plan.sunday}</li>

        </ul>

    </div>

    `;

}