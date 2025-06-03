import typer
from datetime import date
session = SessionLocal()
from app.models.user import User
from app.models.mealplan import MealPlan
from app.db import SessionLocal

meals_app = typer.Typer()

@meals_app.command("add")
def add_plan(user: str, week: int, description: str):
    user_obj = session.query(User).filter_by(name=user).first()
    if not user_obj:
        typer.echo("User not found.")
        raise typer.Exit()

    plan = MealPlan(user_id=user_obj.id, week=week, description=description, date_created=date.today())
    session.add(plan)
    session.commit()
    typer.echo(f"Meal plan added for week {week}.")

@meals_app.command("update")
def update_plan(id: int, description: str):
    plan = session.query(MealPlan).filter_by(id=id).first()
    if not plan:
        typer.echo("Meal plan not found.")
        raise typer.Exit()

    plan.description = description
    session.commit()
    typer.echo(f"Meal plan {id} updated.")

@meals_app.command("list")
def list_plans(user: str = None):
    if user:
        user_obj = session.query(User).filter_by(name=user).first()
        if not user_obj:
            typer.echo("User not found.")
            raise typer.Exit()
        plans = session.query(MealPlan).filter_by(user_id=user_obj.id).all()
    else:
        plans = session.query(MealPlan).all()

    for plan in plans:
        typer.echo(f"ID: {plan.id}, Week: {plan.week}, Description: {plan.description}")
