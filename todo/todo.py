from pathlib import Path
from rich.console import Console
from typer import Typer, Argument, Option, Exit, confirm
from typing_extensions import Annotated  # to be able to let interpreter know how to treat values 
from todo.db import app as db_app

# Rich Console object to allow for more console related features
console = Console()
# Typer object that will keep all cli options and other details
app = Typer(name="TODO", add_completion=False, no_args_is_help=True, help="CLI TODO is here to help your productivity!")
app.add_typer(db_app, name="db")  # adding submodule 


@app.command()  # this app.command() will make the function available as cli
def hello_world(name: str):  # underscores ('_') in function names will be replaced with dash ('-') in cli
    """Prints a welcome message.

    Args:
        name (str): your name!
    """
    console.print(f"Hello {name}!")


@app.command()
def goodbye_world(name: str):
    """Prints a goodbye message.

    Args:
        name (str): your name!
    """
    console.print(f"Goodbye {name}!")


@app.command()
def add(n1: Annotated[int, Argument(..., help="An Integer")],  # typer has the elipse (...) showing that its required
        n2: Annotated[int, Argument(..., help="An Integer")] = 1):  # adding a value instead will allow for defaulting
    """Adds two numbers.

    Args:
        n1 (int): first number.
        n2 (int): second number. defaults to 1.
    """
    console.print(n1 + n2)


def check_if_files_exist(paths: list[Path]):
    """Checks for each filepath in list if it exists. 

    Args:
        paths (list[Path]): List of filepaths to be validated.

    Raises:
        Exit: 1 if one of the supplied paths does not exist.

    Returns:
        list[Path]: validated list of filepaths.
    """
    for path in paths:
        if not path.exists():
            console.print(f"The path '{path}' that you supplied, does not exist.", style="red")  # rich style
            raise Exit(code=1)
    return paths


@app.command()
def word_count(paths: Annotated[list[Path], Argument(..., help="List of files to count the words in.", 
                                                     callback=check_if_files_exist)]):
    """Count words per file.

    Args:
        paths (list[Path]): List of filepaths to to count the words in.
    """
    for path in paths:
        texts = path.read_text().split("\n")
        word_count = len([word for text in texts for word in text.split(" ")])
        console.print(f"In total there are {word_count} words in {path}.")


@app.command()
def talk(text: Annotated[str, Argument(..., help="The text to type.")],
         repeat: Annotated[int, Option(..., help="Number of times to repeat.")] = 1,  # not mandatory, can be mixed
         loud: Annotated[bool, Option(..., is_flag=True)] = False):  # adding is_flag means no value needs to be passed
    """Talks back to you based on your specified text and options.

    Args:
        text (str): The text to type.
        repeat (int, optional): Number of times to repeat. Defaults to 1.
        loud (bool, optional): If text needs to be in caps. Defaults to False.
    """
    if loud: 
        text = text.upper()
    for _ in range(repeat):
        console.print(text)


if __name__ == "__main__":
    app()  # runs the typer object as cli
