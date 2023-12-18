from typer.testing import CliRunner

from odk_mailer.main import app

runner = CliRunner()

def test_app_create_valid():
    result = runner.invoke(app, ["create", "--csv-file", "tests/data/valid.csv", "--email-field","email", "--message-text", "Hello World"])
    assert result.exit_code == 0
    assert "Validated 2 entries." in result.stdout
    assert "Success. Created job with 2 mails to be sent." in result.stdout
    assert "[{'firstname': 'foo', 'lastname': 'bar', 'email': 'foo@yahoo.com'}, {'firstname': 'hoo', 'lastname': 'mar', 'email': 'hoo@gmail.com'}]" in result.stdout

