from typer.testing import CliRunner
from todo.todo import app


runner = CliRunner()


def test_hello():
    result = runner.invoke(app, ["hello"])
    assert result.exit_code == 0
    assert result.stdout.strip() == "Hello world!"
