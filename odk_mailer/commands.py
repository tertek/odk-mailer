import typer
import sys
from odk_mailer.lib import prompts, validators, utils, log
from odk_mailer.classes.job import Job 


def create(source, fields, message, schedule):
    typer.echo(">>> Creating a mail job")

    if not source:
        p_source = prompts.source()
        source  = utils.join(p_source)    
    
    v_source = validators.source(source)

    # Get raw data
    raw = utils.get_raw(v_source)

    if not fields:
        p_fields = prompts.fields(raw["headers"])    
        fields = utils.join(p_fields)

    v_fields = validators.fields(fields, raw["headers"])

    if not message:
        p_message = prompts.message()
        message = utils.join(p_message)

    v_message = validators.message(message)    

    if not schedule:
        p_schedule = prompts.schedule()
        if p_schedule["now"]:
            schedule = "now"
        else: schedule=p_schedule["future"]

    v_schedule = validators.schedule(schedule)


    # mailJob.setSchedule(schedule)

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

    # mailJob.save()

    # run mail job

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

