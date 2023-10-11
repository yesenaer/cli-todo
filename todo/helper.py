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
