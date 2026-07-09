from services.report_service import save_report
from services.ai_report_service import generate_ai_report
from services.diet_service import generate_diet_plan
from services.condition_service import get_condition_advice
from services.workout_service import generate_workout_plan
from services.score_service import calculate_health_score


def calculate_bmi_and_recommendation(
    age,
    gender,
    height_cm,
    weight_kg,
    activity_level,
    goal,
    condition
):
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)

    if bmi < 18.5:
        category = "Underweight"
        recommendation = "Increase calorie intake and follow a weight gain workout plan."

    elif bmi < 25:
        category = "Normal Weight"
        recommendation = "Maintain your current weight and perform moderate exercise regularly."

    elif bmi < 30:
        category = "Overweight"
        recommendation = "Focus on fat loss through cardio and a calorie deficit diet."

    else:
        category = "Obese"
        recommendation = "Consult a healthcare professional and start with low-impact exercises."

    # BMR Calculation
    if gender.lower() == "male":
        bmr = (10 * weight_kg) + (6.25 * height_cm) - (5 * age) + 5
    else:
        bmr = (10 * weight_kg) + (6.25 * height_cm) - (5 * age) - 161

    multipliers = {
        "sedentary": 1.2,
        "lightly_active": 1.375,
        "moderately_active": 1.55,
        "very_active": 1.725
    }

    multiplier = multipliers.get(activity_level.lower(), 1.2)

    maintenance_calories = round(bmr * multiplier)
    weight_loss_calories = maintenance_calories - 500
    weight_gain_calories = maintenance_calories + 300

    if goal.lower() == "lose_weight":
        target_calories = weight_loss_calories
        workout_type = "Cardio + Strength Training"

    elif goal.lower() == "gain_weight":
        target_calories = weight_gain_calories
        workout_type = "Strength Training"

    else:
        target_calories = maintenance_calories
        workout_type = "Balanced Fitness Routine"

    protein_g = round(weight_kg * 1.6)
    water_liters = round(weight_kg * 0.035, 1)

    # Services
    diet_plan = generate_diet_plan(
        goal,
        condition)
    workout_plan = generate_workout_plan(goal, condition)
    condition_data = get_condition_advice(condition)

    # Health Score
    health_score, risk_level = calculate_health_score(
        bmi,
        activity_level,
        condition
    )

    # AI Report
    ai_report = generate_ai_report(
        bmi=bmi,
        category=category,
        goal=goal,
        activity_level=activity_level,
        condition=condition,
        health_score=health_score,
        risk_level=risk_level
    )
    try:
        save_report({
             "age": age,
            "gender": gender,
            "height": height_cm,
            "weight": weight_kg,
            "bmi": round(bmi, 2),
            "category": category,
            "goal": goal,
            "condition": condition,
            "activity_level": activity_level,
            "calories": target_calories,
            "protein": protein_g,
            "water": water_liters,
            "health_score": health_score,
            "risk_level": risk_level
          })   # the dict you already have
    except Exception as e:
        print(f"[save_report] Failed to persist report: {e}")
   


    return {
        "bmi": round(bmi, 2),
        "category": category,
        "recommendation": recommendation,
        "disclaimer": "This report is generated automatically for general informational purposes only. It is not medical advice. Consult a qualified healthcare professional before making health, diet, or exercise decisions.", 
        "goal": goal,
        "condition": condition,
        "condition_advice": condition_data["condition_advice"],
        "target_calories": target_calories,
        "workout_type": workout_type,
        "protein_g": protein_g,
        "water_liters": water_liters,
        "diet_plan": diet_plan,
        "workout_plan": workout_plan,
        "health_score": health_score,
        "risk_level": risk_level,
        "ai_report": ai_report
    }