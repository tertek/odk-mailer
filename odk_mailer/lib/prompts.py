from inquirer import errors
import inquirer
import re
from odk_mailer.lib import validators

def source_type():
    questions = [
        inquirer.List('source_type', 
                    message="Select source type:",
                    choices= [
                        ("CSV file.", "file"),
                        ("ODK API", "api")
                    ],                      
                    carousel=True
        )
    ]
    return inquirer.prompt(questions, raise_keyboard_interrupt=True)

def source_path_file():
    # tbd: check if string is local file path or URL to remote CSV file in format https://*.<tld>/**/*.csv
    questions = [
        inquirer.Path('source_path_file',
                    message="Input local path to CSV file",
                    path_type=inquirer.Path.FILE,
                    exists=True,
                    normalize_to_absolute_path=True
        )
    ]
    return inquirer.prompt(questions, raise_keyboard_interrupt=True)

def email_field(headers=[]):
    questions = [
    inquirer.List('email_field',
                    message="What field should be used for sending emails?",
                    choices=headers,
                    default='email' if 'email' in headers else "",
                    carousel=True
                ),
    ]
    return inquirer.prompt(questions, raise_keyboard_interrupt=True)

def data_fields(headers=[]):
    questions = [
        inquirer.Checkbox("data_fields", 
                    message="Select data field(s)",
                    choices=headers
        )
    ]
    return inquirer.prompt(questions, raise_keyboard_interrupt=True)

def message():
    questions = [
        inquirer.Text('message_sender',
                      message="Input message sender",
                      default="odk@swisstph.ch"
                      #tbd: add email regex validation
        ),
        inquirer.List('message_format', 
                      message="Select message format:",
                      choices= [
                          ("Text", "txt"),
                          ("HTML", "html")
                          ],                      
                      carousel=True
        ),
        inquirer.List('message_source', 
                      message="Select message source:",
                      choices= [
                          ("Input as string", "stdin"),
                          ("File from path", "path")
                          ],                      
                      carousel=True
                      ),        
        inquirer.Text('message_content',
                      message="Input message string",
                      ignore=lambda x: x["message_source"] != "stdin"
        ),
        inquirer.Path('message_content',
                      message="Message file path",
                      ignore=lambda x: x["message_source"] != "path",
                      path_type=inquirer.Path.FILE,
                      exists=True,
                      normalize_to_absolute_path=True
        )
    ]
    return inquirer.prompt(questions, raise_keyboard_interrupt=True)

def schedule():
    questions = [
        inquirer.List('schedule_now',
                      message="Send immediately now or schedule for later?",
                      choices=[
                          ("Send now",True),
                          ("Schedule for later", False)
                      ]
        ),
        inquirer.Text('schedule_datetime',
                      message="Input schedule time and date",
                      ignore=lambda x: x["schedule_now"] == True,
                      validate= validators.date_format
        )
    ]

    return inquirer.prompt(questions, raise_keyboard_interrupt=True)

def confirm():
    return inquirer.prompt(
        [
            inquirer.Confirm("confirm", message="Create MailJob?")
        ], 
        raise_keyboard_interrupt=True)