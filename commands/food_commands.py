import typer
from app.models.food import Food
from app.db import SessionLocal
from app.models.user import User
import datetime



food_app = typer.Typer()

@food_app.command()
def add(name: str, calories: int, username: str):
    """Add a new food for a user"""
    db = SessionLocal()
    user = db.query(User).filter_by(name=username).first()
    if not user:
        typer.echo(f"User '{username}' not found.")
        db.close()
        raise typer.Exit(code=1)
    food = Food(name=name, calories=calories, user_id=user.id, date=datetime.date.today())
    db.add(food)
    db.commit()
    typer.echo(f"Food '{name}' with {calories} calories added for user '{username}'.")
    db.close()

@food_app.command()
def update(food_id: int, name: str = None, calories: int = None):
    """Update a food's name and/or calories by its ID"""
    db = SessionLocal()
    food = db.query(Food).filter_by(id=food_id).first()
    if not food:
        typer.echo(f"Food with ID {food_id} not found.")
        db.close()
        raise typer.Exit(code=1)
    if name is not None:
        food.name = name
    if calories is not None:
        food.calories = calories
    db.commit()
    typer.echo(f"Food with ID {food_id} updated.")
    db.close()

@food_app.command()
def delete(food_id: int):
    """Delete a food by its ID"""
    db = SessionLocal()
    food = db.query(Food).filter_by(id=food_id).first()
    if not food:
        typer.echo(f"Food with ID {food_id} not found.")
        db.close()
        raise typer.Exit(code=1)
    db.delete(food)
    db.commit()
    typer.echo(f"Food with ID {food_id} deleted.")
    db.close()

@food_app.command("list-user")
def list_foods_for_user(username: str):
    """List all foods for a specific user"""
    db = SessionLocal()
    user = db.query(User).filter_by(name=username).first()
    if not user:
        typer.echo(f"User '{username}' not found.")
        db.close()
        raise typer.Exit(code=1)
    foods = db.query(Food).filter_by(user_id=user.id).all()
    if not foods:
        typer.echo(f"No foods found for user '{username}'.")
    else:
        for f in foods:
            typer.echo(f"{f.id}: {f.name} - {f.calories} cal")
    db.close()