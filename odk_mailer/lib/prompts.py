from inquirer import errors
import inquirer
import re

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
    # check if string is local file path or URL to remote CSV file in format https://*.<tld>/**/*.csv
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

def validation_schedule_date(_, current):
    # valdidate format
    re_YYYY_MM_DD_hh_mm = "[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1]) (2[0-3]|[01][0-9]):[0-5][0-9]"
    if not re.search(re_YYYY_MM_DD_hh_mm, current):
        raise errors.ValidationError('', 'Invalid date format. Has to be YYYY-MM-DD hh:mm')
       
    return True
    


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
                      validate= validation_schedule_date
        )
    ]

    return inquirer.prompt(questions, raise_keyboard_interrupt=True)


# def csv_file():
#     questions = [
#     inquirer.Path('csv_file',
#                     message="Where is the recipients csv_file located?",
#                     path_type=inquirer.Path.FILE,
#                     exists=True
#                     ),
#     ]

#     return inquirer.prompt(questions)