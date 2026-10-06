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

## Running scripts

There are two ways to run scripts. Both use the same `.venv` environment.

### Option 1 — `uv run` (no activation needed)

Run any script through uv so it uses the project venv and its dependencies:

```powershell
uv run python main.py
uv run python array/example.py
```

You can also run a module the same way (e.g. a package under `oops/`, `algo/`):

```powershell
uv run python -m algo.some_module
```

### Option 2 — activate the venv, then run `python` directly

Activate the venv in your terminal (activates automatically when you open a terminal in VS Code if `.vscode/settings.json` is set up):

```powershell
# PowerShell
.venv\Scripts\Activate.ps1

# CMD
.venv\Scripts\activate.bat
```

Once activated, the prompt is prefixed with `(.venv)` and `python`/`pip` point to the venv, so you can run scripts directly:

```powershell
python main.py
python array/example.py
python -m algo.some_module
```

When done, exit the venv:

```powershell
deactivate
```

You can confirm you're using the venv with:

```powershell
where.exe python   # should show the .venv\Scripts\python.exe path
```

In VS Code, once the `.venv` interpreter is selected (see below), you can open any `.py` file and press **Run** (play button) or **F5** — it will use the venv automatically.

> Tip: use the **Run Python File** play button in the top-right of the editor, or set up a `.vscode/launch.json` to run the current file.

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
