import typer
from commands.user_commands import user_app
from commands.food_commands import food_app
from commands.goals_commands import goals_app
from commands.meals_commands import meals_app
from commands.goals_commands import goals_app

app = typer.Typer()

# Register command groups
app.add_typer(user_app, name="user", help="User creation and listing")
app.add_typer(food_app, name="food", help="Add, update, list, delete food entries")
app.add_typer(goals_app, name="goals", help="Set and view goals")
app.add_typer(meals_app, name="plan-meal", help="Weekly meal planning")

if __name__ == "__main__":
    app()