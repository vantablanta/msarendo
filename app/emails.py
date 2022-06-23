from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_welcome_email(username,receiver):
    # Creating message subject and sender
    subject = 'Welcome to Msarendo'
    sender = 'michellenjeri54@gmail.com'

    #passing in the context vairables
    text_content = render_to_string('email/welcome.txt',{"username": username})
    html_content = render_to_string('email/welcome.html',{"username": username})

    msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()


def send_new_applicant_email(username,receiver):
    # Creating message subject and sender
    subject = 'You have a new application pending your review'
    sender = 'michellenjeri54@gmail.com'

    #passing in the context vairables
    text_content = render_to_string('email/welcome.txt',{"username": username})
    html_content = render_to_string('email/welcome.html',{"username": username})

    msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()

