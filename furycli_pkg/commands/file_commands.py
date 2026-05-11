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
def delete(name: str):
    if os.path.exists(name):
        os.remove(name)
        print("[red]Deleted:[/red]", name)
    else:
        print("[yellow]File not found[/yellow]")
