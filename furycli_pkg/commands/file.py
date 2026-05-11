import typer
from rich import print
import os

app = typer.Typer()

@app.command()
def list():
    print("[cyan]Files in current folder:[/cyan]")
    for f in os.listdir():
        print("-", f)

@app.command()
def create(name: str):
    filename = name + ".txt"
    with open(filename, "w") as f:
        f.write("Created by FuryCLI")
    print("[green]File created:[/green]", filename)

@app.command()
def delete(name: str):
    filename = name + ".txt"
    if os.path.exists(filename):
        os.remove(filename)
        print("[red]Deleted:[/red]", filename)
    else:
        print("[yellow]File not found[/yellow]")

@app.command()
def read(name: str):
    filename = name + ".txt"
    if os.path.exists(filename):
        with open(filename, "r") as f:
            print("[green]Content:[/green]")
            print(f.read())
    else:
        print("[red]File not found[/red]")
