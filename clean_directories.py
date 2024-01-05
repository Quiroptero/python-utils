"""Delete directories of a git project if the directory is not associated to any active git worktree."""

# Set project_path to the absolute path to your project directory.
# In other words, the directory where you have checked out the main branch of the project.
project_path="/absolute/path/to/your/project"

# DO NOT EDIT BELOW THIS LINE
# ===========================

import pathlib
import shutil
import subprocess

project_path = pathlib.Path(project_path)

# Get the list of active git worktrees
active_worktrees = subprocess.check_output(
  ["git", "-C", str(project_path), "worktree", "list", "--porcelain"],
  text=True
).splitlines()

active_worktree_paths = [pathlib.Path(worktree.split()[1]) for worktree in active_worktrees if "worktree" in worktree]
all_directories = [d for d in pathlib.Path(project_path).parent.iterdir() if d.is_dir()]

for dir in all_directories:
    if dir not in active_worktree_paths:
        print(f"Deleting dir: {dir}")
        shutil.rmtree(dir)
