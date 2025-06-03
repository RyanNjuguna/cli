from sqlalchemy import Column, Integer, String, ForeignKey, Date
from app.db import Base

class Food(Base):

    __tablename__ = 'foods'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    calories = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    date = Column(Date, nullable=False)

    def __repr__(self):
        return f"<Food(name={self.name}, calories={self.calories}, date={self.date})>"
