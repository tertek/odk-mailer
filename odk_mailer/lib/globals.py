import os
# https://stackoverflow.com/questions/24608665/how-to-store-python-application-data/24608746#24608746

odk_mailer_base = os.path.join(os.getenv("HOME"), ".odk-mailer")
odk_mailer_jobs = os.path.join(odk_mailer_base, "jobs.json")
odk_mailer_job = os.path.join(odk_mailer_base, "job")
#odk_mailer_path = os.path.expanduser('~') + "/.odk-mailer"