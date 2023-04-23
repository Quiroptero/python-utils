from typing import List
from pathlib import Path


def find_dirs_without_readme() -> List[str]:
    """Finds all top-directories relative to the current location that do not contain a README.md file.

    Returns:
        A list containing the names of the directories that match the condition.
    """
    p = Path(".").resolve()
    dirs = [d for d in p.glob(pattern="*") if d.is_dir()]
    parents = [r.parent for r in p.glob(pattern="*/README.md")]
    return [d.name for d in dirs if d not in parents]
