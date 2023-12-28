import typer
from odk_mailer import commands, before

from odk_mailer.classes.odk_api import ODKClient

app = typer.Typer(add_completion=False)

@app.callback()
def callback():
    """
    ODK Mailer

    Use it with the create command.

    A new mail job will be created for given CSV_FILE, EMAIL_FIELD, MESSAGE_TEXT and additional options.
    """
    # read config here from $HOME/.odk-mailer
    before.init()



@app.command()
def create(
    source: str = "",
    fields: str = "",
    # source_type: str = "",
    # source_path: str = "",
    # email_field: str = "",
    # data_fields: str = "",
    message: str = "",
    schedule: str = "",
    # force: bool = False
    
):
    """
    Create a mail job, optionally with --csv-file, --email-field, --message-text.
    If these are not entered, user will be prompted.
    """

    commands.create(source, fields, message, schedule)

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


