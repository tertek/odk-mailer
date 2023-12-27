from rich.console import Console
from rich.table import Table
from rich import print
from rich import print_json
from rich.panel import Panel
from rich.columns import Columns
import json

def render_table(header, body):
    console = Console()

    if header:
        table = Table(*header)

    for row in body:
        table.add_row(*row)
    
    console.print(table)

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