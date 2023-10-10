from pathlib import Path
from typer.testing import CliRunner
from pytest import fixture


@fixture()
def test_data():
    return Path(__file__).parent.resolve() / "resources" / "test_data.yml"


@fixture()
def runner():
    return CliRunner()
