import typer
from typing_extensions import Annotated
from odk_mailer import commands, before
from odk_mailer.classes.odk_api import ODKClient

app = typer.Typer(add_completion=False)

@app.callback()
def callback():
    """
    ODK Mailer

    Setup mail jobs by fetching recipients from CSV files or ODK API.

    Run mail jobs immediately or schedule them to be run over time.

    Automatically send reminders to non-responding mail recipients.
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
    """
    commands.create(source, fields, message, schedule)

@app.command()
def run(
    id: Annotated[str, typer.Argument(help="Hexadecimal hash")]
):
    """
    Run a mail job by id
    """
    commands.run(id)

@app.command()
def list():
    """
    List available mail jobs
    """    
    commands.list()

# @app.command()
# def config():
#     """
#     Configure ODK Mailer
#     """
#     typer.echo("Open configuration dialog if no config")
# @app.command()
# def api():
#     """
#     Send api request
#     """
#     typer.echo("api call")

#     odk_client = ODKClient()

#     # odk_client.auth()

#     # odk_client.submissions_data()

#     odk_client.form_attachment()



