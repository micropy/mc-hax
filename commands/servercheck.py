from rstatus import RStatusClient
import sys
from colorama import Fore
from rich.console import Console

console = Console()

def servercheck(ip, port):
    try:
        # Get Java Server status
        ip = ''.join(ip)
        port = ''.join(port)
        client = RStatusClient(f"{ip}:{port}")
        server_data = client.get_server_data(bot=False)
        if server_data:
                console.print(f"[bold blue]IP:[/bold blue] [bold yellow]{server_data.ip_address}[/bold yellow]")
                console.print(f"[bold blue]Players Online:[/bold blue] [bold green]{server_data.players.online}[/bold green]")
    except Exception as e:
        print(e)

servercheck(sys.argv[1], sys.argv[2])