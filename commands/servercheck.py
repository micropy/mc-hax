from rstatus import RStatusClient
import sys
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich import box

console = Console()

def servercheck(ip, port):
    try:
        ip = ''.join(ip)
        port = ''.join(port)

        console.rule(f"[bold cyan]🌐 Minecraft Server Status Checker[/bold cyan]")

        client = RStatusClient(f"{ip}:{port}")
        server_data = client.get_server_data(bot=False)

        if server_data:
            table = Table(title=f"[bold green]✅ Server Found![/bold green]", box=box.DOUBLE_EDGE, show_lines=True)

            table.add_column("Property", style="bold magenta", justify="right")
            table.add_column("Value", style="bold yellow", justify="left")

            table.add_row("📍 IP Address", server_data.ip_address)
            table.add_row("👥 Online Players", str(server_data.players.online))
            table.add_row("🌐 Version", server_data.version.name)
            table.add_row("📝 MOTD", server_data.motd.clean if hasattr(server_data.motd, 'clean') else "N/A")

            console.print(table)
        else:
            console.print(Panel.fit("[bold red]No server data received.[/bold red]", title="⚠️ Error", border_style="red"))

    except Exception as e:
        console.print(
            Panel.fit(f"[bold red]An error occurred:[/bold red]\n[italic]{str(e)}[/italic]",
                      title="❌ Exception", border_style="red"))
        
servercheck(sys.argv[1], sys.argv[2])
