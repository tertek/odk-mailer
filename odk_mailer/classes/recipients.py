import typer
import os
import csv
from collections import defaultdict

# return unformatted string instead of raising error
# when key is missing within dictionary
# https://stackoverflow.com/a/17215533/3127170
class SafeDict(dict):
    def __missing__(self, key):
        return '{' + key + '}'

class Recipients:
    def __init__(self, path):
        self.path  = path
        self.fieldnames = []
        self.data = []

        self.init()

    def init(self):

        # invalid file extension
        ext = os.path.splitext(self.path)[-1].lower()
        if not ext == ".csv":
            raise typer.Exit("Invalid file extension.")

        # invalid file path
        if not os.path.isfile(self.path):
            raise typer.Exit("Invalid file path.")

        # read data
        with open(self.path, newline='') as f:
            reader = csv.DictReader(f, skipinitialspace=True)
            self.fieldnames = reader.fieldnames
            for row in reader:
                self.data.append(row)

    def validate_email(self, email_field):
        invalid_emails = []
        valid = False
        total = 0

        print("\nValidating recipients...")
        with typer.progressbar(emails) as progress:
            for row in progress:
                total += 1
                email = row[field]
                try:
                    if not email:
                        raise EmailNotValidError("Email address missing. Check for missing delimiters (',') in your CSV file.")
                    validate_email(email)
                except EmailNotValidError as e:
                    invalid = [str(total) ,email, str(e)]
                    invalid_emails.append(invalid)
                
        print(f"Validated {total} entries.\n")
        
        if len(invalid_emails) == 0:
            valid = True
        
        return valid, invalid_emails

    def test(self):
        print(self.fieldnames)
        print(f'file path is {self.path}')
        
        txt = "The firstname is {firstname}\n lastname is {lastname} \n email is {email} \n not filled {not_filled}"
        for row in self.data:
            print(txt.format_map(SafeDict(row)))