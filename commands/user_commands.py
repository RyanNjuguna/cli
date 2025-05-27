import typer
from app.db import SessionLocal
from app.models.user import User

user_app = typer.Typer()

@user_app.command("create")
def create_user(name: str):
    session = SessionLocal()
    user = User(name=name)
    session.add(user)
    session.commit()
    session.close()
    typer.echo(f"User '{name}' created!")

@user_app.command("list")
def list_users():
    session = SessionLocal()
    users = session.query(User).all()
    for user in users:
        typer.echo(f"{user.id}: {user.name}")
    session.close()