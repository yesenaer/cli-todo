from pathlib import Path
from rich.console import Console
from typer import Typer, Argument, Option
from typing_extensions import Annotated
from todo.example import app as example_app
from todo.helper import (create_file_if_not_exists, write_data_to_file, load_data_from_file, remove_item_from_list, 
                         update_item_in_list)


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
    data = load_data_from_file(DATA)
    if not data.get(list):
        data[list] = []
    todo_list = data.get(list)
    todo_list.append({"item": item, "done": done})
    write_data_to_file(data, DATA)
    console.print(f"Added {item} to your {list} list.")


@app.command()
def show(list: Annotated[str, Option(..., help="The list of interest.")] = "todo",
         all: Annotated[bool, Option(..., is_flag=True)] = False):
    """Shows items in list or shows items of all lists.

    Args:
        list (str): The name of list of interest. Defaults to "todo".
        all (bool): Flag to have all lists shown. Defaults to False.
    """
    data = load_data_from_file(DATA)
    if all:
        for x in data:
            show_list(x, data)
            console.print()  
    else:
        if not data.get(list):
            console.print(f"{list=} does not exist in data.")
            return
        show_list(list, data)


def show_list(name: str, data: dict):
    """Shows all items on list if list exists in data.

    Args:
        name (str): the name of the list.
        data (dict): data that contains the list.
    """
    console.print(f"{name}:")
    for item in data.get(name):
        done = ['x' if item.get("done") else ' ']
        console.print(f"{done[0]} | {item.get('item')}")


@app.command()
def remove(item: Annotated[str, Argument(..., help="The todo item to remove.")], 
           list: Annotated[str, Option(..., help="The list it needs to be removed from.")] = "todo"):
    """Removes an item from the specified list.

    Args:
        item (str): The todo item to remove.
        list (str): The list it needs to be removed from. Defaults to "todo".
    """
    data = load_data_from_file(DATA)
    if not data.get(list):
        console.print(f"List {list} does not exist.")
        return
    updated_data = remove_item_from_list(data, item, list)
    write_data_to_file(updated_data, DATA)
    console.print(f"Removed {item} from your {list} list.")


@app.command()
def complete(item: Annotated[str, Argument(..., help="The todo item to complete.")], 
             list: Annotated[str, Option(..., help="The list it needs to be completed on.")] = "todo",
             undo: Annotated[bool, Option(..., is_flag=True)] = False):
    """Removes an item from the specified list.

    Args:
        item (str): The todo item to complete.
        list (str): The list it needs to be completed on. Defaults to "todo".
        undo (bool): Undo done status of item. Defaults to False.
    """
    data = load_data_from_file(DATA)
    if not data.get(list):
        console.print(f"List {list} does not exist.")
        return
    done = not undo
    updated_data = update_item_in_list(data, item, done, list)
    write_data_to_file(updated_data, DATA)
    console.print(f"Changed {item} done status on your {list} list.")


if __name__ == "__main__":
    app()
