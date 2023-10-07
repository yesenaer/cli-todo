from pathlib import Path
from typer import Typer, Argument, Exit


# Typer object that will keep all cli options and other details
app = Typer(name="TODO", add_completion=False, no_args_is_help=True, help="CLI TODO is here to help your productivity!")


@app.command()  # this app.command() will make the function available as cli
def hello_world(name: str):  # underscores ('_') in function names will be replaced with dash ('-') in cli
    """Prints a welcome message.

    Args:
        name (str): your name!
    """
    print(f'Hello {name}!')


@app.command()
def goodbye_world(name: str):
    """Prints a goodbye message.

    Args:
        name (str): your name!
    """
    print(f'Goodbye {name}!')


@app.command()
def add(n1: int = Argument(..., help='An Integer'),  # typer has the elipse (...) as showing that it requires a value
        n2: int = Argument(1, help='An Integer')):  # adding a value instead will allow for defaulting
    """Adds two numbers.

    Args:
        n1 (int): first number.
        n2 (int): second number. defaults to 1.
    """
    print(n1 + n2)


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
            print(f'The path you\'ve supplied {path} does not exist.')
            raise Exit(code=1)
    return paths


@app.command()
def word_count(paths: list[Path] = Argument(..., help="List of files to count the words in.", 
                                            callback=check_if_files_exist)):
    """Count words per file.

    Args:
        paths (list[Path]): List of filepaths to to count the words in.
    """
    for path in paths:
        texts = path.read_text().split('\n')
        word_count = len([word for text in texts for word in text.split(" ")])
        print(f'In total there are {word_count} words in {path}.')


if __name__ == "__main__":
    app()  # runs the typer object as cli
