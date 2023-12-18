from typer.testing import CliRunner

from odk_mailer.main import app

runner = CliRunner()

def test_app_create_valid():
    result = runner.invoke(app, ["create", "--csv-file", "tests/data/valid.csv", "--email-field","email", "--message-text", "Hello World"])
    assert result.exit_code == 0
    assert "Validated 2 entries." in result.stdout
    assert "Success. Created job with 2 mails to be sent." in result.stdout
    assert "[{'firstname': 'foo', 'lastname': 'bar', 'email': 'foo@yahoo.com'}, {'firstname': 'hoo', 'lastname': 'mar', 'email': 'hoo@gmail.com'}]" in result.stdout

def test_app_create_invalid_csv():
    result = runner.invoke(app, ["create", "--csv-file", "tests/data/invalid.csv", "--email-field","email"],  input="N")
    assert result.exit_code == 1
    assert "Validated 4 entries." in result.stdout
    assert "Aborted" in result.stdout

def test_app_create_invalid_email():
    result = runner.invoke(app, ["create", "--csv-file", "tests/data/invalid.csv", "--email-field","invalid_email_field"])
    assert result.exit_code == 1
    assert "Invalid email_field. Terminating." in result.stdout