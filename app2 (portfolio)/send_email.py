import smtplib, ssl
import os

def sendEmail(message):
    host = "smtp.gmail.com"
    port = 465
    username = "maamounchebbi@gmail.com"
    password = os.environ.get("MC_EMAIL_PASSWORD")
    
    receiver = "maamounchebbi@gmail.com"
    
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)