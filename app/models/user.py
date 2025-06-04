from sqlalchemy import Column, Integer, String
from app.db import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    meal_plans = relationship("MealPlan", back_populates="user")