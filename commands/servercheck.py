from rstatus import RStatusClient
import sys
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.rule import Rule

console = Console()

def servercheck(ip, port):
    try:
        ip = ''.join(ip)
        port = ''.join(port)

        console.print(Rule(title="[bold cyan]🌐 Server Status Checker[/bold cyan]", characters="━"))

        client = RStatusClient(f"{ip}:{port}")
        server_data = client.get_server_data(bot=False)

        if server_data:
            console.print(
                Panel.fit(
                    f"[bold blue]📍 IP:[/bold blue] [bold yellow]{server_data.ip_address}[/bold yellow]\n"
                    f"[bold blue]👥 Players Online:[/bold blue] [bold green]{server_data.players.online}[/bold green]",
                    title="✅ [bold green]Server Online[/bold green]",
                    border_style="green"
                )
            )

    except Exception as e:
        console.print(
            Panel.fit(
                f"[bold red]An error occurred:[/bold red]\n[italic]{str(e)}[/italic]",
                title="❌ [bold red]Exception[/bold red]",
                border_style="red"
            )
        )

servercheck(sys.argv[1], sys.argv[2])
