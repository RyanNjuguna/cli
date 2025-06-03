import typer
from datetime import date
from app.models.meals import Meal
from app.models.user import User
from app.models.food import Food
from app.db import SessionLocal

meals_app = typer.Typer()

@meals_app.command()
def add(user: str, food: str, calories: int, date_str: str):
    """Add a meal entry"""
    db = SessionLocal()
    user_obj = db.query(User).filter(User.name == user).first()
    if not user_obj:
        typer.echo(f"User '{user}' not found")
        raise typer.Exit(code=1)
    meal = Meal(user_id=user_obj.id, food=food, calories=calories, date=date.fromisoformat(date_str))
    db.add(meal)
    db.commit()
    typer.echo(f"Added meal entry for {user} on {date_str}")
    db.close()

@meals_app.command()
def list(user: str = None, date_str: str = None):
    """List meal entries optionally filtered by user or date"""
    db = SessionLocal()
    query = db.query(Meal)
    if user:
        user_obj = db.query(User).filter(User.name == user).first()
        if not user_obj:
            typer.echo(f"User '{user}' not found")
            raise typer.Exit(code=1)
        query = query.filter(Meal.user_id == user_obj.id)
    if date_str:
        query = query.filter(Meal.date == date.fromisoformat(date_str))
    entries = query.all()
    for e in entries:
        typer.echo(f"{e.id}: {e.food} - {e.calories} cal on {e.date}")
    db.close()
