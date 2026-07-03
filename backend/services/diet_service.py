def food(food, calories, protein, carbs, fat):
    return {
        "food": food,
        "calories": calories,
        "protein": protein,
        "carbs": carbs,
        "fat": fat
    }


def generate_diet_plan(goal, condition="none"):

    goal = goal.lower()
    condition = condition.lower()

    # -------------------------
    # LOSE WEIGHT
    # -------------------------
    if goal == "lose_weight":

        if condition == "pcos":

            return {

                "breakfast": [
                    food("Oats",180,6,30,3),
                    food("Boiled Eggs",140,12,1,10),
                    food("Green Tea",2,0,0,0)
                ],

                "lunch": [
                    food("Brown Rice",220,5,46,2),
                    food("Dal",180,10,25,2),
                    food("Mixed Salad",80,2,12,1)
                ],

                "dinner": [
                    food("Grilled Paneer",250,20,8,15),
                    food("Steamed Vegetables",90,4,18,1)
                ]

            }

        elif condition == "diabetes":

            return {

                "breakfast":[
                    food("Vegetable Omelette",220,18,5,12),
                    food("Multigrain Toast",120,5,22,2)
                ],

                "lunch":[
                    food("Brown Rice",220,5,46,2),
                    food("Dal",180,10,25,2),
                    food("Cucumber Salad",50,2,8,0)
                ],

                "dinner":[
                    food("Grilled Fish",260,28,0,12),
                    food("Broccoli",55,4,10,0)
                ]

            }

        else:

            return {

                "breakfast":[
                    food("Oats",180,6,30,3),
                    food("Boiled Eggs",140,12,1,10),
                    food("Green Tea",2,0,0,0)
                ],

                "lunch":[
                    food("Brown Rice",220,5,46,2),
                    food("Dal",180,10,25,2),
                    food("Salad",70,2,12,1)
                ],

                "dinner":[
                    food("Paneer",250,20,8,15),
                    food("Vegetables",90,4,18,1)
                ]

            }

    # -------------------------
    # GAIN WEIGHT
    # -------------------------

    elif goal == "gain_weight":

        return {

            "breakfast":[
                food("Peanut Butter Toast",320,14,28,16),
                food("Banana",110,1,27,0),
                food("Milk",150,8,12,8)
            ],

            "lunch":[
                food("Rice",250,5,52,1),
                food("Dal",180,10,25,2),
                food("Paneer",300,22,10,18)
            ],

            "dinner":[
                food("Chapati",180,6,36,3),
                food("Paneer",300,22,10,18),
                food("Dry Fruits",220,5,18,16)
            ]

        }

    # -------------------------
    # MAINTAIN
    # -------------------------

    else:

        return {

            "breakfast":[
                food("Oats",180,6,30,3),
                food("Fruits",120,2,28,0)
            ],

            "lunch":[
                food("Rice",220,5,46,2),
                food("Dal",180,10,25,2),
                food("Vegetables",90,4,18,1)
            ],

            "dinner":[
                food("Chapati",180,6,36,3),
                food("Paneer",250,20,8,15),
                food("Salad",70,2,12,1)
            ]

        }