import typer
import os
from rich import print

app = typer.Typer()


@app.command()
def create(name: str):
    """
    Create a new Fury project
    """

    if os.path.exists(name):
        print(f"❌ Folder '{name}' already exists")
        return

    os.makedirs(f"{name}/src")
    os.makedirs(f"{name}/data")
    os.makedirs(f"{name}/logs")

    with open(f"{name}/README.md", "w") as f:
        f.write(f"# {name}\n\nCreated with FuryCLI 🔥")

    with open(f"{name}/src/main.py", "w") as f:
        f.write("print('Hello from Fury Project 🚀')")

    print(f"[green]✅ Project '{name}' created successfully![/green]")
