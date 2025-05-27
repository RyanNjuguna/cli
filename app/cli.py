import typer
from app.db import init_db

app = typer.Typer()

@app.command()
def init():
    """Initialize the database and create tables."""
    init_db()
    typer.echo("Database initialized.")