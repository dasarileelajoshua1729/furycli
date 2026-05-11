import typer
from rich import print

# import all command apps
from furycli_pkg.commands.db import app as db_app
from furycli_pkg.commands.file import app as file_app
from furycli_pkg.commands.system import app as system_app
from furycli_pkg.commands.search import app as search_app
from furycli_pkg.commands.notes import app as notes_app
from furycli_pkg.commands.net import app as net_app
from furycli_pkg.commands.project import app as project_app
from furycli_pkg.commands.task import app as task_app
from furycli_pkg.commands.plugin import app as plugin_app
from furycli_pkg.commands.build import app as build_app
from furycli_pkg.commands.ai import app as ai_app
app = typer.Typer()

# attach subcommands
app.add_typer(file_app, name="file")
app.add_typer(system_app, name="system")
app.add_typer(search_app, name="search")
app.add_typer(notes_app, name="notes")
app.add_typer(net_app, name="net")
app.add_typer(project_app, name="project")
app.add_typer(db_app, name="db")
app.add_typer(task_app, name="task")
app.add_typer(plugin_app, name="plugin")
app.add_typer(plugin_app, name="plugin")
app.add_typer(build_app, name="build")
app.add_typer(ai_app, name="ai")
# main commands
@app.command()
def start():
    print("[green]🔥 FuryCLI running[/green]")


@app.command()
def hello():
    print("[blue]Hello from FuryCLI 👋[/blue]")


@app.command()
def version():
    print("[bold green]FuryCLI v1.0[/bold green]")
