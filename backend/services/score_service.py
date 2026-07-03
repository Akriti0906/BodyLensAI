def calculate_health_score(bmi, activity_level, condition):
    score = 100

    # BMI Score
    if bmi < 18.5:
        score -= 15
    elif bmi < 25:
        score -= 0
    elif bmi < 30:
        score -= 10
    else:
        score -= 25

    # Activity Score
    activity = activity_level.lower()

    if activity == "sedentary":
        score -= 15
    elif activity == "lightly_active":
        score -= 8
    elif activity == "moderately_active":
        score -= 3
    elif activity == "very_active":
        score -= 0

    # Medical Condition
    if condition.lower() != "none":
        score -= 10

    score = max(0, min(score, 100))

    if score >= 80:
        risk = "Low Risk"
    elif score >= 60:
        risk = "Moderate Risk"
    else:
        risk = "High Risk"

    return score, risk