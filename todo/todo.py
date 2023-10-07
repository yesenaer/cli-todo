import typer


def hello_world(name: str):
    """Prints a welcome message.

    Args:
        name (str): your name!
    """
    print(f'Hello {name}!')


if __name__ == "__main__":
    typer.run(hello_world)
