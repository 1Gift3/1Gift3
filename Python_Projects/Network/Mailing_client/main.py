import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart




server = smtplib.SMTP('smtp.gmail.com', 25)

server.ehlo()
# encrypted txt password file for this use
with open('password.txt', 'r') as f:
    password = f.read()

server.login('joshuaramaoka@gmail.com', password)

msg = MIMEMultipart()
msg['From'] = 'Joshua'
msg['To'] = 'sigmedia03@gmail.com'
msg['Subject'] = 'Just A Test'

with open('message.text', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))    

filename = 'proxy-image.jpg'
attachment = open(filename, 'rb')

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; filename={filename}')
msg.attach(p)

text = msg.as_string()
server.sendmail('joshuaramaoka@gmail.com', 'sigmedia03@gmail.com', text)

# not first  but i need an encrypted txt file containing my josh password
# check also ssmpt if im correct to get instructions

