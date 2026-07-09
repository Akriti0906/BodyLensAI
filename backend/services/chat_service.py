import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

SYSTEM_PROMPT = """You are BodyLens AI's friendly health and fitness assistant.
You help users with questions about BMI, diet, nutrition, workouts, calories,
protein, hydration, and general fitness and wellness.

Guidelines:
- Give clear, concise, practical answers.
- Be encouraging and supportive.
- If the user's health profile is provided below, personalize your answer to it
  (use their BMI, goal, calories, weight, condition, etc.).
- If asked about serious medical issues, gently suggest consulting a doctor.
- Stay focused on health, fitness, diet, and wellness topics.
- Keep answers short (2-4 sentences) unless the user asks for detail.
"""


def _build_context(profile):
    """Turn the user's report dict into a readable context block for Gemini."""
    if not profile:
        return "No health profile available yet. Answer generally."

    lines = ["The user's current health profile:"]
    mapping = {
        "bmi": "BMI",
        "category": "BMI category",
        "goal": "Goal",
        "condition": "Health condition",
        "target_calories": "Daily calorie target",
        "protein_g": "Daily protein target (g)",
        "water_liters": "Daily water target (L)",
        "health_score": "Health score (out of 100)",
        "risk_level": "Risk level",
        "workout_type": "Workout type",
    }
    for key, label in mapping.items():
        val = profile.get(key)
        if val is not None and val != "":
            lines.append(f"- {label}: {val}")
    return "\n".join(lines)


def get_chat_response(user_message, profile=None):
    """Send the user's message (plus optional health profile) to Gemini."""
    try:
        context = _build_context(profile)
        prompt = (
            f"{SYSTEM_PROMPT}\n\n"
            f"{context}\n\n"
            f"User question: {user_message}"
        )
        response = model.generate_content(prompt)
        return {"reply": response.text.strip()}

    except Exception as e:
        print(f"[chat_service] Error: {e}")
        return {
            "reply": "Sorry, I'm having trouble responding right now. Please try again in a moment."
        }