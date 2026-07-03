def get_condition_advice(condition):

    condition = condition.lower()

    if condition == "pcos":
        return {
            "condition_advice":
            "Focus on strength training, walking, high protein diet and reducing processed sugar."
        }

    elif condition == "diabetes":
        return {
            "condition_advice":
            "Monitor carbohydrate intake, stay active daily and prioritize low glycemic foods."
        }

    elif condition == "knee_pain":
        return {
            "condition_advice":
            "Prefer low-impact exercises such as walking, cycling and swimming."
        }

    elif condition == "back_pain":
        return {
            "condition_advice":
            "Focus on posture improvement, stretching and core strengthening exercises."
        }
    elif condition == "none":
        return {
            "condition_advice":
            "No specific condition selected. Keep following your personalized plan and stay consistent."
        }

    else:
        return {
            "condition_advice":
            "No specific condition guidance available."
        }