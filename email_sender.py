import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
"""
Create an object of EmailMessage
"""
email = EmailMessage()
"""
Who sends the Email
"""
email['from'] ='John Doe'
"""
Email you want to send the message
"""
email['to'] = 'email@gmail.com'
email['subject'] = 'You won 1000000 dollars!'
"""
SetUp your html accordingly/Customized Email
"""
email.set_content(html.substitute(name : 'Random name'),'html')

"""
Send an email using imported library
"""

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    #smtp.ehlo()
    smtp.login('Your email goes here','password')
    smtp.send_message(email)
    print('All good boss!')
