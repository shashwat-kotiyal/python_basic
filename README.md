# python-basic

A collection of Python basics, algorithms, data structures, and practice scripts (including Jupyter notebooks, Robot Framework, and Selenium examples).

## Requirements

- [uv](https://docs.astral.sh/uv/) (package/project manager) — Python is installed automatically by uv
- VS Code (optional, recommended) with the [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) extension

## Clone & Setup

```powershell
# 1. Clone the repository
git clone <repo-url> python-basic
cd python-basic

# 2. Create the venv and install all dependencies from uv.lock
uv sync

# 3. Verify the Python interpreter
uv run python --version
```

> The project pins Python to 3.13 via `.python-version`. uv downloads and installs it automatically.

## Daily uv commands

```powershell
uv sync               # install/sync dependencies into .venv
uv sync --locked      # sync without updating the lockfile
uv sync -U            # upgrade all dependencies and update uv.lock
uv add <package>      # add a dependency
uv remove <package>   # remove a dependency
uv run python script.py
```

## Running Jupyter notebooks

```powershell
uv run jupyter notebook
```

### VS Code setting (fixes "install ipykernel" prompt)

After `uv sync`, VS Code may still ask to install `ipykernel` when you open a `.ipynb` file. This happens when the selected Python interpreter is the global Python (e.g. 3.14) instead of the project venv, which is where uv installs ipykernel.

Fix it by pointing VS Code at the venv interpreter. Add this to `.vscode/settings.json`:

```json
{
  "python.defaultInterpreterPath": "${workspaceFolder}/.venv/Scripts/python.exe",
  "python.terminal.activateEnvironment": true
}
```

Then in any `.ipynb` file, click the kernel name (top-right) → **Select Another Kernel** → **Python Environments** → choose `python-basic` (.venv).

If the prompt appears for a different interpreter, run once:

```powershell
uv run python -m ipykernel install --user
```
