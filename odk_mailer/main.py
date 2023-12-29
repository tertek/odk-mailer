import typer
from odk_mailer import commands, before

from odk_mailer.classes.odk_api import ODKClient

app = typer.Typer(add_completion=False)

@app.callback()
def callback():
    """
    ODK Mailer

    Use it with the create command.

    A new mail job will be created for given SOURCE, FIELDS, MESSAGE and SCHEDULE.
    """
    # read config here from $HOME/.odk-mailer
    before.init()

@app.command()
def create(
    source: str = "",
    fields: str = "",
    message: str = "",
    schedule: str = ""
):
    """
    Create a mail job.
    If these are not entered, user will be prompted.
    """
    commands.create(source, fields, message, schedule)

@app.command()
def list():
    """
    List available mail jobs
    """
    typer.echo("Listing mail jobs")
    
@app.command()
def config():
    """
    Configure ODK Mailer
    """
    typer.echo("Open configuration dialog if no config")
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



