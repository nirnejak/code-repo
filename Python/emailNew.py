import os
import sendgrid
from sendgrid.helpers.mail import *

sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('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'))
from_email = Email('info@destinationsofnewyorkstate.com')
to_email = Email('yogesh@inkoop.in')
subject = "Welcome to Destinations of New York State"
content = Content("text/html", '<h1>EMAIL_BODY</h1>')
mail = Mail(from_email, subject, to_email, content)
response = sg.client.mail.send.post(request_body=mail.get())
print(response.status_code)
print(response.body)
print(response.headers)
