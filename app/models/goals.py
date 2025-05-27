from sqlalchemy import Column, Integer, ForeignKey
from app.db import Base

class Goal(Base):
    __tablename__ = 'goals'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    daily = Column(Integer)
    weekly = Column(Integer)
