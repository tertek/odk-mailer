import typer
from odk_mailer import commands

from rich.console import Console
from rich.table import Table

from odk_mailer.classes.recipients import Recipients
import csv

from odk_mailer.classes.odk_api import ODKClient


app = typer.Typer(add_completion=False)

@app.callback()
def callback():
    """
    ODK Mailer

    Use it with the create command.

    A new mail job will be created for given CSV_FILE, EMAIL_FIELD, MESSAGE_TEXT and additional options.
    """


@app.command()
def create(
    csv_file: str = "",
    email_field: str = "",
    message_text: str = ""
):
    """
    Create a mail job, optionally with --csv-file, --email-field, --message-text.
    If these are not entered, user will be prompted.
    """

    commands.create(csv_file, email_field, message_text)

@app.command()
def api():
    """
    Send api request
    """
    typer.echo("api call")

    odk_client = ODKClient()

    # odk_client.auth()

    # odk_client.submissions_data()

    odk_client.form_attachment()



@app.command()
def list():
    """
    List available mail jobs
    """
    typer.echo("Listing mail jobs")

