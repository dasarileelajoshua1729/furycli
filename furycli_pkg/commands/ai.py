import typer
from rich import print
import os
import subprocess
from datetime import datetime

app = typer.Typer()

MEMORY_FILE = "memory.txt"

# =========================
# SAFE COMMAND LIST
# =========================
ALLOWED_COMMANDS = [
    "ls",
    "pwd",
    "whoami",
    "python --version",
    "uname -a",
    "echo"
]


# =========================
# MEMORY SYSTEM
# =========================
def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return []
    with open(MEMORY_FILE, "r") as f:
        return [line.strip() for line in f.readlines()]


def save_memory(text):
    with open(MEMORY_FILE, "a") as f:
        f.write(text + "\n")


@app.command()
def remember(text: str):
    save_memory(text)
    print(f"[green]🧠 Remembered:[/green] {text}")


@app.command()
def memory():
    data = load_memory()
    print("[cyan]🧠 FuryAI Memory:[/cyan]")
    for i, d in enumerate(data, 1):
        print(f"{i}. {d}")


@app.command()
def chat():
    print("[green]🔥 FuryAI Started (type 'exit' to quit)[/green]")

    memory_data = load_memory()

    while True:
        user_input = input("You: ")
        msg = user_input.lower().strip()

        if msg == "exit":
            print("[red]FuryAI closed[/red]")
            break

        # =========================
        # MEMORY LEARN NAME
        # =========================
        if "my name is " in msg:
            name = msg.replace("my name is ", "")
            save_memory(f"my name is {name}")
            print(f"[green]FuryAI:[/green] Nice to meet you {name}")
            continue

        # =========================
        # ASK NAME
        # =========================
        if "who am i" in msg or "my name" in msg:
            for m in memory_data:
                if "my name is" in m:
                    print(f"[cyan]FuryAI:[/cyan] {m}")
                    break
            else:
                print("[red]I don't know your name yet[/red]")
            continue

        # =========================
        # RUN COMMAND (SAFE)
        # =========================
        if msg.startswith("run "):

            command = msg.replace("run ", "").strip()
            base = command.split()[0]

            if base not in ALLOWED_COMMANDS:
                print(f"[red]Blocked:[/red] {command}")
                continue

            print(f"[yellow]Running:[/yellow] {command}")

            try:
                result = subprocess.check_output(command, shell=True, text=True)
                print(result)
            except Exception as e:
                print(f"[red]ERROR:[/red] {e}")

            continue

        # =========================
        # OPEN FILE
        # =========================
        if msg.startswith("open "):
            file = msg.replace("open ", "")
            subprocess.run(f"explorer.exe {file}", shell=True)
            print(f"[green]Opened {file}[/green]")
            continue

        # =========================
        # CREATE PYTHON
        # =========================
        if "create python calculator" in msg:
            with open("calculator.py", "w") as f:
                f.write("""num1 = float(input())
num2 = float(input())
print(num1 + num2)
""")
            print("[green]Created calculator.py[/green]")
            continue

        elif "create python" in msg:
            with open("hello.py", "w") as f:
                f.write("print('Hello FuryAI')")
            print("[green]Created hello.py[/green]")
            continue

        # =========================
        # CREATE HTML
        # =========================
        if "create html login page" in msg:
            with open("login.html", "w") as f:
                f.write("<h1>Login Page</h1>")
            print("[green]Created login.html[/green]")
            continue

        elif "create html" in msg:
            with open("index.html", "w") as f:
                f.write("<h1>FuryAI Page</h1>")
            print("[green]Created index.html[/green]")
            continue

        # =========================
        # CREATE CSS
        # =========================
        if "create css" in msg:
            with open("style.css", "w") as f:
                f.write("body{background:black;color:white;}")
            print("[green]Created style.css[/green]")
            continue

        # =========================
        # CREATE JS
        # =========================
        if "create javascript" in msg:
            with open("script.js", "w") as f:
                f.write("alert('FuryAI');")
            print("[green]Created script.js[/green]")
            continue

        # =========================
        # WEBSITE GENERATOR
        # =========================
        if "create website" in msg:

            theme = "default"
            if "anime" in msg:
                theme = "anime"
            elif "gaming" in msg:
                theme = "gaming"
            elif "dark" in msg:
                theme = "dark"
            elif "business" in msg:
                theme = "business"

            html = f"<h1>{theme.upper()} WEBSITE</h1>"
            css = "body{background:black;color:white;text-align:center;}"

            with open("index.html", "w") as f:
                f.write(html)

            with open("style.css", "w") as f:
                f.write(css)

            print(f"[green]Created {theme} website[/green]")
            continue

        # =========================
        # TKINTER APP
        # =========================
        if "create tkinter app" in msg:

            code = """import tkinter as tk

root = tk.Tk()
root.title("FuryAI App")

label = tk.Label(root, text="Hello FuryAI")
label.pack()

root.mainloop()
"""

            with open("fury_app.py", "w") as f:
                f.write(code)

            print("[green]Created fury_app.py[/green]")
            continue

        # =========================
        # DEFAULT RESPONSE
        # =========================
        print(f"You said: {user_input}")
