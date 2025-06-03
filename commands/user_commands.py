import typer
from app.db import SessionLocal
from app.models.user import User

user_app = typer.Typer()

@user_app.command()
def add(name: str):
    """Add a new user"""
    db = SessionLocal()
    user = User(name=name)
    db.add(user)
    db.commit()
    typer.echo(f"User '{name}' created.")
    db.close()

@user_app.command("list")
def list_users():
    session = SessionLocal()
    users = session.query(User).all()
    for user in users:
        typer.echo(f"{user.id}: {user.name}")
    session.close()