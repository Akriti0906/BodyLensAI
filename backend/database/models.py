from sqlalchemy import Column, Integer, Float, String
from database.database import Base


class HealthReport(Base):

    __tablename__ = "health_reports"

    id = Column(Integer, primary_key=True, index=True)

    age = Column(Integer)
    gender = Column(String)

    height = Column(Float)
    weight = Column(Float)

    bmi = Column(Float)
    category = Column(String)

    goal = Column(String)
    condition = Column(String)
    activity_level = Column(String)

    calories = Column(Integer)
    protein = Column(Integer)
    water = Column(Float)

    health_score = Column(Integer)
    risk_level = Column(String)