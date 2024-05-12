from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.conf import settings
from enum import Enum


class Templates(Enum):
    AUTH_CODE = 'auth/auth_code.html'


class EmailService:
    @staticmethod
    def send_email(template, email_data):
        template = get_template(template.value)
        content = template.render(
            {
                'data': email_data['data']
            }
        )
        emailApp = EmailMultiAlternatives(
            email_data['subject'],
            email_data['text'],
            settings.EMAIL_HOST_USER,
            [email_data['to']]
        )
        emailApp.attach_alternative(content, 'text/html')
        try:
            emailApp.send()
        except Exception as e:
            raise e
