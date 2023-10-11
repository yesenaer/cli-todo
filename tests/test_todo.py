from pathlib import Path
from typing import Union
from pytest import fixture
from unittest.mock import patch
from yaml import safe_load, safe_dump
from todo.todo import app

@fixture()
def reset_data(test_file):
    yield
    with open(test_file, "w") as w:
        data = {"todo": []}
        safe_dump(data, w, sort_keys=False)


def key_in_data(location: Path, key: str, value: Union[str, bool] = "item", list: str = "todo") -> bool:
    with open(location, "r") as f:
        data = safe_load(f)
        list = data.get(list)
        for i in list:
            if i.get(key) == value:
                return True
    return False


def test_hello(runner):
    result = runner.invoke(app, ["hello"])
    assert result.exit_code == 0
    assert result.stdout.strip() == "Hello world!"


def test_add(reset_data, test_file, runner):
    with patch("todo.todo.DATA", test_file):
        result = runner.invoke(app, ["add", "potions"])
        assert result.exit_code == 0
        assert result.stdout.strip() == "Added potions to your todo list."
        assert key_in_data(test_file, "item", "potions")
        assert key_in_data(test_file, "done", False)


def test_add_list_option(reset_data, test_file, runner):
    with patch("todo.todo.DATA", test_file):
        result = runner.invoke(app, ["add", "swords", "--list", "weapons"])
        assert result.exit_code == 0
        assert result.stdout.strip() == "Added swords to your weapons list."
        assert key_in_data(test_file, "item", "swords", "weapons")
        assert key_in_data(test_file, "done", False, "weapons")


def test_add_done_option(reset_data, test_file, runner):
    with patch("todo.todo.DATA", test_file):
        result = runner.invoke(app, ["add", "food", "--done"])
        assert result.exit_code == 0
        assert result.stdout.strip() == "Added food to your todo list."
        assert key_in_data(test_file, "item", "food")
        assert key_in_data(test_file, "done", True)
