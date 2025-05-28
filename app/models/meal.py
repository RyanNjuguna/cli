from sqlalchemy import Column, Integer, String, ForeignKey
from app.db import Base

class MealPlan(Base):
    __tablename__ = 'meal_plans'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    week = Column(Integer, nullable=False)
    meals = Column(String, nullable=False)  
