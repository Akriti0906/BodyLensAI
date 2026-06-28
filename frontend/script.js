async function calculateBMI() {

    const button = document.querySelector("button");

    const bodyData = {
        age: Number(document.getElementById("age").value),
        gender: document.getElementById("gender").value,
        height_cm: Number(document.getElementById("height").value),
        weight_kg: Number(document.getElementById("weight").value),
        activity_level: document.getElementById("activity").value,
        goal: document.getElementById("goal").value,
        condition: document.getElementById("condition").value
    };

    if (!validateInputs(bodyData)) {
        return;
    }

    try {

        button.disabled = true;
        button.innerHTML = "⏳ Analyzing...";

        console.log("Sending Request...");
        console.log(bodyData);

        const data = await getHealthReport(bodyData);

        console.log("Backend Response:");
        console.log(data);

        renderResult(data);

    }
    catch (error) {

        console.error("Frontend Error:", error);

        if (error instanceof TypeError) {
            alert("Cannot connect to backend. Make sure FastAPI server is running on http://127.0.0.1:8000");
        } else {
            alert(error.message);
        }

    }
    finally {

        button.disabled = false;
        button.innerHTML = "Analyze My Body";

    }
}