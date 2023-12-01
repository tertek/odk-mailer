# ODK Mailer

*stil under development*

A simple CLI to send Mails for ODK.

Built with Typer and packaged with Poetry.

Building a Package - Guide: https://typer.tiangolo.com/tutorial/package/#create-your-app

## Features > commands

create a mail task
- [x] Read a recipients CSV list, validate input
- [x] Define field from available headers to be used for email sending, validate email addresses
- [ ] Read message from stdin or file as txt or html, support templating with format()
- [ ] Add reminders for a mail task

list mail tasks
- [ ] Show available mail tasks (that are stored in the local db)

edit mail tasks
- [ ] change or delete available mail tasks


show queue:
- [ ] see upcoming mail jobs

show logs
- [ ] see past mail jobs by status

check connection
- [ ] give instant feedback about connectivity to SMTP and API endpoints

## Development

```bash
    # clone the repo and cd into
    poetry shell
    poetry install
    # Run it with
    poetry run odk-mailer 
```

## Push to pypi

```
    poetry build
    poetry publish
```