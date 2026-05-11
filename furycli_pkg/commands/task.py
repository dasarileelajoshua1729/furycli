import typer
import subprocess
from rich import print

app = typer.Typer()


@app.command()
def cmd(command: str):
    """
    Run terminal commands
    """

    print(f"[yellow]Running:[/yellow] {command}")

    result = subprocess.run(
        command,
        shell=True,
        text=True,
        capture_output=True
    )

    print("[green]OUTPUT:[/green]")
    print(result.stdout)

    if result.stderr:
        print("[red]ERROR:[/red]")
        print(result.stderr)
