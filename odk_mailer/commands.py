import typer
import sys
from odk_mailer.lib import prompts, utils
from odk_mailer.classes.recipients import Recipients 
from odk_mailer.classes.job import Job 


def create(source_type, source_path, email_field, data_fields, message, schedule, force):
    typer.echo(">>> Creating a mail job")

    # prompt source type
    if not source_type:
        answer_source_type = prompts.source_type()
        source_type = answer_source_type["source_type"]

    mailJob = Job(source_type)

    # prompt source path
    if mailJob.source["type"] == 'file':
        if not source_path:
            answer_source_path_file = prompts.source_path_file()
            source_path = answer_source_path_file["source_path_file"]
    elif mailJob.source["type"] == 'api':
        # check API connection & credentials
        # promptAPIcredentials() // host, user, pass, project
        # checkAPIconnection()  // auth endpoint
        if not source_path:
            answer_source_path = prompts.source_path_api()
    else:
        raise Exception("Something went wrong.")
      
    mailJob.setSourcePath(source_path)
    
    # prompt email filed as list
    if not email_field:
        answer_email_field = prompts.email_field(mailJob.headers)
        email_field = answer_email_field["email_field"]
    
    mailJob.setEmailField(email_field)

    if not data_fields:
        answer_data_fields = prompts.data_fields( list(filter(lambda x: x != mailJob.email_field, mailJob.headers)) )
        data_fields = answer_data_fields["data_fields"]

    mailJob.setDataFields(data_fields)

    # prompt message input string that is going to be split into list
    if not message:
        answer_message = prompts.message()
        message = answer_message["message_sender"] + ":" + answer_message["message_format"] + ":" + answer_message["message_source"] + ":" + answer_message["message_content"]

    mailJob.setMessage(message)

    if not schedule:
        answer_schedule = prompts.schedule()
        if answer_schedule["schedule_now"]:
            schedule = "now"
        else:
            schedule = answer_schedule["schedule_datetime"]
        
    mailJob.setSchedule(schedule)

    #
    # tbd: add reminders
    #

    # optional: confirm mailjob on summary
    # utils.render_summary(mailJob)
    # if not force:
    #     answer_confirmed = prompts.confirm()
    #     confirmed = answer_confirmed["confirm"]
    # else: confirmed = force

    # if not confirmed:
    #     raise typer.Exit("MailJob was not confirmed.")

    mailJob.save()

    sys.exit()

    # validate recipients and process invalid emails in case
    # if not recipients.validate(email_field):
    #     utils.render_table(["id", "email_field", "error"], recipients.invalidEmails)
    #     ignore_invalid_emails = typer.confirm("Invalid emails found. Would you like to continue although you have invalid emails?")
    
    #     if not ignore_invalid_emails:
    #         raise typer.Exit("\nAborted.")


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

