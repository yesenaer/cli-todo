from pathlib import Path
from todo.helper import create_file_if_not_exists


def test_create_file_if_not_already_exists(test_data):
    assert test_data.exists()
    assert not create_file_if_not_exists(test_data)


def test_create_file_if_not_already_exists_created():
    path = Path(__file__).parent.resolve() / "resources" / "non_existing.yml"
    assert not path.exists()
    assert create_file_if_not_exists(path)
    assert path.exists()
    path.unlink()
    assert not path.exists()
