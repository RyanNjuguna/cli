from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.db import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    entries = relationship("FoodEntry", back_populates="user")
    goals = relationship("Goal", back_populates="user")
    meal_plans = relationship("MealPlan", back_populates="user")

class FoodEntry(Base):
    __tablename__ = 'food_entries'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    food = Column(String, nullable=False)
    calories = Column(Integer, nullable=False)
    date = Column(Date, nullable=False)
    user = relationship("User", back_populates="entries")

class Goal(Base):
    __tablename__ = 'goals'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    daily = Column(Integer)
    weekly = Column(Integer)
    user = relationship("User", back_populates="goals")

class MealPlan(Base):
    __tablename__ = 'meal_plans'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    week = Column(Integer)
    plan = Column(String)  # JSON string or comma-separated meals
    user = relationship("User", back_populates="meal_plans")
