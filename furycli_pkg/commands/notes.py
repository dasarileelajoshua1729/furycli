import typer
import os

app = typer.Typer()

NOTES_FILE = os.path.expanduser("~/.fury_notes.txt")


def load_notes():
    if not os.path.exists(NOTES_FILE):
        return []
    with open(NOTES_FILE, "r") as f:
        return f.readlines()


def save_notes(notes):
    with open(NOTES_FILE, "w") as f:
        f.writelines(notes)


@app.command()
def add(text: str):
    notes = load_notes()
    notes.append(text + "\n")
    save_notes(notes)
    print("✅ Note added")


@app.command()
def show():
    notes = load_notes()
    if not notes:
        print("No notes found")
        return

    print("📒 Your Notes:")
    for i, note in enumerate(notes, start=1):
        print(f"{i}. {note.strip()}")


@app.command()
def delete(index: int):
    notes = load_notes()

    if index < 1 or index > len(notes):
        print("❌ Invalid index")
        return

    removed = notes.pop(index - 1)
    save_notes(notes)
    print(f"🗑 Deleted: {removed.strip()}")


@app.command()
def clear():
    if os.path.exists(NOTES_FILE):
        os.remove(NOTES_FILE)
    print("🧹 All notes cleared")
