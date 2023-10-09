from rich.console import Console
from typer import Typer
from todo.example import app as example_app


console = Console()
app = Typer(name="todo", add_completion=False, no_args_is_help=True, help="TODO is here to help your productivity!")
app.add_typer(example_app, name="example")  # see example and db modules for explanatory comments on typer


@app.command()
def hello():
    """Prints a welcome message."""
    console.print(f"Hello world!")


if __name__ == "__main__":
    app()
