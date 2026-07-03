from pydantic import BaseModel, Field

class BMIRequest(BaseModel):
    age: int = Field(gt=0, lt=120)
    gender: str
    height_cm: float = Field(gt=0, le=300)
    weight_kg: float = Field(gt=0, le=500)
    activity_level: str
    goal: str
    condition: str