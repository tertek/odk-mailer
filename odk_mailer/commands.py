import typer
from odk_mailer.lib import prompts, utils
from odk_mailer.classes.recipients import Recipients 

def create(csv_file, email_field, message_text):
    typer.echo(">>> Creating mail task")
    # Step 1: Ask for CSV file path (or URL)

    message:str

    # prompt csv_file if no csv file path is set
    if not csv_file:
        answer_csv_file = prompts.csv_file()
        csv_file = answer_csv_file

    recipients = Recipients(csv_file)
    headers = recipients.fieldnames

    # prompt email filed as list
    if not email_field:
        answer_email_field = prompts.email_field(headers)
        email_field = answer_email_field

    # get index within headers
    if email_field not in headers:
        raise typer.Exit("Invalid email_field. Terminating.")

    # validate recipients and process invalid emails in case
    if not recipients.validate(email_field):
        utils.render_table(["id", "email_field", "error"], recipients.invalidEmails)
        ignore_invalid_emails = typer.confirm("Invalid emails found. Would you like to continue although you have invalid emails?")
    
        if not ignore_invalid_emails:
            raise typer.Exit("\nAborted.")

    # prompt message content as editor
    # Do you have a message template ready?
    # if true: ask for message file path 
    # if false: open editor for message content and store in temporary folder
    
    # prompt message text
    if not message_text:
        answer_message = typer.prompt("What is the mail message?")
        message_text = answer_message

    # Success
    print(f"Success. Created job with {recipients.numEmails} mails to be sent.")        
    typer.echo(recipients.data)

    # Replace placeholder with variables using pyhton template engine
    # We will need dictionary for that..

    # finally store mail-tasks in a text file or JSON https://www.w3schools.com/python/python_json.asp
    # https://stackoverflow.com/a/24608746/3127170
    # the task will be stored with final data

    # task = {
    #   csv_file: path/to/file.csv
    #   email_field: email
    #   message: <msg>
    #   sender: <sndr>
    #   reminders: ...
    # }


    # add cron-job via https://pypi.org/project/python-crontab/ and https://stackabuse.com/scheduling-jobs-with-python-crontab/
    # We will need a single job, that checks every hour if we have open reminder tasks.
    # Process reminder tasks as follows: 
    # 1. Perform API request to calculate reminder recipients
    # 2. Send Emails based on calculated recipients
    # 3. Summarize progress

