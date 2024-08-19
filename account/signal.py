from django.db.models.signals import post_save 
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.template.loader import render_to_string
from account.utils import EmailSender


User = get_user_model()

@receiver(post_save, sender=User)
def send_registration_mail(sender, instance, created, **kwargs):
    if created:
        context = {'user':instance, 'mail_code':instance.verify_code}
        message = render_to_string('mails/account_verification.html', context)
        data = {
            'email_subject':'CAF | FOOD VERIFICATION',
            'email_body': message,
            'to_email':instance.email
        }
        EmailSender.send_email(data)
        
       