from odk_mailer.lib import db
from email.mime.text import MIMEText
from smtplib import SMTP
import os

# return unformatted string instead of raising error
# when key is missing within dictionary
# https://stackoverflow.com/a/17215533/3127170
class SafeDict(dict):
    def __missing__(self, key):
        return '{' + key + '}' 
    

class Mailer:
    hash: str
    sender:str
    format: str
    content: str
    recipients: []

    subject: str
    body: str
    sender: str
    headers: str

    def __init__(self, id: str):
        self.hash = id
        
        job = db.getJob(self.hash)

        print(job)

        # get all relevant stuff here

    def send(self, dry=False):

        print(self.hash)
        print("================================================================")
        print("Sending emails..")

        # Set SMTP 
        # https://docs.python.org/3/library/smtplib.html#smtplib.SMTP_SSL
        # https://docs.python.org/3/library/email.examples.html#email-examples
        # required smtp parameters
        smtp_host = os.getenv('SMTP_HOST')
        smtp_port = os.getenv('SMTP_PORT')
        #smtp_username = os.getenv('SMTP_USERNAME')
        #smtp_password = os.getenv('SMTP_PASSWORD')

        for recipient in self.recipients:
            
            print(f"Sending mail to {recipient['email']}")
            text = self.content
            
            message = text.format_map(SafeDict(recipient))
            print(message)

            # send_mail()



            subject = "Email Subject"
            body = "This is the body of the text message"
            sender = "odk@swisspth.ch"
            recipient = "foo@bar.com"

            msg = MIMEText(body)
            msg['Subject'] = subject
            msg['From'] = sender

