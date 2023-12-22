from datetime import datetime
import time
import os
import typer
import csv
import re

class MailJob:
    def __init__(self, type: str):
        self.source_type = type
        self.source_path = ""
        self.email_field = ""
        self.data_fields = []
        self.createdAt = ""
        self.message = {}
        self.schedule_datetime = ""

        self.headers = []
        self.recipients = []


        self.init()

    def init(self):
        self.createdAt = int(time.time())

    def setSourcePath(self, path:str):

        # validate type: file
        if self.source_type == "file":
            # invalid file extension
            ext = os.path.splitext(path)[-1].lower()
            if not ext == ".csv":
                raise typer.Exit("Invalid file extension.")

            # invalid file path
            if not os.path.isfile(path):
                raise typer.Exit("Invalid file path.")
            
            self.source_path = path
            # read data
            with open(self.source_path, newline='') as f:
                reader = csv.DictReader(f, skipinitialspace=True)
                self.headers = reader.fieldnames
                for row in reader:
                    self.recipients.append(row)

    def setEmailField(self, email):
         # validate email field
        if email not in self.headers:
            raise typer.Exit("Invalid email_field. Terminating.")
        
        self.email_field = email

    def setDataFields(self, fields):
        # in case user enters data fields as comma separated string
        if type(fields) is str:
            # create list
            fields_list = list(filter(None, fields.split(",")))
            # filter all non-existing field names
            data_fields = list(filter(lambda x: x in self.headers, fields_list))

            if len(data_fields) < len(fields_list):
                typer.echo("Notice: On or more data field(s) were not found in the source.")                        

        elif type(fields) is list:
            data_fields = fields
        else:
            raise Exception("Invalid data fields type")
        
        self.data_fields = data_fields

    def setMessage(self, msg: str):
        message = msg.split(":")

        # validate message string 
        if len(message) != 4:
             raise typer.Exit("Invalid message string: [sender]:[format]:[source]:[content]")
        
        # validate message sender
        if not re.match(r"^\S+@\S+\.\S+$", message[0]) :
            raise typer.Exit("Invalid message sender. Use valid email address.")
        
        if message[1] not in ["txt", "html"]:
            raise typer.Exit("Invalid message format. Use either 'txt' or 'html.")
        
        if message[2] not in ["stdin", "path"]:
            raise typer.Exit("Invalid message source. Use either 'stdin' or 'path.")
        
        # add html validation if needed
        
        self.message = {
            "sender": message[0],
            "format": message[1],
            "source": message[2],
            "content": message[3]
        }

    # tbd: check UTC timezone behaviour and adjust accordingly
    def setSchedule(self, date_str):
        if date_str == "now":
            self.schedule_datetime = int(time.time())
        else: 
            #tbd date format validation
            # exit if not YYYY-DD-MM hh:mm
            _datetime = datetime.fromisoformat(date_str)
            self.schedule_datetime = int(datetime.timestamp(_datetime))

    def getSummary(self):
        typer.echo(self)
