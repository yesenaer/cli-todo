from rich.console import Console
from typer import Typer, Option, confirm
from typing_extensions import Annotated


console = Console()
app = Typer(name="db", add_completion=False, no_args_is_help=True, help="Database commands.")


@app.command()
def create_db(table: Annotated[str, Option(..., prompt="What is the name of the table?",  # prompting if not supplied
                                  confirmation_prompt=True)]):  # prompting again
    """Creates a table in database.

    Args:
        table (str, optional): Name of table that needs to be created. Prompts if not given.
    """
    console.print(f"Creating table '{table}' in database.", style="green")


@app.command()
def delete_db(table: Annotated[str, Option(..., prompt="What is the name of the table?", confirmation_prompt=True)]):
    """Deletes a table from database.

    Args:
        table (str, optional): Name of table that needs to be deleted. Prompts if not given.
    """
    sure = confirm("Are you really really sure?")  # typer confirm will ask a y/N confirmation
    if sure:
        console.print(f"Deleting table '{table}' in database.", style="red")
    else:
        console.print("Back to safety!", style="green")
