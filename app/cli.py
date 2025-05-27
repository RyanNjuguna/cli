import typer
from app.db import init_db, SessionLocal
from app.models import User, FoodEntry
from datetime import date

app = typer.Typer()

@app.command()
def init():
    """Initialize the database."""
    init_db()
    typer.echo("Database initialized.")

@app.command()
def user_create(name: str):
    """Create a new user."""
    db = SessionLocal()
    user = User(name=name)
    db.add(user)
    db.commit()
    db.refresh(user)
    typer.echo(f"User {user.name} created with ID {user.id}")
    db.close()

@app.command()
def user_list():
    """List all users."""
    db = SessionLocal()
    users = db.query(User).all()
    for user in users:
        typer.echo(f"{user.id}: {user.name}")
    db.close()