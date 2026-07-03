def generate_action_plan(goal, activity_level, water_liters, protein_g):

    plan = []

    # Goal
    if goal == "lose_weight":
        plan.append("Maintain a moderate calorie deficit.")
        plan.append("Walk at least 8,000–10,000 steps daily.")

    elif goal == "gain_weight":
        plan.append("Eat in a healthy calorie surplus.")
        plan.append("Focus on progressive strength training.")

    else:
        plan.append("Maintain your current healthy lifestyle.")

    # Activity
    if activity_level == "sedentary":
        plan.append("Exercise at least 30 minutes every day.")

    elif activity_level == "lightly_active":
        plan.append("Increase workouts to 4 days per week.")

    elif activity_level == "moderately_active":
        plan.append("Continue exercising 4–5 days each week.")

    else:
        plan.append("Maintain your current active routine.")

    # Water
    plan.append(f"Drink at least {water_liters} L of water every day.")

    # Protein
    plan.append(f"Consume around {protein_g} g of protein daily.")

    # Sleep
    plan.append("Sleep for 7–8 hours every night.")

    # Lifestyle
    plan.append("Limit sugary drinks and processed foods.")

    return plan