import typer
import json
import os

app = typer.Typer()

DB_FILE = "data/db.json"


def load_db():
    if not os.path.exists("data"):
        os.makedirs("data")

    if not os.path.exists(DB_FILE):
        with open(DB_FILE, "w") as f:
            json.dump({}, f)

    with open(DB_FILE, "r") as f:
        return json.load(f)


def save_db(db):
    with open(DB_FILE, "w") as f:
        json.dump(db, f, indent=4)


@app.command()
def insert(table: str, value: str):
    db = load_db()

    if table not in db:
        db[table] = []

    db[table].append(value)
    save_db(db)

    print(f"✅ Inserted into '{table}'")


@app.command()
def show(table: str):
    db = load_db()

    if table not in db or len(db[table]) == 0:
        print("⚠️ No data found")
        return

    print(f"📂 Table: {table}")
    for i, item in enumerate(db[table], 1):
        print(f"{i}. {item}")


@app.command()
def clear(table: str):
    db = load_db()

    if table in db:
        db[table] = []
        save_db(db)
        print(f"🧹 Cleared table '{table}'")
    else:
        print("⚠️ Table not found")
