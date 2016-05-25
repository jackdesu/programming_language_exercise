import smtplib

message = """From: From Person <xxx@gmail.com>
To: To Person <xxx@gmail.com>
MIME-Version: 1.0
Content-type: text/html
Subject: SMTP HTML e-mail test

This is an e-mail message to be sent in HTML format

<b>This is HTML message.</b>
<h1>This is headline.</h1>
"""

try:
    account = ""
    password = ""
    sender = ""
    receiver = ""
    smtpObj = smtplib.SMTP('smtp.gmail.com:587')
    smtpObj.starttls()
    smtpObj.login(account, password)
    smtpObj.sendmail(receiver, sender, message)
    smtpObj.close()
    print("Successfully sent email")
except smtplib.SMTPException:
    print("Error: unable to send email")
