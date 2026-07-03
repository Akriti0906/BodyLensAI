def get_exercise_details(exercise):

    exercises = {

        "Squats": {
            "image": "images/exercises/squats.jpg",
            "steps": [
                "Stand with feet shoulder-width apart.",
                "Keep your back straight.",
                "Lower your body until thighs are parallel to the floor.",
                "Push back up through your heels."
            ],
            "benefits": [
                "Builds leg strength",
                "Improves balance",
                "Burns calories"
            ],
            "difficulty": "Beginner",
            "target_muscle": "Legs & Glutes",
            "calories": "55 kcal / 10 min"
        },

        "Push Ups": {
            "image": "images/exercises/pushups.jpg",
            "steps": [
                "Start in a high plank position.",
                "Lower your chest until elbows reach 90°.",
                "Push yourself back up."
            ],
            "benefits": [
                "Builds chest strength",
                "Strengthens shoulders",
                "Improves endurance"
            ],
            "difficulty": "Beginner",
            "target_muscle": "Chest, Shoulders, Triceps",
            "calories": "60 kcal / 10 min"
        },

        "Plank": {
            "image": "images/exercises/plank.jpg",
            "steps": [
                "Rest on your forearms.",
                "Keep your body in a straight line.",
                "Tighten your core.",
                "Hold the position."
            ],
            "benefits": [
                "Strengthens core",
                "Improves posture",
                "Reduces back pain"
            ],
            "difficulty": "Beginner",
            "target_muscle": "Core",
            "calories": "45 kcal / 10 min"
        },

        "Walking": {
            "image": "images/exercises/walking.jpg",
            "steps": [
                "Walk with an upright posture.",
                "Swing your arms naturally.",
                "Maintain a brisk pace."
            ],
            "benefits": [
                "Improves heart health",
                "Burns fat",
                "Boosts stamina"
            ],
            "difficulty": "Easy",
            "target_muscle": "Full Body",
            "calories": "40 kcal / 10 min"
        },

        "Lunges": {
            "image": "images/exercises/lunges.jpg",
            "steps": [
                "Stand upright.",
                "Step one leg forward.",
                "Lower both knees.",
                "Push back to standing."
            ],
            "benefits": [
                "Strengthens legs",
                "Improves balance",
                "Targets glutes"
            ],
            "difficulty": "Beginner",
            "target_muscle": "Legs & Glutes",
            "calories": "58 kcal / 10 min"
        }

    }

    return exercises.get(
        exercise,
        {
            "image": "",
            "steps": [],
            "benefits": [],
            "difficulty": "",
            "target_muscle": "",
            "calories": ""
        }
    )