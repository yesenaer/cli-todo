from typer import Exit
from example import app, check_if_files_exist
from pathlib import Path
from pytest import raises


def test_hello_world(runner):
    result = runner.invoke(app, ["hello-world", "Gerald"])
    assert result.exit_code == 0
    assert result.stdout.strip() == "Hello Gerald!"


def test_goodbye_world(runner):
    result = runner.invoke(app, ["goodbye-world", "Gerald"])
    assert result.exit_code == 0
    assert result.stdout.strip() == "Goodbye Gerald!"


def test_add(runner):
    result = runner.invoke(app, ["add", "5", "3"])
    assert result.exit_code == 0
    assert result.stdout.strip() == "8"


def test_add_default(runner):
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


def test_word_count(runner):
    test_file = str((Path(__file__).resolve().parent / "resources/test.txt"))
    result = runner.invoke(app, ["word-count", test_file])
    assert result.exit_code == 0
    assert "In total there are 4 words in" in result.stdout.strip()


def test_word_count_failure(runner):
    test_file = str(Path("nonexistingfile"))
    result = runner.invoke(app, ["word-count", test_file])
    assert result.exit_code == 1
    assert result.stdout.strip() == "The path 'nonexistingfile' that you supplied, does not exist."


def test_talk(runner):
    result = runner.invoke(app, ["talk", "hello world", "--repeat", "2", "--loud"])
    assert result.exit_code == 0
    assert result.stdout.strip() == "HELLO WORLD\nHELLO WORLD" 


def test_talk_defaults(runner):
    result = runner.invoke(app, ["talk", "hello world"])
    assert result.exit_code == 0
    assert result.stdout.strip() == "hello world" 


def test_db(runner):
    result = runner.invoke(app, ["db", "create-db", "--table", "gwent"])
    assert result.exit_code == 0
    assert result.stdout.strip() == "Creating table 'gwent' in database." 
