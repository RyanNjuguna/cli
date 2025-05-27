from sqlalchemy import Column, Integer, String, Date, ForeignKey
from app.db import Base

class FoodEntry(Base):
    __tablename__ = 'food_entries'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    food = Column(String, nullable=False)
    calories = Column(Integer, nullable=False)
    date = Column(Date, nullable=False)
