from helper import (create_file_if_not_exists, load_data_from_file, write_data_to_file, get_item_from_list,
remove_item_from_list, update_item_in_list)


def test_create_file_if_not_already_exists(test_file):
    assert test_file.exists()
    assert not create_file_if_not_exists(test_file)


def test_create_file_if_not_already_exists_created(resource_dir):
    path = resource_dir / "non_existing.yml"
    assert not path.exists()
    assert create_file_if_not_exists(path)
    assert path.exists()
    path.unlink()
    assert not path.exists()


def test_load_data_from_file(test_file):
    data = load_data_from_file(test_file)
    assert data == {"todo": []}


def test_write_data_to_file(test_file):
    data = {"other": "data"}
    write_data_to_file(data, test_file)
    result = load_data_from_file(test_file)
    assert result == data
    

def test_get_item_from_list():
    data = {"todo": [{"item": "swords", "done": False}, {"item": "potions", "done": False}]}
    actual = get_item_from_list(data, "swords")
    assert actual == {"item": "swords", "done": False}


def test_update_item_in_list():
    data = {"todo": [{"item": "swords", "done": False}, {"item": "potions", "done": False}]}
    actual = update_item_in_list(data, "swords", True)
    assert actual == {"todo": [{"item": "swords", "done": True}, {"item": "potions", "done": False}]}


def test_remove_item_from_list():
    data = {"todo": [{"item": "swords", "done": False}, {"item": "potions", "done": False}]}
    actual = remove_item_from_list(data, "swords")
    assert actual == {"todo": [{"item": "potions", "done": False}]}

