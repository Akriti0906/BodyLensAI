from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database.database import Base, engine
from database import models

from models.bmi import BMIRequest
from services.health_service import calculate_bmi_and_recommendation

from fastapi import Depends
from sqlalchemy.orm import Session

from database.database import get_db
from database.models import HealthReport


# Create Database Tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="BodyLens AI API",
    version="1.0.0"
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:5500",
        "http://127.0.0.1:5500",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Home Route
@app.get("/")
def home():
    return {
        "message": "Welcome to BodyLens AI 🚀",
        "status": "Server Running Successfully"
    }

# BMI Route
@app.post("/bmi")
def calculate_bmi(data: BMIRequest, db: Session = Depends(get_db)):
    result = calculate_bmi_and_recommendation(
        age=data.age,
        gender=data.gender,
        height_cm=data.height_cm,
        weight_kg=data.weight_kg,
        activity_level=data.activity_level,
        goal=data.goal,
        condition=data.condition
    )
    report = HealthReport(
        age=data.age,
        gender=data.gender,
        height=data.height_cm,
        weight=data.weight_kg,
        bmi=result["bmi"],
        category=result["category"],
        goal=result["goal"],
        condition=result["condition"],
        calories=result["target_calories"],
        protein=result["protein_g"],
        water=result["water_liters"],
    )
    db.add(report)
    db.commit()
    return result