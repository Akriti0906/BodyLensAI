def generate_ai_report(
    bmi,
    category,
    goal,
    activity_level,
    condition,
    health_score,
    risk_level
):

    report = []

    # BMI Analysis
    if category == "Normal Weight":
        report.append(
            "Your BMI falls within the healthy range, suggesting a balanced body weight for your height."
        )

    elif category == "Underweight":
        report.append(
            "Your BMI indicates that you are underweight. A nutritious calorie surplus along with strength training may help you gain healthy weight."
        )

    elif category == "Overweight":
        report.append(
            "Your BMI suggests that you are overweight. Gradual fat loss through balanced nutrition and regular exercise can improve overall health."
        )

    else:
        report.append(
            "Your BMI falls in the obesity range. A structured nutrition and exercise plan may help reduce health risks over time."
        )

    # Goal
    if goal == "lose_weight":
        report.append(
            "Focus on creating a moderate calorie deficit while maintaining adequate protein intake to preserve muscle."
        )

    elif goal == "gain_weight":
        report.append(
            "Aim for a healthy calorie surplus with strength training to support lean muscle gain."
        )

    else:
        report.append(
            "Maintain your current lifestyle by balancing nutrition and regular physical activity."
        )

    # Activity
    if activity_level == "sedentary":
        report.append(
            "Increasing daily movement such as walking or light exercise can significantly improve your overall fitness."
        )

    elif activity_level == "lightly_active":
        report.append(
            "Building a consistent workout routine can further improve endurance and overall health."
        )

    elif activity_level == "moderately_active":
        report.append(
            "Your activity level is good. Staying consistent will help maintain your current fitness."
        )

    else:
        report.append(
            "Your active lifestyle supports cardiovascular health and muscle maintenance."
        )

    # Condition
    if condition != "none":
        report.append(
            f"Since you selected '{condition}', follow the recommended workout and nutrition plan carefully. Consult a healthcare professional for personalized medical advice if needed."
        )

    # Health Score
    report.append(
        f"Your overall Health Score is {health_score}/100 with a {risk_level}. Continue building healthy habits for long-term wellness."
    )

    report.append(
        "This report provides general fitness guidance and should not replace professional medical advice."
    )

    return report