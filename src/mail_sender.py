import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


email_user = 'contact.launch.hub@gmail.com' # Sender's email
email_password = 'Get.Pass.456' # Sender's password. ENVIRONMENTAL VARIABLE RECOMMENDED, NEVER PUSH PASSWORDS TO GIT.
email_send = 'contact.launch.hub@gmail.com' # Recipient's email


def msg_builder(name, email, message):
    return "New message from: [ " + name + " ] < " + email + " > \n\n\n" + message


def sendmail(main):
    subject = "Launch hub has received a New Message!"
    body = main
    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_send
    msg['Subject'] = subject
    msg.attach(MIMEText(body,'plain'))
    text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(email_user,email_password)
    server.sendmail(email_user,email_send,text)
    server.quit()
