from services.exercise_service import get_exercise_details


def generate_workout_plan(goal):

    if goal.lower() == "lose_weight":

        workout = {
            "monday": "Squats",
            "tuesday": "Push Ups",
            "wednesday": "Walking",
            "thursday": "Plank",
            "friday": "Lunges",
            "saturday": "Squats",
            "sunday": "Rest Day"
        }

    elif goal.lower() == "gain_weight":

        workout = {
            "monday": "Push Ups",
            "tuesday": "Squats",
            "wednesday": "Lunges",
            "thursday": "Plank",
            "friday": "Push Ups",
            "saturday": "Squats",
            "sunday": "Rest Day"
        }

    else:

        workout = {
            "monday": "Walking",
            "tuesday": "Plank",
            "wednesday": "Walking",
            "thursday": "Lunges",
            "friday": "Push Ups",
            "saturday": "Squats",
            "sunday": "Rest Day"
        }

    detailed_workout = {}

    for day, exercise in workout.items():

        if exercise == "Rest Day":

            detailed_workout[day] = {
                "name": "Rest Day",
                "image": "",
                "steps": [],
                "benefits": ["Allow your body to recover."]
            }

        else:

            details = get_exercise_details(exercise)

            detailed_workout[day] = {
                "name": exercise,
                "image": details["image"],
                "steps": details["steps"],
                "benefits": details["benefits"]
            }

    return detailed_workout