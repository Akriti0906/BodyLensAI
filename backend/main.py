from services.chat_service import get_chat_response
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database.database import Base, engine
from database import models

from models.bmi import BMIRequest
from services.health_service import calculate_bmi_and_recommendation
from services.report_service import get_all_reports

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
# History Route
@app.get("/reports")
def read_reports():
    return get_all_reports()


# BMI Route
@app.post("/bmi")
def calculate_bmi(data: BMIRequest):
    return calculate_bmi_and_recommendation(
        age=data.age,
        gender=data.gender,
        height_cm=data.height_cm,
        weight_kg=data.weight_kg,
        activity_level=data.activity_level,
        goal=data.goal,
        condition=data.condition
    )
from pydantic import BaseModel

class ChatRequest(BaseModel):
    message: str

# Chatbot Route

from typing import Optional

class ChatRequest(BaseModel):
    message: str
    profile: Optional[dict] = None

# Chatbot Route
@app.post("/chat")
def chat(data: ChatRequest):
    return get_chat_response(data.message, data.profile)