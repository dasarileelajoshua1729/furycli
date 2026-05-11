import typer
import subprocess
from rich import print

app = typer.Typer()


@app.command()
def exe():
    """
    Build FuryCLI executable
    """

    print("[yellow]Building FuryCLI executable...[/yellow]")

    subprocess.run(
        [
            "pyinstaller",
            "--onefile",
            "furycli_pkg/__main__.py",
            "--name",
            "furycli",
        ]
    )

    print("[green]✅ Build complete![/green]")
