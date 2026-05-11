import typer
import random
import string

tool_app = typer.Typer()

@tool_app.command("random")
def random_string(length: int = 8):
    chars = string.ascii_letters + string.digits
    print(''.join(random.choice(chars) for _ in range(length)))


@tool_app.command("calc")
def calc(x: int, y: int, op: str):
    if op == "+":
        print(x + y)
    elif op == "-":
        print(x - y)
    elif op == "*":
        print(x * y)
    elif op == "/":
        print(x / y)
