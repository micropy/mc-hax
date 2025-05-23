from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich import box
import requests
import sys

console = Console()

def mojangapi(username):
    console.rule(f"[bold cyan]🔍 Mojang API Lookup[/bold cyan]")

    api = f'https://api.mojang.com/users/profiles/minecraft/{username}'
    response = requests.get(api)

    if response.status_code == 200:
        infojson = response.json()

        table = Table(title=f"[bold green]Minecraft Profile[/bold green] 🎮", box=box.ROUNDED, expand=False)
        table.add_column("Field", style="bold magenta", justify="center")
        table.add_column("Value", style="bold yellow", justify="center")

        table.add_row("Username", infojson["name"])
        table.add_row("UUID", infojson["id"])

        console.print(table)
    elif response.status_code == 204:
        console.print(
            Panel.fit(f"[bold red]User '{username}' not found.[/bold red]", border_style="red", title="Error ❌")
        )
    else:
        console.print(
            Panel.fit(f"[bold red]Request failed (status code {response.status_code})[/bold red]", border_style="red", title="Error ⚠️")
        )

mojangapi(sys.argv[1])
