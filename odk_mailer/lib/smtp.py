from email.message import EmailMessage
import smtplib

def send_mail(subject, sender, recipient, message, type='plain'):

    smtp_host = 'smtp.freesmtpservers.com'
    smtp_port = 25
    smtp_username = ''
    smtp_password = ''

    email = EmailMessage()
    email['Subject'] = subject
    email['From'] = sender
    email['To'] = recipient
    email.set_content(message, subtype=type)

    try:
        smtp = smtplib.SMTP(timeout=5)
        smtp.set_debuglevel(2)
        smtp.connect(smtp_host, smtp_port)
        smtp.send_message(email)
        smtp.quit()
        print("Successfully sent email to " + email["To"])
    except Exception as error:
        print(error)
