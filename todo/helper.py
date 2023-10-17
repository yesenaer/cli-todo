from pathlib import Path
from yaml import safe_load, safe_dump


def create_file_if_not_exists(path: Path) -> bool:
    """Creates file if it does not yet exist.

    Args:
        path (pathlib.Path): Path to file.

    Returns:
        bool: if a file was created.
    """
    if not path.exists():
        with open(path, "w") as w:
            data = {"todo": []}
            safe_dump(data, w, sort_keys=False)
            return True
    return False


def load_data_from_file(path: Path):
    """Loads data from file at file path.

    Args:
        path (Path, optional): path of existing file. Defaults to path of "data/data.yml".

    Returns:
        dict: Data as a dict.
    """
    with open(path, "r") as f:
        return safe_load(f)
    
    
def write_data_to_file(data: dict, path: Path):
    """Writes received data to file at path.

    Args:
        data (dict): Data that requires to be written.
        path (Path, optional): path of existing file. Defaults to path of "data/data.yml".
    """
    with open(path, "w") as f:
        safe_dump(data, f, sort_keys=False)


def get_item_from_list(data: dict, key: str, list: str = "todo") -> dict:
    """Returns the requested item from list if item exists.

    Args:
        data (dict): data to retrieve item from.
        key (str): name that identifies item.
        list (str, optional): The list that the item needs to be retrieved from. Defaults to "todo".

    Returns:
        dict: the key's information.
    """
    list = data.get(list)
    for entry in list: 
        if entry.get("item") == key:
            return entry
        

def update_item_in_list(data: dict, key: str, done: bool, list: str = "todo") -> dict:
    """Updates the requested item in list if item exists.

    Args:
        data (dict): data to update item in.
        key (str): name that identifies item.
        done (bool) the status that is to be updated.
        list (str, optional): The list that the item needs to be retrieved from. Defaults to "todo".

    Returns:
        dict: the key's information.
    """
    list = data.get(list)
    for entry in list: 
        if entry.get("item") == key:
            entry["done"] = done
    return data


def remove_item_from_list(data: dict, key: str, list: str = "todo") -> dict:
    """Removes the requested item from list if item exists.

    Args:
        data (dict): data to remove item from.
        key (str): name that identifies item.
        list (str, optional): The list that the item needs to be removed from. Defaults to "todo".

    Returns:
        dict: data without the key.
    """
    list = data.get(list)
    for index, entry in enumerate(list): 
        if entry.get("item") == key:
            list.pop(index)
    return data
