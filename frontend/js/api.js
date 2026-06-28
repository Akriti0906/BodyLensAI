async function getHealthReport(bodyData) {

    const response = await fetch("http://127.0.0.1:8000/bmi", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify(bodyData)

    });

    if (!response.ok) {

        throw new Error("Failed to fetch health report.");

    }

    return await response.json();

}