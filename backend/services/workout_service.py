def generate_workout_plan(goal):

    if goal.lower() == "lose_weight":
        return {
            "monday": "30 min Cardio + Squats",
            "tuesday": "Upper Body Workout",
            "wednesday": "Walking + Abs Workout",
            "thursday": "Strength Training",
            "friday": "HIIT Workout",
            "saturday": "Full Body Workout",
            "sunday": "Rest Day"
        }

    elif goal.lower() == "gain_weight":
        return {
            "monday": "Chest + Triceps",
            "tuesday": "Back + Biceps",
            "wednesday": "Leg Day",
            "thursday": "Shoulders",
            "friday": "Arms",
            "saturday": "Full Body Strength",
            "sunday": "Rest Day"
        }

    else:
        return {
            "monday": "Walking",
            "tuesday": "Light Strength Training",
            "wednesday": "Yoga",
            "thursday": "Walking",
            "friday": "Bodyweight Workout",
            "saturday": "Stretching",
            "sunday": "Rest Day"
        }