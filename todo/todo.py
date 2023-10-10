from pathlib import Path
from rich.console import Console
from typer import Typer, Argument, Option
from typing_extensions import Annotated
from yaml import safe_load, safe_dump
from todo.example import app as example_app
from todo.helper import create_file_if_not_exists


DATA = Path(__file__).parent.resolve() / "data" / "data.yml" 
create_file_if_not_exists(path=DATA)  # creating here to allow for usage of both cli and main entry

console = Console()
app = Typer(name="todo", add_completion=False, no_args_is_help=True, help="TODO is here to help your productivity!")
app.add_typer(example_app, name="example")  # see example and db modules for explanatory comments on typer


@app.command()
def hello():
    """Prints a welcome message."""
    console.print(f"Hello world!")


@app.command()
def add(item: Annotated[str, Argument(..., help="The todo item to add.")], 
        list: Annotated[str, Option(..., help="The list it needs to be added to.")] = "todo",
        done: Annotated[bool, Option(..., is_flag=True)] = False):
    """Adds an item to the specified list.

    Args:
        item (str): The item to add.
        list (str): List to add the item to. Defaults to "todo".
        done (bool): Flag to mention if item is done. Defaults to False.
    """
    with open(DATA, "r") as f:
        data = safe_load(f)
        if not data.get(list):
            data[list] = []
        todo_list = data.get(list)
        todo_list.append({"item": item, "done": done})
    with open(DATA, "w") as w:
        safe_dump(data, w, sort_keys=False)
    console.print(f"Added {item} to your {list} list.")


if __name__ == "__main__":
    app()
