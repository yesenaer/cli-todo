from typer.testing import CliRunner
from db import app


runner = CliRunner()


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