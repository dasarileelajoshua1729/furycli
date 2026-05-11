import typer
import os

app = typer.Typer()

IGNORE_DIRS = {"venv", "__pycache__", ".git"}
IGNORE_FILES = {".pyc", ".save", ".log"}


@app.command()
def file(name: str):
    print(f"Searching for file: {name}")
    for root, dirs, files in os.walk("."):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]

        for f in files:
            if any(f.endswith(ext) for ext in IGNORE_FILES):
                continue

            if name.lower() in f.lower():
                print(os.path.join(root, f))


@app.command()
def text(query: str):
    print(f"Searching inside files for: '{query}'\n")

    for root, dirs, files in os.walk("."):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]

        for file in files:
            if any(file.endswith(ext) for ext in IGNORE_FILES):
                continue

            path = os.path.join(root, file)

            try:
                with open(path, "r", errors="ignore") as f:
                    for i, line in enumerate(f, start=1):
                        if query.lower() in line.lower():
                            print(f"{path} (line {i}): {line.strip()}")
            except:
                continue
