from pathlib import Path
from typing import Union
from unittest.mock import patch
from todo.todo import app
from todo.helper import load_data_from_file


def key_in_data(location: Path, key: str, value: Union[str, bool] = "item", list: str = "todo") -> bool:
    data = load_data_from_file(location)
    list = data.get(list)
    for i in list:
        if i.get(key) == value:
            return True
    return False


def test_hello(runner):
    result = runner.invoke(app, ["hello"])
    assert result.exit_code == 0
    assert result.stdout.strip() == "Hello world!"


def test_add(test_file, runner):
    with patch("todo.todo.DATA", test_file):
        result = runner.invoke(app, ["add", "potions"])
        assert result.exit_code == 0
        assert result.stdout.strip() == "Added potions to your todo list."
        assert key_in_data(test_file, "item", "potions")
        assert key_in_data(test_file, "done", False)


def test_add_list_option(test_file, runner):
    with patch("todo.todo.DATA", test_file):
        result = runner.invoke(app, ["add", "swords", "--list", "weapons"])
        assert result.exit_code == 0
        assert result.stdout.strip() == "Added swords to your weapons list."
        assert key_in_data(test_file, "item", "swords", "weapons")
        assert key_in_data(test_file, "done", False, "weapons")


def test_add_done_option(test_file, runner):
    with patch("todo.todo.DATA", test_file):
        result = runner.invoke(app, ["add", "food", "--done"])
        assert result.exit_code == 0
        assert result.stdout.strip() == "Added food to your todo list."
        assert key_in_data(test_file, "item", "food")
        assert key_in_data(test_file, "done", True)
