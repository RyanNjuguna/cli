import typer
from app.models.goals import Goal
from app.models.user import User
from app.db import SessionLocal

goals_app = typer.Typer()

@goals_app.command()
def set(user: str, daily: int, weekly: int):
    """Set daily and weekly calorie goals for a user"""
    db = SessionLocal()
    user_obj = db.query(User).filter(User.name == user).first()
    if not user_obj:
        typer.echo(f"User '{user}' not found")
        raise typer.Exit(code=1)

    goal = db.query(Goal).filter(Goal.user_id == user_obj.id).first()
    if not goal:
        goal = Goal(user_id=user_obj.id, daily=daily, weekly=weekly)
        db.add(goal)
    else:
        goal.daily_calories = daily
        goal.weekly_calories = weekly
    db.commit()
    typer.echo(f"Set goals for {user}: daily={daily}, weekly={weekly}")
    db.close()

@goals_app.command("list")
def list(user: str):
    """List goals for a user"""
    db = SessionLocal()
    user_obj = db.query(User).filter(User.name == user).first()
    if not user_obj:
        typer.echo(f"User '{user}' not found")
        raise typer.Exit(code=1)
    goal = db.query(Goal).filter(Goal.user_id == user_obj.id).first()
    if goal:
        typer.echo(f"Goals for {user}: daily={goal.daily}, weekly={goal.weekly}")
    else:
        typer.echo(f"No goals set for {user}")
    db.close()
