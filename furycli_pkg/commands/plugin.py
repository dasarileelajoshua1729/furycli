import typer
import os
from rich import print

app = typer.Typer()

PLUGIN_DIR = "plugins"


@app.command()
def install(name: str):
    """
    Install a plugin
    """

    os.makedirs(PLUGIN_DIR, exist_ok=True)

    plugin_file = f"{PLUGIN_DIR}/{name}.plugin"

    with open(plugin_file, "w") as f:
        f.write(f"Plugin: {name}")

    print(f"[green]✅ Plugin '{name}' installed[/green]")


@app.command()
def list():
    """
    List installed plugins
    """

    if not os.path.exists(PLUGIN_DIR):
        print("[red]No plugins installed[/red]")
        return

    plugins = os.listdir(PLUGIN_DIR)

    if not plugins:
        print("[red]No plugins found[/red]")
        return

    print("[blue]Installed Plugins:[/blue]")

    for plugin in plugins:
        print(f"- {plugin}")
