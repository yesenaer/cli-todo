from pathlib import Path
from typing import Union
from pytest import fixture
from typer.testing import CliRunner
from unittest.mock import patch
from yaml import safe_load, safe_dump
from todo.todo import app, create_file_if_not_exists


TEST_DATA = Path(__file__).parent.resolve() / "resources" / "test_data.yml"

runner = CliRunner()


@fixture()
def reset_data():
    yield
    with open(TEST_DATA, "w") as w:
            data = {"todo": []}
            safe_dump(data, w, sort_keys=False)


def key_in_data(key: str, value: Union[str, bool] = "item", list: str = "todo") -> bool:
    with open(TEST_DATA, "r") as f:
        data = safe_load(f)
        list = data.get(list)
        for i in list:
             if i.get(key) == value:
                return True
    return False


def test_create_file_if_not_already_exists():
    assert TEST_DATA.exists()
    assert not create_file_if_not_exists(TEST_DATA)


def test_create_file_if_not_already_exists_created():
    path = Path(__file__).parent.resolve() / "resources" / "non_existing.yml"
    assert not path.exists()
    assert create_file_if_not_exists(path)
    assert path.exists()
    path.unlink()
    assert not path.exists()


def test_hello():
    result = runner.invoke(app, ["hello"])
    assert result.exit_code == 0
    assert result.stdout.strip() == "Hello world!"


@patch("todo.todo.DATA", TEST_DATA)
def test_add(reset_data):
    result = runner.invoke(app, ["add", "potions"])
    assert result.exit_code == 0
    assert result.stdout.strip() == "Added potions to your todo list."
    assert key_in_data("item", "potions")
    assert key_in_data("done", False)


@patch("todo.todo.DATA", TEST_DATA)
def test_add_list_option(reset_data):
    result = runner.invoke(app, ["add", "swords", "--list", "weapons"])
    assert result.exit_code == 0
    assert result.stdout.strip() == "Added swords to your weapons list."
    assert key_in_data("item", "swords", "weapons")
    assert key_in_data("done", False, "weapons")


@patch("todo.todo.DATA", TEST_DATA)
def test_add_done_option(reset_data):
    result = runner.invoke(app, ["add", "food", "--done"])
    assert result.exit_code == 0
    assert result.stdout.strip() == "Added food to your todo list."
    assert key_in_data("item", "food")
    assert key_in_data("done", True)
