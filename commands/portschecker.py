from rstatus import RStatusClient
import sys
from rich.console import Console
from rich.text import Text

console = Console()

def checkport(file):
    with open(file, encoding="utf-8") as portsfile:
        readedfile = portsfile.readlines()
        for row in readedfile:
            row = row.strip()
            try:
                client = RStatusClient(row)
                server_data = client.get_server_data(bot=False)

                ip_text = Text(f"{server_data.ip_address}", style="bold yellow")
                players_text = Text(f"{server_data.players.online}", style="bold green")

                console.print(f"[bold cyan]{row}[/bold cyan] - IP Address: {ip_text} Players: {players_text}\n")

            except (TimeoutError, ConnectionRefusedError):
                console.print(f"[bold red]{row}[/bold red] - [bold]isn't open[/bold]\n", style="red")

            except Exception as e:
                console.print(f"[bold red]Error:[/bold red] {e}\n", style="red")

checkport(sys.argv[1])
