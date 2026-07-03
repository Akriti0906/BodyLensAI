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

// Save report for PDF
window.lastReport = data;

try {

    console.log("renderResult started");
    console.log(document.getElementById("result"));

    renderResult(data);

    console.log("renderResult finished");

} catch (e) {

    console.error("Render Error:", e);

}

     

        // Show download button
        const downloadBtn = document.getElementById("downloadBtn");
        if (downloadBtn) {
            downloadBtn.style.display = "inline-block";
        }

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

function downloadPDF() {

    if (!window.lastReport) {
        alert("Generate a report first.");
        return;
    }

    const { jsPDF } = window.jspdf;
    const doc = new jsPDF();

    const data = window.lastReport;

    let y = 20;

    doc.setFontSize(18);
    doc.text("BodyLens AI - Health Report", 20, y);

    y += 15;
    doc.setFontSize(12);

    doc.text(`BMI: ${data.bmi}`, 20, y);
    y += 8;

    doc.text(`Category: ${data.category}`, 20, y);
    y += 8;

    doc.text(`Health Score: ${data.health_score}`, 20, y);
    y += 8;

    doc.text(`Risk Level: ${data.risk_level}`, 20, y);
    y += 8;

    doc.text(`Calories: ${data.target_calories} kcal`, 20, y);
    y += 8;

    doc.text(`Protein: ${data.protein_g} g`, 20, y);
    y += 8;

    doc.text(`Water Intake: ${data.water_liters} L`, 20, y);
    y += 15;

    doc.setFontSize(14);
    doc.text("Diet Plan", 20, y);

    y += 10;
    doc.setFontSize(12);

    doc.text("Breakfast:", 20, y);
    y += 7;
    data.diet_plan.breakfast.forEach(item => {
        doc.text("- " + item, 25, y);
        y += 6;
    });

    y += 4;
    doc.text("Lunch:", 20, y);
    y += 7;
    data.diet_plan.lunch.forEach(item => {
        doc.text("- " + item, 25, y);
        y += 6;
    });

    y += 4;
    doc.text("Dinner:", 20, y);
    y += 7;
    data.diet_plan.dinner.forEach(item => {
        doc.text("- " + item, 25, y);
        y += 6;
    });

    y += 10;

    doc.setFontSize(14);
    doc.text("Workout Plan", 20, y);

    y += 10;
    doc.setFontSize(12);

    for (const day in data.workout_plan) {
        doc.text(`${day}: ${data.workout_plan[day]}`, 20, y);
        y += 7;
    }

    y += 5;

    doc.setFontSize(14);
    doc.text("Condition Advice", 20, y);

    y += 10;
    doc.setFontSize(12);

    doc.text(data.condition_advice, 20, y, {
        maxWidth: 170
    });

    doc.save("BodyLensAI_Health_Report.pdf");
}
async function downloadPDF() {

    const { jsPDF } = window.jspdf;

    const element = document.getElementById("pdf-content");

    const canvas = await html2canvas(element, {
        scale: 2,
        useCORS: true,
        backgroundColor: "#ffffff"
    });

    const imgData = canvas.toDataURL("image/png");

    const pdf = new jsPDF("p", "mm", "a4");

    const pageWidth = pdf.internal.pageSize.getWidth();
    const pageHeight = pdf.internal.pageSize.getHeight();

    const imgWidth = pageWidth;
    const imgHeight = (canvas.height * imgWidth) / canvas.width;

    let heightLeft = imgHeight;
    let position = 0;

    pdf.addImage(imgData, "PNG", 0, position, imgWidth, imgHeight);

    heightLeft -= pageHeight;

    while (heightLeft > 0) {

        position = heightLeft - imgHeight;

        pdf.addPage();

        pdf.addImage(imgData, "PNG", 0, position, imgWidth, imgHeight);

        heightLeft -= pageHeight;
    }

    pdf.save("BodyLensAI_Report.pdf");
}