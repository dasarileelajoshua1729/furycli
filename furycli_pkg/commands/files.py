import typer
import os

file_app = typer.Typer()

@file_app.command("list")
def list_files():
    print(os.listdir())


@file_app.command("read")
def read(name: str):
    try:
        print(open(name).read())
    except:
        print("File not found")


@file_app.command("delete")
def delete(name: str):
    try:
        os.remove(name)
        print("Deleted")
    except:
        print("File not found")
