from pathlib import Path
from yaml import safe_dump


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
