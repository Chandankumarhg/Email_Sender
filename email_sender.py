import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Chandan Kumar'
email['to'] = 'astaroth1528@gmail.com'
email['subject'] = 'You won 1,000,000 dollars'

email.set_content(html.substitute({'name':'Chandan'}),'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('astaroth1528@gmail.com', 'Your Password')
    smtp.send_message(email)
    print("all good boss")