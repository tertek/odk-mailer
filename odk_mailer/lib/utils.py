import typer
import os
import string
import csv

from email_validator import validate_email, EmailNotValidError

from rich.progress import track
from rich.console import Console
from rich.table import Table


def is_valid(infile):

    # invalid file extension
    ext = os.path.splitext(infile)[-1].lower()
    if not ext == ".csv":
        return False

    # invalid file path
    if not os.path.isfile(infile):
        return False

    return True

def get_data(infile):
    with open(infile, 'r') as f:
        data = []
        reader = csv.reader(f, skipinitialspace=True)
        for row in reader:
            data.append(row)

        return data

def get_index(data:list,string:str):
    try:
        return data.index(string)
    except:
        return false


def get_invalid(emails, index):
    invalid_emails = []

    total = 0

    print("\nValidating recipients...")
    with typer.progressbar(emails) as progress:
        for row in progress:
            total += 1
            email = row[index]
            try:
                validate_email(email)
            except EmailNotValidError as e:
                invalid = [str(total) ,email, str(e)]
                invalid_emails.append(invalid)
            
    print(f"Validated {total} emails.\n")    
    
    if len(invalid_emails) > 0:
        return invalid_emails

    return False

def render_table(header, body):
    console = Console()

    if header:
        table = Table(*header)

    for row in body:
        table.add_row(*row)
    
    console.print(table)
