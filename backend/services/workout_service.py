import random
 
from services.exercise_service import get_exercise_details  # kept for backward compatibility
from services.exercise_library import EXERCISE_LIBRARY
 
 
DAYS = ["monday", "tuesday", "wednesday", "thursday",
        "friday", "saturday", "sunday"]
 
 
# Each day = (focus label, [ordered list of categories to fill]).
# Category counts are tuned so every training day lands in the 4-8 range.
DAY_TEMPLATES = {
 
    "lose_weight": [
        ("Full Body Cardio",    ["cardio", "cardio", "legs", "core", "mobility"]),
        ("Lower Body + Core",   ["legs", "legs", "core", "cardio", "mobility"]),
        ("Upper Body Burn",     ["upper", "upper", "core", "cardio", "mobility"]),
        ("Active Cardio",       ["cardio", "low_impact", "legs", "core", "mobility"]),
        ("HIIT Style",          ["cardio", "legs", "upper", "core", "cardio", "mobility"]),
        ("Full Body Strength",  ["legs", "upper", "core", "cardio", "mobility"]),
        ("Rest Day",            ["rest"]),
    ],
 
    "gain_weight": [
        ("Upper Body Strength", ["upper", "upper", "core", "mobility"]),
        ("Lower Body Strength", ["legs", "legs", "legs", "core", "mobility"]),
        ("Push Focus",          ["upper", "upper", "core", "mobility"]),
        ("Core & Stability",    ["core", "core", "legs", "mobility"]),
        ("Full Body Power",     ["legs", "upper", "core", "upper", "mobility"]),
        ("Leg Day",             ["legs", "legs", "core", "mobility"]),
        ("Rest Day",            ["rest"]),
    ],
 
    "maintain_weight": [
        ("Balanced Full Body",  ["cardio", "legs", "upper", "core", "mobility"]),
        ("Mobility & Core",     ["mobility", "core", "core", "low_impact"]),
        ("Light Cardio",        ["low_impact", "cardio", "legs", "mobility"]),
        ("Strength Basics",     ["legs", "upper", "core", "mobility"]),
        ("Active Recovery",     ["low_impact", "mobility", "mobility", "core"]),
        ("Full Body Tone",      ["cardio", "legs", "upper", "core", "mobility"]),
        ("Rest Day",            ["rest"]),
    ],
}
 
 
def _pool(category, condition):
    """All library exercises in a category that are safe for the condition."""
    cond = (condition or "none").lower()
    result = []
    for ex in EXERCISE_LIBRARY.values():
        if ex["category"] != category:
            continue
        if cond != "none" and cond in ex.get("avoid", []):
            continue
        result.append(ex)
    return result
 
 
def generate_workout_plan(goal, condition="none"):
    """
    Build a weekly plan where each training day holds 4-8 exercises,
    selected by goal and filtered by medical condition.
 
    Returns:
        {
          "monday": {"focus": "...", "exercises": [ {exercise dict}, ... ]},
          ...
          "sunday": {"focus": "Rest Day", "exercises": [ {rest dict} ]}
        }
    """
    goal = (goal or "maintain_weight").lower()
    if goal not in DAY_TEMPLATES:
        goal = "maintain_weight"
 
    templates = DAY_TEMPLATES[goal]
    rng = random.Random()  # fresh variety each request
    plan = {}
 
    for i, day in enumerate(DAYS):
        focus, categories = templates[i]
 
        if categories == ["rest"]:
            plan[day] = {
                "focus": "Rest Day",
                "exercises": [dict(EXERCISE_LIBRARY["Rest Day"])],
            }
            continue
 
        chosen = []
        used = set()
 
        for cat in categories:
            # only exercises in this category not already used today
            pool = [e for e in _pool(cat, condition) if e["name"] not in used]
            if not pool:
                continue  # category exhausted for today; skip (backfill covers the count)
            ex = rng.choice(pool)
            used.add(ex["name"])
            chosen.append(dict(ex))
 
        # Backfill: condition filtering can thin a day out. Guarantee at least
        # 4 exercises by pulling more safe, unused exercises from any category.
        if len(chosen) < 4:
            backfill = [
                e for e in EXERCISE_LIBRARY.values()
                if e["category"] != "rest"
                and e["name"] not in used
                and (condition or "none").lower() not in e.get("avoid", [])
            ]
            rng.shuffle(backfill)
            for ex in backfill:
                if len(chosen) >= 4:
                    break
                used.add(ex["name"])
                chosen.append(dict(ex))
 
        plan[day] = {
            "focus": focus,
            "exercises": chosen,
        }
 
    return plan
 