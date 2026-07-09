"""
Exercise Library for BodyLens AI
=================================
A richer, categorized library of exercises used by the multi-exercise
workout generator (workout_service.generate_workout_plan).
 
This file is ADDITIVE. It does not replace exercise_service.get_exercise_details,
which older code may still use. Each exercise is a self-contained dict with all
fields the frontend (ui.js) renders.
 
Categories are used by the workout generator to build balanced daily sessions:
    - cardio        : elevates heart rate, burns calories
    - legs          : lower-body strength
    - upper         : chest / shoulders / arms / back
    - core          : abs and lower back
    - low_impact    : joint-friendly, safe for knee/back pain
    - mobility      : stretching / warm-up / cool-down
 
Every exercise carries a set of "tags" describing which conditions it is
SAFE for or should be AVOIDED for, so the generator can filter by medical
condition (knee_pain, back_pain, pcos, diabetes).
"""
 
# Base path for images. Frontend serves these from /frontend/images/exercises/.
# Kept relative so it works regardless of how Live Server is rooted; ui.js
# already handles a missing file gracefully via onerror.
IMG = "images/exercises"
 
 
EXERCISE_LIBRARY = {
 
    # ============================================================
    # CARDIO
    # ============================================================
    "Jumping Jacks": {
        "name": "Jumping Jacks",
        "category": "cardio",
        "image": f"{IMG}/jumping_jacks.jpg",
        "video": "https://www.youtube.com/results?search_query=jumping+jacks+form",
        "target_muscle": "Full Body",
        "difficulty": "Beginner",
        "calories": "80 kcal / 10 min",
        "prescription": "3 sets x 40 seconds",
        "steps": [
            "Stand upright with arms at your sides.",
            "Jump while spreading your legs and raising your arms overhead.",
            "Jump again to return to the starting position.",
            "Keep a steady, continuous rhythm."
        ],
        "benefits": [
            "Raises heart rate quickly",
            "Burns calories",
            "Improves coordination"
        ],
        "avoid": ["knee_pain"],
    },
 
    "High Knees": {
        "name": "High Knees",
        "category": "cardio",
        "image": f"{IMG}/high_knees.jpg",
        "video": "https://www.youtube.com/results?search_query=high+knees+exercise",
        "target_muscle": "Legs & Core",
        "difficulty": "Intermediate",
        "calories": "90 kcal / 10 min",
        "prescription": "3 sets x 30 seconds",
        "steps": [
            "Stand tall with feet hip-width apart.",
            "Drive one knee up toward your chest.",
            "Quickly switch legs in a running motion.",
            "Pump your arms as you go."
        ],
        "benefits": [
            "Boosts cardiovascular fitness",
            "Strengthens legs",
            "Improves running form"
        ],
        "avoid": ["knee_pain"],
    },
 
    "Brisk Walking": {
        "name": "Brisk Walking",
        "category": "low_impact",
        "image": f"{IMG}/walking.jpg",
        "video": "https://www.youtube.com/results?search_query=brisk+walking+workout",
        "target_muscle": "Full Body",
        "difficulty": "Easy",
        "calories": "50 kcal / 10 min",
        "prescription": "20-30 minutes",
        "steps": [
            "Walk with an upright posture.",
            "Swing your arms naturally.",
            "Maintain a brisk, steady pace.",
            "Breathe rhythmically."
        ],
        "benefits": [
            "Improves heart health",
            "Gentle on joints",
            "Burns fat steadily"
        ],
        "avoid": [],
    },
 
    "Marching In Place": {
        "name": "Marching In Place",
        "category": "low_impact",
        "image": f"{IMG}/marching.jpg",
        "video": "https://www.youtube.com/results?search_query=marching+in+place+low+impact",
        "target_muscle": "Legs & Core",
        "difficulty": "Easy",
        "calories": "45 kcal / 10 min",
        "prescription": "3 sets x 60 seconds",
        "steps": [
            "Stand tall with a straight back.",
            "Lift one knee to hip height.",
            "Lower and lift the other knee.",
            "Swing your arms gently."
        ],
        "benefits": [
            "Safe low-impact cardio",
            "Easy on knees and back",
            "Warms up the body"
        ],
        "avoid": [],
    },
 
    # ============================================================
    # LEGS
    # ============================================================
    "Squats": {
        "name": "Squats",
        "category": "legs",
        "image": f"{IMG}/squats.jpg",
        "video": "https://www.youtube.com/results?search_query=bodyweight+squat+form",
        "target_muscle": "Legs & Glutes",
        "difficulty": "Beginner",
        "calories": "55 kcal / 10 min",
        "prescription": "3 sets x 12 reps",
        "steps": [
            "Stand with feet shoulder-width apart.",
            "Keep your back straight and chest up.",
            "Lower your body until thighs are parallel to the floor.",
            "Push back up through your heels."
        ],
        "benefits": [
            "Builds leg strength",
            "Improves balance",
            "Burns calories"
        ],
        "avoid": ["knee_pain"],
    },
 
    "Lunges": {
        "name": "Lunges",
        "category": "legs",
        "image": f"{IMG}/lunges.jpg",
        "video": "https://www.youtube.com/results?search_query=lunges+exercise+form",
        "target_muscle": "Legs & Glutes",
        "difficulty": "Beginner",
        "calories": "58 kcal / 10 min",
        "prescription": "3 sets x 10 reps each leg",
        "steps": [
            "Stand upright with feet together.",
            "Step one leg forward.",
            "Lower both knees to about 90 degrees.",
            "Push back to standing and switch legs."
        ],
        "benefits": [
            "Strengthens legs",
            "Improves balance",
            "Targets glutes"
        ],
        "avoid": ["knee_pain"],
    },
 
    "Glute Bridge": {
        "name": "Glute Bridge",
        "category": "legs",
        "image": f"{IMG}/glute_bridge.jpg",
        "video": "https://www.youtube.com/results?search_query=glute+bridge+exercise",
        "target_muscle": "Glutes & Lower Back",
        "difficulty": "Beginner",
        "calories": "40 kcal / 10 min",
        "prescription": "3 sets x 15 reps",
        "steps": [
            "Lie on your back with knees bent, feet flat.",
            "Push through your heels to lift your hips.",
            "Squeeze your glutes at the top.",
            "Lower slowly and repeat."
        ],
        "benefits": [
            "Strengthens glutes",
            "Supports lower back",
            "Safe for most conditions"
        ],
        "avoid": [],
    },
 
    "Wall Sit": {
        "name": "Wall Sit",
        "category": "legs",
        "image": f"{IMG}/wall_sit.jpg",
        "video": "https://www.youtube.com/results?search_query=wall+sit+exercise",
        "target_muscle": "Legs & Glutes",
        "difficulty": "Intermediate",
        "calories": "50 kcal / 10 min",
        "prescription": "3 sets x 30-45 seconds",
        "steps": [
            "Stand with your back against a wall.",
            "Slide down until your knees are at 90 degrees.",
            "Keep your back flat against the wall.",
            "Hold the position."
        ],
        "benefits": [
            "Builds leg endurance",
            "Low movement, controlled load",
            "Strengthens quads"
        ],
        "avoid": ["knee_pain"],
    },
 
    # ============================================================
    # UPPER BODY
    # ============================================================
    "Push Ups": {
        "name": "Push Ups",
        "category": "upper",
        "image": f"{IMG}/pushups.jpg",
        "video": "https://www.youtube.com/results?search_query=push+up+form",
        "target_muscle": "Chest, Shoulders, Triceps",
        "difficulty": "Beginner",
        "calories": "60 kcal / 10 min",
        "prescription": "3 sets x 10 reps",
        "steps": [
            "Start in a high plank position.",
            "Keep your body in a straight line.",
            "Lower your chest until elbows reach about 90 degrees.",
            "Push yourself back up."
        ],
        "benefits": [
            "Builds chest strength",
            "Strengthens shoulders",
            "Improves endurance"
        ],
        "avoid": [],
    },
 
    "Knee Push Ups": {
        "name": "Knee Push Ups",
        "category": "upper",
        "image": f"{IMG}/knee_pushups.jpg",
        "video": "https://www.youtube.com/results?search_query=knee+push+ups",
        "target_muscle": "Chest, Shoulders, Triceps",
        "difficulty": "Easy",
        "calories": "45 kcal / 10 min",
        "prescription": "3 sets x 12 reps",
        "steps": [
            "Start on your hands and knees.",
            "Keep a straight line from head to knees.",
            "Lower your chest toward the floor.",
            "Push back up."
        ],
        "benefits": [
            "Beginner-friendly upper body work",
            "Builds pushing strength gradually",
            "Lower joint stress"
        ],
        "avoid": [],
    },
 
    "Arm Circles": {
        "name": "Arm Circles",
        "category": "upper",
        "image": f"{IMG}/arm_circles.jpg",
        "video": "https://www.youtube.com/results?search_query=arm+circles+exercise",
        "target_muscle": "Shoulders",
        "difficulty": "Easy",
        "calories": "30 kcal / 10 min",
        "prescription": "2 sets x 30 seconds each direction",
        "steps": [
            "Stand with arms extended out to the sides.",
            "Make small circles forward.",
            "After 30 seconds, reverse direction.",
            "Keep arms straight."
        ],
        "benefits": [
            "Warms up shoulders",
            "Improves mobility",
            "Very low impact"
        ],
        "avoid": [],
    },
 
    "Superman Hold": {
        "name": "Superman Hold",
        "category": "upper",
        "image": f"{IMG}/superman.jpg",
        "video": "https://www.youtube.com/results?search_query=superman+exercise+back",
        "target_muscle": "Back & Glutes",
        "difficulty": "Beginner",
        "calories": "35 kcal / 10 min",
        "prescription": "3 sets x 15 seconds",
        "steps": [
            "Lie face down with arms extended forward.",
            "Lift your arms, chest, and legs off the floor.",
            "Hold briefly, squeezing your back.",
            "Lower slowly."
        ],
        "benefits": [
            "Strengthens lower back",
            "Improves posture",
            "Supports the spine"
        ],
        "avoid": [],
    },
 
    # ============================================================
    # CORE
    # ============================================================
    "Plank": {
        "name": "Plank",
        "category": "core",
        "image": f"{IMG}/plank.jpg",
        "video": "https://www.youtube.com/results?search_query=plank+exercise+form",
        "target_muscle": "Core",
        "difficulty": "Beginner",
        "calories": "45 kcal / 10 min",
        "prescription": "3 sets x 30 seconds",
        "steps": [
            "Rest on your forearms and toes.",
            "Keep your body in a straight line.",
            "Tighten your core.",
            "Hold the position without dropping your hips."
        ],
        "benefits": [
            "Strengthens core",
            "Improves posture",
            "Reduces back pain"
        ],
        "avoid": [],
    },
 
    "Dead Bug": {
        "name": "Dead Bug",
        "category": "core",
        "image": f"{IMG}/dead_bug.jpg",
        "video": "https://www.youtube.com/results?search_query=dead+bug+core+exercise",
        "target_muscle": "Core",
        "difficulty": "Beginner",
        "calories": "35 kcal / 10 min",
        "prescription": "3 sets x 10 reps each side",
        "steps": [
            "Lie on your back, arms pointing up, knees bent at 90 degrees.",
            "Lower one arm and the opposite leg slowly.",
            "Return to start.",
            "Alternate sides while keeping your back flat."
        ],
        "benefits": [
            "Safe core strengthening",
            "Protects the lower back",
            "Improves stability"
        ],
        "avoid": [],
    },
 
    "Bird Dog": {
        "name": "Bird Dog",
        "category": "core",
        "image": f"{IMG}/bird_dog.jpg",
        "video": "https://www.youtube.com/results?search_query=bird+dog+exercise",
        "target_muscle": "Core & Lower Back",
        "difficulty": "Beginner",
        "calories": "35 kcal / 10 min",
        "prescription": "3 sets x 10 reps each side",
        "steps": [
            "Start on your hands and knees.",
            "Extend one arm forward and the opposite leg back.",
            "Keep your hips level and back flat.",
            "Return and switch sides."
        ],
        "benefits": [
            "Strengthens core and back",
            "Very gentle on the spine",
            "Improves balance"
        ],
        "avoid": [],
    },
 
    "Seated Knee Lifts": {
        "name": "Seated Knee Lifts",
        "category": "core",
        "image": f"{IMG}/seated_knee_lifts.jpg",
        "video": "https://www.youtube.com/results?search_query=seated+knee+lifts",
        "target_muscle": "Lower Abs",
        "difficulty": "Easy",
        "calories": "30 kcal / 10 min",
        "prescription": "3 sets x 12 reps",
        "steps": [
            "Sit tall on the edge of a chair.",
            "Hold the sides for support.",
            "Lift both knees toward your chest.",
            "Lower slowly and repeat."
        ],
        "benefits": [
            "Gentle ab activation",
            "Chair-based and accessible",
            "Safe for back pain"
        ],
        "avoid": [],
    },
 
    # ============================================================
    # MOBILITY / STRETCH
    # ============================================================
    "Cat Cow Stretch": {
        "name": "Cat Cow Stretch",
        "category": "mobility",
        "image": f"{IMG}/cat_cow.jpg",
        "video": "https://www.youtube.com/results?search_query=cat+cow+stretch",
        "target_muscle": "Spine & Back",
        "difficulty": "Easy",
        "calories": "20 kcal / 10 min",
        "prescription": "2 sets x 10 slow reps",
        "steps": [
            "Start on your hands and knees.",
            "Arch your back up like a cat.",
            "Then dip your back down, lifting your head.",
            "Move slowly with your breath."
        ],
        "benefits": [
            "Relieves back tension",
            "Improves spine mobility",
            "Great for back pain"
        ],
        "avoid": [],
    },
 
    "Standing Hamstring Stretch": {
        "name": "Standing Hamstring Stretch",
        "category": "mobility",
        "image": f"{IMG}/hamstring_stretch.jpg",
        "video": "https://www.youtube.com/results?search_query=standing+hamstring+stretch",
        "target_muscle": "Hamstrings",
        "difficulty": "Easy",
        "calories": "15 kcal / 10 min",
        "prescription": "Hold 30 seconds x 2 each leg",
        "steps": [
            "Stand tall and extend one leg forward, heel down.",
            "Hinge gently at the hips.",
            "Reach toward your toes without rounding your back.",
            "Hold, then switch legs."
        ],
        "benefits": [
            "Improves flexibility",
            "Relieves tight legs",
            "Aids recovery"
        ],
        "avoid": [],
    },
 
    "Child's Pose": {
        "name": "Child's Pose",
        "category": "mobility",
        "image": f"{IMG}/childs_pose.jpg",
        "video": "https://www.youtube.com/results?search_query=childs+pose+stretch",
        "target_muscle": "Back & Hips",
        "difficulty": "Easy",
        "calories": "10 kcal / 10 min",
        "prescription": "Hold 30-60 seconds",
        "steps": [
            "Kneel and sit back on your heels.",
            "Fold forward, extending your arms ahead.",
            "Rest your forehead on the floor.",
            "Breathe and relax."
        ],
        "benefits": [
            "Gently stretches the back",
            "Calming and restorative",
            "Safe for back pain"
        ],
        "avoid": [],
    },
 
    # ============================================================
    # REST
    # ============================================================
    "Rest Day": {
        "name": "Rest Day",
        "category": "rest",
        "image": "",
        "video": "",
        "target_muscle": "Recovery",
        "difficulty": "-",
        "calories": "-",
        "prescription": "Active recovery / full rest",
        "steps": [],
        "benefits": [
            "Allows your body to recover.",
            "Prevents overtraining.",
            "Supports muscle growth."
        ],
        "avoid": [],
    },
}
 
 
def get_exercise(name):
    """Return a copy of one exercise, or a safe empty fallback."""
    return EXERCISE_LIBRARY.get(name, {
        "name": name,
        "category": "",
        "image": "",
        "video": "",
        "target_muscle": "",
        "difficulty": "",
        "calories": "",
        "prescription": "",
        "steps": [],
        "benefits": [],
        "avoid": [],
    })