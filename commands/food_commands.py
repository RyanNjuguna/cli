import typer
from app.models.food import Food
from app.db import SessionLocal

app = typer.Typer()

@app.command()
def add(name: str, calories: int):
    """Add a new food"""
    db = SessionLocal()
    food = Food(name=name, calories=calories)
    db.add(food)
    db.commit()
    typer.echo(f"Food '{name}' with {calories} calories added.")
    db.close()

@app.command()
def list():
    """List all foods"""
    db = SessionLocal()
    foods = db.query(Food).all()
    for f in foods:
        typer.echo(f"{f.id}: {f.name} - {f.calories} cal")
    db.close()
