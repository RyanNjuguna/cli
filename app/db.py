from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base  # Base is your declarative base in models.py

DATABASE_URL = "sqlite:///health_simplified.db"

engine = create_engine(DATABASE_URL, echo=True, future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

def init_db():
    """Create all tables in the database."""
    Base.metadata.create_all(bind=engine)