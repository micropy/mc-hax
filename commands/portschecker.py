from rstatus import RStatusClient
import sys
from rich.console import Console
from rich.text import Text
from rich.panel import Panel
from rich.table import Table
from rich import box
from rich.rule import Rule

console = Console()

def checkport(file):
    console.print(Rule(title="[bold cyan]🔌 Port Status Checker[/bold cyan]", characters="━"))
    
    with open(file, encoding="utf-8") as portsfile:
        readedfile = portsfile.readlines()
        for row in readedfile:
            row = row.strip()
            try:
                client = RStatusClient(row)
                server_data = client.get_server_data(bot=False)

                table = Table(box=box.MINIMAL, show_edge=False, expand=True, padding=(0, 1))
                table.add_column("Info", justify="right", style="bold blue")
                table.add_column("Data", justify="left", style="bold yellow")

                table.add_row("🌐 IP", f"{server_data.ip_address}")
                table.add_row("👥 Players", f"[bold green]{server_data.players.online}[/bold green]")

                console.print(Panel.fit(table, title=f"[bold green]✅ {row}[/bold green]", border_style="green"))

            except (TimeoutError, ConnectionRefusedError):
                console.print(
                    Panel.fit(
                        f"[bold red]{row}[/bold red] - [italic]isn't open[/italic]",
                        title="⚠️ [bold red]Connection Error[/bold red]",
                        border_style="red"
                    )
                )

            except Exception as e:
                console.print(
                    Panel.fit(
                        f"[bold red]Error:[/bold red] {e}",
                        title="❌ [bold red]Exception[/bold red]",
                        border_style="red"
                    )
                )

checkport(sys.argv[1])
