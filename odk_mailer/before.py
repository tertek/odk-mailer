from pathlib import Path
from odk_mailer.lib import globals
import typer
import json

def init():
        
        jobs_dir = Path(globals.odk_mailer_job)
        jobs_dir.mkdir(parents=True, exist_ok=True)
        
        path_jobs = Path(globals.odk_mailer_jobs)

        # create jobs.json if not exists
        if not path_jobs.exists():
            path_jobs.touch()
            #jobs_db.write_text("Test")

        if path_jobs.stat().st_size == 0:
           path_jobs.write_text("[]")

        if not is_json(path_jobs.read_text()):
            raise typer.Exit("The jobs.json file is invalid JSON")

def is_json(myjson):
  try:
    json.loads(myjson)
  except ValueError as e:
    return False
  return True