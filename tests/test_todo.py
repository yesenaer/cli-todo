from typer import Exit
from typer.testing import CliRunner
from todo import app, check_if_files_exist
from pathlib import Path
from pytest import raises
from unittest import mock


runner = CliRunner()


def test_hello_world():
    result = runner.invoke(app, ["hello-world", "Gerald"])
    assert result.exit_code == 0
    assert result.stdout.strip() == "Hello Gerald!"


def test_goodbye_world():
    result = runner.invoke(app, ["goodbye-world", "Gerald"])
    assert result.exit_code == 0
    assert result.stdout.strip() == "Goodbye Gerald!"


def test_add():
    result = runner.invoke(app, ["add", "5", "3"])
    assert result.exit_code == 0
    assert result.stdout.strip() == "8"


def test_add_default():
    result = runner.invoke(app, ["add", "5"])
    assert result.exit_code == 0
    assert result.stdout.strip() == "6"


def test_check_if_files_exist():
    filename = Path(__file__)
    existing_paths = [filename]
    result = check_if_files_exist(existing_paths)
    assert result == existing_paths


def test_check_if_files_exist_failure():
    with raises(Exit):
        filename = Path("nonexistingfile")
        check_if_files_exist([filename])


def test_word_count():
    test_file = str((Path(__file__).resolve().parent / "resources/test.txt"))
    result = runner.invoke(app, ["word-count", test_file])
    assert result.exit_code == 0
    assert "In total there are 4 words in" in result.stdout.strip()


def test_word_count_failure():
    test_file = str(Path("nonexistingfile"))
    result = runner.invoke(app, ["word-count", test_file])
    assert result.exit_code == 1
    assert result.stdout.strip() == "The path 'nonexistingfile' that you supplied, does not exist."


def test_talk():
    result = runner.invoke(app, ["talk", "hello world", "--repeat", "2", "--loud"])
    assert result.stdout.strip() == "HELLO WORLD\nHELLO WORLD" 


def test_talk_defaults():
    result = runner.invoke(app, ["talk", "hello world"])
    assert result.stdout.strip() == "hello world" 


def test_create_db():
    result = runner.invoke(app, ["create-db", "--table", "gwent"])
    assert result.stdout.strip() == "Creating table 'gwent' in database." 


def test_create_db_prompt():
    result = runner.invoke(app, ["create-db"], input="gwent\ngwent\n")
    assert result.stdout.strip() == "What is the name of the table?: gwent\n" \
                                    "Repeat for confirmation: gwent\n" \
                                    "Creating table 'gwent' in database." 


def test_delete_db():
    result = runner.invoke(app, ["delete-db", "--table", "gwent"], input="y\n")
    assert result.stdout.strip() == "Are you really really sure? [y/N]: y\n" \
                                    "Deleting table 'gwent' in database." 
    

def test_delete_db_confirm_n():
    result = runner.invoke(app, ["delete-db", "--table", "gwent"], input="N\n")
    assert result.stdout.strip() == "Are you really really sure? [y/N]: N\n" \
                                    "Back to safety!" 
    

def test_delete_db_prompt():
    result = runner.invoke(app, ["delete-db"], input="gwent\ngwent\ny\n")
    assert result.stdout.strip() == "What is the name of the table?: gwent\n" \
                                    "Repeat for confirmation: gwent\n" \
                                    "Are you really really sure? [y/N]: y\n" \
                                    "Deleting table 'gwent' in database." 
