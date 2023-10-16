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


def test_show(test_file, runner):
    with patch("todo.todo.DATA", test_file):
        runner.invoke(app, ["add", "potions"])
        runner.invoke(app, ["add", "swords", "--done"])
        result = runner.invoke(app, ["show"])
        assert result.exit_code == 0
        output = result.stdout.split("\n")
        assert output[0] == "todo:"
        assert output[1] == "  | potions"
        assert output[2] == "x | swords"


def test_show_all(test_file, runner):
    with patch("todo.todo.DATA", test_file):
        runner.invoke(app, ["add", "potions"])
        runner.invoke(app, ["add", "swords", "--done", "--list", "weapons"])
        result = runner.invoke(app, ["show", "--all"])
        assert result.exit_code == 0
        output = result.stdout.split("\n")
        assert output[0] == "todo:"
        assert output[1] == "  | potions"
        assert output[2] == ""
        assert output[3] == "weapons:"
        assert output[4] == "x | swords"


def test_remove(test_file, runner):
    with patch("todo.todo.DATA", test_file):
        runner.invoke(app, ["add", "swords"])
        assert key_in_data(test_file, "item", "swords")
        assert key_in_data(test_file, "done", False)

        runner.invoke(app, ["remove", "swords"])
        assert not key_in_data(test_file, "item", "swords")
        
        
def test_remove_list_option(test_file, runner):
    with patch("todo.todo.DATA", test_file):
        runner.invoke(app, ["add", "swords", "--list", "weapons"])
        assert key_in_data(test_file, "item", "swords", "weapons")
        assert key_in_data(test_file, "done", False, "weapons")

        runner.invoke(app, ["remove", "swords", "--list", "weapons"])
        assert not key_in_data(test_file, "item", "swords", "weapons")


def test_remove_failed(test_file, runner):
    with patch("todo.todo.DATA", test_file):
        result = runner.invoke(app, ["remove", "swords"])
        assert result.stdout.strip() == "List todo does not exist."
