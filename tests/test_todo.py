from typer.testing import CliRunner
from todo import app


runner = CliRunner()


def test_hello_world():
    result = runner.invoke(app, ['hello-world', 'Gerald'])
    assert result.exit_code == 0
    assert result.stdout.strip() == "Hello Gerald!"


def test_goodbye_world():
    result = runner.invoke(app, ['goodbye-world', 'Gerald'])
    assert result.exit_code == 0
    assert result.stdout.strip() == "Goodbye Gerald!"


def test_add():
    result = runner.invoke(app, ['add', '5', '3'])
    assert result.exit_code == 0
    assert result.stdout.strip() == '8'


def test_add_default():
    result = runner.invoke(app, ['add', '5'])
    assert result.exit_code == 0
    assert result.stdout.strip() == '6'
