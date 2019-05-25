import smtplib

# setting up smtp server
s = smtplib.SMTP(host="smtp.office365.com",port=587)
s.starttls()
s.login("sthummala@centinasystems.com","Shanmukh@1996")

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

msg = MIMEMultipart()
Myemail = 'sthummala@centinasystems.com'
msg['From'] = Myemail
msg['To'] = Myemail
msg['Subject'] = 'This is test'

message = "This is also test"

msg.attach(MIMEText(message, 'plain'))

s.send_message(msg)

