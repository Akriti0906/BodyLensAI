def generate_diet_plan(goal):
    
    if goal.lower() == "lose_weight":
        return {
            "breakfast": [
                "Oats",
                "Boiled Eggs / Paneer",
                "Green Tea"
            ],
            "lunch": [
                "Brown Rice",
                "Dal",
                "Salad"
            ],
            "dinner": [
                "Paneer / Chicken",
                "Vegetables"
            ]
        }

    elif goal.lower() == "gain_weight":
        return {
            "breakfast": [
                "Peanut Butter Toast",
                "Banana",
                "Milk"
            ],
            "lunch": [
                "Rice",
                "Dal",
                "Paneer / Chicken"
            ],
            "dinner": [
                "Chapati",
                "Paneer",
                "Dry Fruits"
            ]
        }

    else:
        return {
            "breakfast": [
                "Oats",
                "Fruits"
            ],
            "lunch": [
                "Rice",
                "Dal",
                "Vegetables"
            ],
            "dinner": [
                "Chapati",
                "Paneer",
                "Salad"
            ]
        }