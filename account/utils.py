from django.contrib.auth import get_user_model
from django.template.loader import render_to_string
from django.contrib import messages
from django.core.mail import EmailMessage
from django.shortcuts import get_object_or_404
import string
import random

User = get_user_model()

class EmailSender:
    def send_email(self, data):
        email = EmailMessage(
            subject    = data['email_subject'],
            body       = data['email_body'],
            to         = [data['to_email']],
        )
        email.content_subtype = 'html'
        email.send()


    def send_email_verification_code(self, user):
        context = {'username':user.username, 'mail_code':user.verify_code}
        message = render_to_string('mails/account_verification.html', context)
        data = {
            'email_subject':'Pharmative Password Reset Code',
            'email_body': message,
            'to_email':user.email
            }
        self.send_email(data)

    def send_account_registration_mail(self, user):
        context = {'username':user.username}
        message = render_to_string('mails/account_verification.html', context)
        data = {
            'email_subject':'Pharmative Password Reset Code',
            'email_body': message,
            'to_email':user.email
            }
        self.send_email(data)

    def send_notification_email(self, email):
        context = {'email':email}
        message = render_to_string('mails/notification.html', context)
        data = {
            'email_subject':'Pharmative',
            'email_body': message,
            'to_email':email
            }
        self.send_email(data)
    
    def send_congratulation(self, user):
        context = {'user':user}
        message = render_to_string('mails/register_mail.html', context)
        data = {
            'email_subject':'Pharmative',
            'email_body': message,
            'to_email':user.email
            }
        self.send_email(data)



def send_customer_verify_code(email):
    user = User.objects.get(email=email)
    mail_code = user.verify_code
    context = {'username':user.username, 'mail_code':mail_code}
    message = render_to_string('mails/account_verification.html', context)
    data = {
        'email_subject':'Pharmative Email Verification',
        'email_body': message,
        'to_email':email
        }
    EmailSender().send_email(data)


def check_user_status(email) -> bool:
    if User.objects.filter(email=email, is_admin=True):
        return True
    else:
        return False