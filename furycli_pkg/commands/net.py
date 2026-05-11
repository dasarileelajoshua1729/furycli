import typer
from rich import print
import os

# ✅ CREATE FIRST
app = typer.Typer()

# --------------------
# PING
# --------------------
@app.command()
def ping(host: str):
    print(f"[cyan]Pinging {host}...[/cyan]")
    os.system(f"ping -c 4 {host}")


# --------------------
# DOWNLOAD
# --------------------
@app.command()
def download(url: str, filename: str):
    import urllib.request

    print(f"[cyan]Downloading {url}...[/cyan]")
    try:
        urllib.request.urlretrieve(url, filename)
        print(f"[green]Saved as {filename}[/green]")
    except Exception as e:
        print(f"[red]Error:[/red] {e}")
