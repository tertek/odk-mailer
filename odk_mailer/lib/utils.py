from rich.console import Console
from rich.table import Table

def render_table(header, body):
    console = Console()

    if header:
        table = Table(*header)

    for row in body:
        table.add_row(*row)
    
    console.print(table)
