from rich.console import Console
from rich.table import Table
from rich import print
from rich import print_json
from rich.panel import Panel
from rich.columns import Columns
import json
import typer
import csv 


def abort(msg):
    print("[bold red]Error:[/bold red] "+msg)
    raise typer.Abort()


def render_table(header, body):
    console = Console()

    if header:
        table = Table(*header)

    for row in body:
        table.add_row(*row)
    
    console.print(table)

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

# def render_summary(data):

#     content_config = "source_type: " + data.source_type + "\n" + "source_path: " + data.source_path + "\n" + "email_field: " + data.email_field + "\n" + "data_fields: " + ','.join(data.data_fields) 

#     content_message = ""
#     for k, v in data.message.items():
#         content_message += str(k) + ": "+ str(v) + "\n"
#     test2 = [content_config, content_message+ "\n" + "# recipients:" + str(len(data.recipients))]

#     columns = Columns(test2, expand=True)

#     print(Panel(columns, title="Summary"))


def render_json(summary):
    
    print_json(json.dumps(summary))

def get_choices(**foo):
    print(foo["answers"])
    
    return ["Foo"]