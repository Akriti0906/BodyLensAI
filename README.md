# 🏋️ BodyLens AI — Your Personal AI Fitness Assistant

BodyLens AI is a production-ready, AI-powered fitness and health web application.
Users get an instant, personalized health analysis — including BMI, calorie and
macro targets, a full weekly workout roadmap, and a diet plan — plus a built-in
AI health assistant they can chat with by text **or voice**.

> Built with FastAPI, vanilla JavaScript, and Google Gemini.

---

## ✨ Features

### 🧠 AI Health Engine
- Instant **BMI** calculation with category (Underweight / Normal / Overweight / Obese)
- Personalized **calorie, protein, and water** targets based on age, gender, activity, and goal
- **Health Score** (out of 100) with a **risk-level** assessment
- **Condition-aware** advice for PCOS, diabetes, knee pain, and back pain

### 🥗 Smart Diet Plans
- Personalized meal plans (breakfast, lunch, dinner) tailored to your goal
- Full macro breakdown per food — calories, protein, carbs, fat — with daily totals

### 💪 Weekly Workout Roadmap
- A realistic **4–8 exercises per day**, 7-day plan
- Selected by goal, and **filtered by medical condition** (e.g. no high-impact moves for knee pain)
- Each exercise includes an image, target muscle, difficulty, calories, sets/reps, steps, and benefits

### 🤖 AI Health Assistant (Chatbot)
- Chat with an AI assistant about diet, workouts, nutrition, and wellness
- **Personalized** — the assistant knows your health report and answers based on your data
- Powered by **Google Gemini**

### 🎙️ Voice Assistant
- Ask questions using your **voice** (speech-to-text)
- The assistant **speaks its answers back** (text-to-speech)

### 📊 Premium Report Page
- Animated statistic cards with count-up numbers
- Circular progress ring for Health Score, progress bars for BMI
- Collapsible diet and workout sections
- **Download the full report as a PDF**

### 🎨 Modern UI/UX
- Premium dark theme with smooth animations and transitions
- Fully **responsive** — desktop, tablet, and mobile
- Clean, icon-rich, professional design

---

## 📸 Screenshots

> _Add your screenshots here._

| Landing Page | Health Report |
|:---:|:---:|
| ![Landing Page](screenshots/landing.png) | ![Report](screenshots/report.png) |

| AI Chatbot | Workout Plan |
|:---:|:---:|
| ![Chatbot](screenshots/chatbot.png) | ![Workout](screenshots/workout.png) |

---

## 🛠️ Tech Stack

**Frontend:** HTML, CSS, JavaScript (vanilla)
**Backend:** Python, FastAPI
**Database:** SQLite (SQLAlchemy)
**AI:** Google Gemini API
**Voice:** Web Speech API (browser-native)

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- A free [Google Gemini API key](https://aistudio.google.com/apikey)

### 1. Clone the repository
```bash
git clone https://github.com/Akriti0906/BodyLensAI.git
cd BodyLensAI
```

### 2. Set up the backend
```bash
cd backend
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS/Linux
pip install -r requirement.txt
```

### 3. Add your API key
Create a file named `.env` inside the `backend/` folder:
GEMINI_API_KEY=
### 4. Run the backend
```bash
uvicorn main:app --reload
```
The API runs at `http://127.0.0.1:8000`

### 5. Run the frontend
Open `frontend/index.html` with a live server (e.g. the VS Code **Live Server** extension).

---

## 📁 Project Structure
---

## ⚠️ Disclaimer

BodyLens AI is for general informational purposes only and is not a substitute
for professional medical advice. Always consult a qualified healthcare provider
before making health, diet, or exercise decisions.

---

## 👤 Author

**Akriti** — [GitHub](https://https://github.com/Akriti0906)