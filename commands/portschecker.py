from rstatus import RStatusClient
import sys
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich import box

console = Console()

def checkport(file_path):
    try:
        with open(file_path, encoding="utf-8") as ports_file:
            read_lines = [line.strip() for line in ports_file if line.strip()]
            if not read_lines:
                console.print(Panel.fit("[bold yellow]The file is empty or improperly formatted.[/bold yellow]", title="⚠️ Warning"))
                return

            table = Table(title="🔌 [bold cyan]Port Checker Results[/bold cyan]", box=box.ROUNDED, show_lines=True)
            table.add_column("Target", style="bold magenta", justify="left")
            table.add_column("Status", style="bold yellow", justify="center")
            table.add_column("Players", style="bold green", justify="center")

            for row in read_lines:
                try:
                    client = RStatusClient(row)
                    server_data = client.get_server_data(bot=False)

                    status = "[bold green]🟢 Open[/bold green]"
                    players = f"{server_data.players.online}"
                    table.add_row(f"{server_data.ip_address}", status, players)

                except (TimeoutError, ConnectionRefusedError):
                    status = "[bold red]🔴 Closed[/bold red]"
                    table.add_row(f"{row}", status, "N/A")

                except Exception as e:
                    status = "[bold red]⚠️ Error[/bold red]"
                    table.add_row(f"{row}", status, str(e))

            console.rule("[bold cyan]📋 Port Scan Summary[/bold cyan]")
            console.print(table)

    except FileNotFoundError:
        console.print(Panel.fit(f"[bold red]File not found:[/bold red] {file_path}", title="❌ Error"))
    except Exception as e:
        console.print(Panel.fit(f"[bold red]Unexpected error:[/bold red] {str(e)}", title="❌ Error"))

checkport(sys.argv[1])
