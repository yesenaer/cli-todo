from pathlib import Path
from typer.testing import CliRunner
from yaml import safe_dump
from pytest import fixture


@fixture()
def resource_dir():
    return Path(__file__).parent.resolve() / "resources"


@fixture()
def test_file(resource_dir):
    return resource_dir / "test_data.yml"


@fixture()
def runner():
    return CliRunner()


@fixture(autouse=True)
def reset_data(test_file):
    yield
    with open(test_file, "w") as w:
        data = {"todo": []}
        safe_dump(data, w, sort_keys=False)
