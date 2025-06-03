import typer
from app.models.goals import Goal
from app.models.user import User
from app.db import SessionLocal

app = typer.Typer()

@app.command()
def set(user: str, daily: int, weekly: int):
    """Set daily and weekly calorie goals for a user"""
    db = SessionLocal()
    user_obj = db.query(User).filter(User.name == user).first()
    if not user_obj:
        typer.echo(f"User '{user}' not found")
        raise typer.Exit(code=1)

    goal = db.query(Goal).filter(Goal.user_id == user_obj.id).first()
    if not goal:
        goal = Goal(user_id=user_obj.id, daily_calories=daily, weekly_calories=weekly)
        db.add(goal)
    else:
        goal.daily_calories = daily
        goal.weekly_calories = weekly
    db.commit()
    typer.echo(f"Set goals for {user}: daily={daily}, weekly={weekly}")
    db.close()

@app.command()
def list(user: str):
    """List goals for a user"""
    db = SessionLocal()
    user_obj = db.query(User).filter(User.name == user).first()
    if not user_obj:
        typer.echo(f"User '{user}' not found")
        raise typer.Exit(code=1)
    goal = db.query(Goal).filter(Goal.user_id == user_obj.id).first()
    if goal:
        typer.echo(f"Goals for {user}: daily={goal.daily_calories}, weekly={goal.weekly_calories}")
    else:
        typer.echo(f"No goals set for {user}")
    db.close()
