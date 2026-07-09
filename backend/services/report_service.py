from database.database import SessionLocal
from database.models import HealthReport


def save_report(data):

    db = SessionLocal()

    try:
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

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()


def get_all_reports():

    db = SessionLocal()

    try:
        reports = (
            db.query(HealthReport)
            .order_by(HealthReport.id.desc())
            .all()
        )

        return [
            {
                "id": r.id,
                "age": r.age,
                "gender": r.gender,
                "height": r.height,
                "weight": r.weight,
                "bmi": r.bmi,
                "category": r.category,
                "goal": r.goal,
                "condition": r.condition,
                "activity_level": r.activity_level,
                "calories": r.calories,
                "protein": r.protein,
                "water": r.water,
                "health_score": r.health_score,
                "risk_level": r.risk_level
            }
            for r in reports
        ]

    finally:
        db.close()