import sys
import os
import json
from odk_mailer.lib import prompts, validators, utils, log, globals, mail
from odk_mailer.classes.job import Job 

def run(hash):
    if not hash:
        utils.abort("ID is required")

    # get mail job by id
    with open(globals.odk_mailer_jobs, "r") as f:
        jobs = json.load(f)

    found = next((obj for obj in jobs if obj["hash"].startswith(hash)), None)
    if not found:
        utils.abort("Job not found.")
  
    # maybe better to check this later?
    # if found["scheduled"] > utils.now():
    #     utils.abort("Schedule is in future")
    
    path_jobs = os.path.join(globals.odk_mailer_job, found['hash']+'.json')
    with open(path_jobs, 'r', encoding='utf-8') as f:
        job = json.load(f)

    # generate mails: format contents
    # instance of Mailer class: mailer = Mailer(job)
    # mailer.send() iterates over recipients
    # for now lets use lib.mail.py
    message = job["message"]
    recipients = job["recipients"]
    print(message)
    print(recipients)

    # send
    for recipient in recipients:
        mail.send(recipient, message)
    

def create(source, fields, message, schedule):

    if not source:
        p_source = prompts.source()
        source  = utils.join(p_source)    
    
    v_source = validators.source(source)

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

    # tbd: Reminders
    # reminders have two attributes:
    # total_amount, frequency, e.g. 3 times in total, every hour|day|week|custom frequency
    # after first scheduled send

    # reminders will be stored inside .odk-mailer/reminder/hash_instance.json
    # having updated recipients from non-respondents (calculated from base recipients and respondents) 
    # on a per reminder case

    # https://github.com/tertek/zapier-odk-scripts/blob/main/get_non_responding.py
    # reminders require api connection and following inputs
    # form_register = "test_form_register" #name of form that is used for registration, given as api or csv
    # form_follow = "test_form_follow"  # name of form that is used for follow up
    # # if use_form_attachment
    # form_follow_attached = "test_form_follow_attached" # name of form that is used for follow up; 
    # form_attachment = "follow.csv" # name of form attachment attached to form_follow; 
    # # field config
    # field_email_register = "email_register" # name of email field for registration form, given
    # field_email_follow = "email_follow"
    # field_email_follow_attach = "email"

    job = Job(v_source, v_fields, v_message, v_schedule, raw)
    
    if "pytest" in sys.modules:
        # testing
        print(vars(job))
        sys.exit()
        
    saved = job.save()
    # run mail job with odk-mailer run <hash>

    sys.exit()

    # validate recipients and process invalid emails in case
    # if not recipients.validate(email_field):
    #     utils.render_table(["id", "email_field", "error"], recipients.invalidEmails)
    #     ignore_invalid_emails = typer.confirm("Invalid emails found. Would you like to continue although you have invalid emails?")
    
    #     if not ignore_invalid_emails:
    #         raise typer.Exit("\nAborted.")
    # store mail-tasks in a text file or JSON https://www.w3schools.com/python/python_json.asp
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
    # We will need a single job, that checks every hour if we have open jobs (with reminder tasks.)
    # Process reminder tasks as follows: 
    # 1. Perform API request to calculate reminder recipients
    # 2. Send Emails based on calculated recipients
    # 3. Summarize progress


    #
    # odk-mailer run command <hash>
    #

    # 1. check if job exists under <hash>
    # 2. get job details
    # 3. replace placeholder in message with data (python template engine)
    # 4. 

def list():

    with open(globals.odk_mailer_jobs, "r+") as f:
        jobs = json.load(f)

    utils.print_jobs(jobs)
    


