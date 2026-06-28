from services.diet_service import generate_diet_plan
from services.condition_service import get_condition_advice
from services.workout_service import generate_workout_plan


def calculate_bmi_and_recommendation(
    age,
    gender,
    height_cm,
    weight_kg,
    activity_level,
    goal,
    condition
):
    # BMI Calculation
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

    # Protein & Water
    protein_g = round(weight_kg * 1.6)
    water_liters = round(weight_kg * 0.035, 1)

    # Diet & Workout
    diet_plan = generate_diet_plan(goal)
    workout_plan = generate_workout_plan(goal)
    condition_data = get_condition_advice(condition)

    # ==========================
    # AI Health Profile
    # ==========================

    # Body Type
    if bmi < 18.5:
        body_type = "Lean"
    elif bmi < 22:
        body_type = "Lean Fit"
    elif bmi < 25:
        body_type = "Fit"
    elif bmi < 30:
        body_type = "Heavy Build"
    else:
        body_type = "Obese"

    # Fitness Level
    activity = activity_level.lower()

    if activity == "sedentary":
        fitness_level = "Beginner"
    elif activity == "lightly_active":
        fitness_level = "Intermediate"
    elif activity == "moderately_active":
        fitness_level = "Active"
    else:
        fitness_level = "Athlete"

    # Risk Level
    if bmi < 18.5:
        risk_level = "Moderate"
    elif bmi < 25:
        risk_level = "Low"
    elif bmi < 30:
        risk_level = "Moderate"
    else:
        risk_level = "High"

    # Goal Difficulty
    if goal.lower() == "maintain_weight":
        goal_difficulty = "Easy"
    elif goal.lower() == "lose_weight":
        goal_difficulty = "Moderate"
    elif goal.lower() == "gain_weight":
        goal_difficulty = "Challenging"
    else:
        goal_difficulty = "Moderate"

    # Health Score
    score = 100

    if bmi < 18.5 or bmi >= 30:
        score -= 25
    elif bmi >= 25:
        score -= 10

    if activity == "sedentary":
        score -= 15
    elif activity == "lightly_active":
        score -= 5

    if age >= 40:
        score -= 5

    if score < 0:
        score = 0

    return {
        "bmi": round(bmi, 2),
        "category": category,
        "recommendation": recommendation,
        "goal": goal,
        "condition": condition,
        "condition_advice": condition_data["condition_advice"],
        "target_calories": target_calories,
        "workout_type": workout_type,
        "protein_g": protein_g,
        "water_liters": water_liters,
        "diet_plan": diet_plan,
        "workout_plan": workout_plan,
        "health_profile": {
            "body_type": body_type,
            "fitness_level": fitness_level,
            "risk_level": risk_level,
            "goal_difficulty": goal_difficulty,
            "health_score": score
        }
    }