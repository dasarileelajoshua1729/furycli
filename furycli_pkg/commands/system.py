import typer
from rich import print
import os
import platform

app = typer.Typer()

@app.command()
def info():
    print("[cyan]System Info:[/cyan]")
    print("OS:", platform.system())
    print("User:", os.getenv("USER"))
    print("Current Dir:", os.getcwd())

@app.command()
def cpu():
    print("[yellow]CPU Info:[/yellow]")
    print(platform.processor())
