import inquirer

def csv_file():
    questions = [
    inquirer.Path('csv_file',
                    message="Where is the recipients csv_file located?",
                    path_type=inquirer.Path.FILE,
                    exists=True
                    ),
    ]

    return inquirer.prompt(questions)["csv_file"]

def email_field(headers=[]):
    questions = [
    inquirer.List('email_field',
                    message="What field should be used for sending emails?",
                    choices=headers,
                    default='email' if 'email' in headers else "",
                    carousel=True
                ),
    ]
    return inquirer.prompt(questions)["email_field"]
