# sample code from here - https://mailtrap.io/blog/python-send-email-gmail/
# uses Andrew Beatty's test account

import smtplib
from email.mime.text import MIMEText

subject = "Email Subject"
body = "This is the body of the text message"
sender = "sender@gmail.com"
recipients = ["recipient1@gmail.com", "recipient2@gmail.com"]
password = "password"


def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
       smtp_server.login(sender, password)
       smtp_server.sendmail(sender, recipients, msg.as_string())
    print("Message sent!")
subject = "Email Subject"
body = "This is the body of the test message"
sender = "andrewbeattycourse@gmail.com"
recipients = ["dvdgeroconnell@gmail.com"]
# password = "notS3cure"
password = "cnkk mvam lcbj sknl"
send_email(subject, body, sender, recipients, password)