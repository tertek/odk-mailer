from email_validator import validate_email, EmailNotValidError

import typer
from rich.progress import track
from rich.console import Console
from rich.table import Table

def get_invalid(emails, field):
    invalid_emails = []

    total = 0


    print("\nValidating recipients...")
    with typer.progressbar(emails) as progress:
        for row in progress:
            total += 1
            email = row[field]
            try:
                if not email:
                    raise EmailNotValidError("Email address missing. Check for missing delimiters (',') in your CSV file.")
                validate_email(email)
            except EmailNotValidError as e:
                invalid = [str(total) ,email, str(e)]
                invalid_emails.append(invalid)
            
    print(f"Validated {total} entries.\n")    
    
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
