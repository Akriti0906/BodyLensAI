from database.database import SessionLocal
from database.models import HealthReport


def save_report(data):

    db = SessionLocal()

    report = HealthReport(
        age=data["age"],
        gender=data["gender"],
        height=data["height"],
        weight=data["weight"],
        bmi=data["bmi"],
        category=data["category"],
        goal=data["goal"],
        condition=data["condition"],
        activity_level=data["activity_level"],
        calories=data["calories"],
        protein=data["protein"],
        water=data["water"],
        health_score=data["health_score"],
        risk_level=data["risk_level"]
    )

    db.add(report)
    db.commit()
    db.close()