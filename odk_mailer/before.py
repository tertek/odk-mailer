from pathlib import Path
from odk_mailer.lib import globals
import typer
import json

def init():
        jobs_dir = Path(globals.odk_mailer_path + '/jobs')
        jobs_dir.mkdir(parents=True, exist_ok=True)
        
        jobs_db = Path(globals.odk_mailer_path + '/jobs.json')

        # create jobs.json if not exists
        if not jobs_db.exists():
            jobs_db.touch()
            #jobs_db.write_text("Test")

        if jobs_db.stat().st_size == 0:
           jobs_db.write_text("[]")

        if not is_json(jobs_db.read_text()):
            raise typer.Exit("Invalid JSON")    

def is_json(myjson):
  try:
    json.loads(myjson)
  except ValueError as e:
    return False
  return True