import typer
import csv 
import time
from rich import print
from rich import print_json
from rich.console import Console
from rich.columns import Columns
from rich.table import Table
from rich.panel import Panel

def abort(msg):
    print("[bold red]Error:[/bold red] "+msg)
    raise typer.Abort()

def now():
    return int(time.time())

def join(answers):

    filtered = []

    for x in answers:
        if answers[x] != None:
            to_append = answers[x]
            if type(answers[x]) is list:
                to_append = ",".join(answers[x])
                
            filtered.append(to_append)

    return "::".join(filtered)

def get_raw(source):    
    if source.type == 'file':        
        with open(source.path, newline='') as f:
            reader = csv.DictReader(f, skipinitialspace=True)
            headers = reader.fieldnames
            rows = []
            for row in reader:
                rows.append(row)
    else: 
        raise Exception("Source type 'api' is not yet implemented.")
    
    return { "headers": headers, "rows": rows}

def render_table(header, body):
    console = Console()

    if header:
        table = Table(*header)

    for row in body:
        table.add_row(*row)
    
    console.print(table)