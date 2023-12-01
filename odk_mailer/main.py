import typer
from odk_mailer import commands

from rich.console import Console
from rich.table import Table

app = typer.Typer(add_completion=False)

@app.callback()
def callback():
    """
    ODK Mailer

    Use it with the create command.

    A new mail task will be created for given CSV_FILE, EMAIL_FIELD and additional options.
    """


@app.command()
def create(
    csv_file: str = "",
    email_field: str = "",
):
    """
    Create a mail, optionally with --csv-file, --email-field.

    If --reminders is used, setup their frequency.
    """

    commands.create(csv_file, email_field)


@app.command()
def list():
    """
    List available mail tasks
    """
    typer.echo("Listing mail tasks")



