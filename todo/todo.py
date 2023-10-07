from typer import Typer, Argument


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


if __name__ == "__main__":
    app()  # runs the typer object as cli
