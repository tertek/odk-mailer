from odk_mailer.lib import globals
from datetime import datetime
import time
import json
import hashlib
from enum import Enum

class JobType(Enum):
    FILE = 'file'
    API = 'api'

class Source:
    type: str
    path: str
    project: int
    hostname: str
    username: str
    password: str

    def __init__(self, lst: []):
        if not len(lst) in [2,6]:
            raise Exception("Source input must have length 2 or 6.")
        
        self.type = JobType(lst[0]).value
        self.path = lst[1]
        if len(lst) == 6:
            self.project = int(lst[2])
            self.hostname = lst[3]
            self.username = lst[4]
            self.password = lst[5]

class Fields:
    email: str
    data: []

    def __init__(self, lst: []):
        if not len(lst) in [1,2]:
            raise Exception("Fields input must have length 1 or 2.")
        
        self.email = lst[0]
        # data fields are optional
        if len(lst) == 2:
            self.data = lst[1].split(",")

class Message:
    sender: str
    format: str
    source: str
    content: str

    def __init__(self, lst: []):
        if not len(lst) == 4:
            raise Exception("Message input must have length 4.")
                
        self.sender = lst[0]
        self.format = lst[1]
        self.source = lst[2]
        self.content = lst[3]        

class Schedule:
    timestamp: int

    def __init__(self,int:int):
        self.timestamp = int

class Job:
    """Job class"""
    def __init__(self, type: str):

        self.created = int(time.time())
        self.source = {
            "type": type,
            "path": ""
        }
        self.raw = {
            "headers": [],
            "data": []
        },
        self.headers = []
        self.recipients = []
        self.fields = {
            "email": "",
            "data": []
        } 
        self.message = {}
        self.scheduled = ""

    # def setSourcePath(self, path:str):

    #     # validate type: file
    #     if self.source["type"] == "file":
    #         # invalid file extension
    #         ext = os.path.splitext(path)[-1].lower()
    #         if not ext == ".csv":
    #             raise typer.Exit("Invalid file extension.")
    #         # invalid file path
    #         if not os.path.isfile(path):
    #             raise typer.Exit("Invalid file path.")
            
    #         self.source["path"] = path
    #         # read data and set headers and recipients
    #         with open(self.source["path"], newline='') as f:
    #             reader = csv.DictReader(f, skipinitialspace=True)
    #             self.headers = reader.fieldnames
    #             for row in reader:
    #                 self.recipients.append(row)

    # def setEmailField(self, email):
    #      # validate email field
    #     if email not in self.headers:
    #         raise typer.Exit("Invalid email_field. Terminating.")
        
    #     self.fields["email"] = email

    # def setDataFields(self, fields):
    #     # in case user enters data fields as comma separated string
    #     if type(fields) is str:
    #         # create list
    #         fields_list = list(filter(None, fields.split(",")))
    #         # filter all non-existing field names
    #         data_fields = list(filter(lambda x: x in self.headers, fields_list))

    #         if len(data_fields) < len(fields_list):
    #             typer.echo("Notice: On or more data field(s) were not found in the source.")                        

    #     elif type(fields) is list:
    #         data_fields = fields
    #     else:
    #         raise Exception("Invalid data fields type")
        
    #     self.fields["data"] = data_fields

    # def setMessage(self, msg: str):
    #     message = msg.split(":")

    #     # validate message string 
    #     if len(message) != 4:
    #          raise typer.Exit("Invalid message string: [sender]::[format]::[source]::[content]")
        
    #     # validate message sender
    #     if not re.match(r"^\S+@\S+\.\S+$", message[0]) :
    #         raise typer.Exit("Invalid message sender. Use valid email address.")
        
    #     if message[1] not in ["txt", "html"]:
    #         raise typer.Exit("Invalid message format. Use either 'txt' or 'html.")
        
    #     if message[2] not in ["stdin", "path"]:
    #         raise typer.Exit("Invalid message source. Use either 'stdin' or 'path.")
        
    #     # add html validation if needed
        
    #     self.message = {
    #         "sender": message[0],
    #         "format": message[1],
    #         "source": message[2],
    #         "content": message[3]
    #     }

    # # tbd: check UTC timezone behaviour and adjust accordingly
    # # tbd: check if scheduled time is in future 
    # def setSchedule(self, date_str):
    #     if date_str == "now":
    #         self.scheduled = self.created
    #     else: 
    #         # tbd: date format validation
    #         # exit if not YYYY-DD-MM hh:mm
    #         _datetime = datetime.fromisoformat(date_str)
    #         self.scheduled = int(datetime.timestamp(_datetime))


    def getSummary(self):
        return {
            "created": self.created,
            "scheduled": self.scheduled,
            "source": self.source,
            "fields": self.fields,
            "message": self.message,
            "recipients": self.recipients            
        }

    # does two things: saves mailjob as <hash>.json and adds it as an entry to jobs.json with hash as id
    def save(self):
        jobs_path = globals.odk_mailer_path + '/jobs'
        jobs_file = globals.odk_mailer_path + '/jobs.json'

        # get content as json
        content = json.dumps(self.getSummary(), ensure_ascii=True, indent=4)
        hash = hashlib.sha256(content.encode()).hexdigest()

        with open(jobs_path + '/'+hash+'.json', 'w', encoding='utf-8') as f:
            f.write(content)

        # with open(jobs_file, "r+") as json_file:
        #     print(json_file.read())

        with open(jobs_file, "r+") as json_file:
            jobs = json.load(json_file)
            jobs.append({
                "hash": hash,
                "scheduled": self.scheduled, 
                "created": self.created,
                "state":0
            })
            json_file.seek(0)
            json_file.truncate()
            json_file.write(json.dumps(jobs))

        print("Success")

        # we want to add an entry to jobs.json: 
        # therefore we have to 1) read the file into an object
        # add an element to the object
        # object format: [{hash, scheduled, state, last_checked},{}.{}]

        # write into jobs.json > id, scheduled, state        

        
        


    def saveJSON(self):

        path = globals.odk_mailer_path + '/jobs'
        content = json.dumps(self.getSummary(), ensure_ascii=False, indent=4)
        hash = hashlib.sha256(content.encode('utf-8')).hexdigest()

        with open(path + '/'+hash+'.json', 'w', encoding='utf-8') as f:
            f.write(content)
            
