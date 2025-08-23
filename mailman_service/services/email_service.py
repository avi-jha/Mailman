from email.mime.text import MIMEText
import os
import logging
import smtplib
from django.conf import settings
from email.mime.multipart import MIMEMultipart
from mailman_service.models import MailmanUser

logger = logging.getLogger(__name__)

class EmailService:
    def __init__(self):
        pass
        
    def send_email(self, to_email, from_email, subject, body):
        try:
            import ipdb; ipdb.set_trace()
            logger.info(f"Sending email from {from_email} to {to_email}")
            msg = MIMEMultipart()
            msg['from'] = from_email
            msg['to'] = to_email
            msg['subject'] = subject
            msg.attach(MIMEText(body, 'plain'))

            # TODO: add check for email source
            server = smtplib.SMTP(settings.SMTP_SERVER, settings.SMTP_PORT)
            server.starttls()
            server.login(settings.SMTP_USERNAME, settings.SMTP_PASSWORD)
            server.send_message(msg)
            server.quit()
            logger.info(f"Email sent successfully to {to_email} from {from_email}")
            
        except Exception as e:
            logger.error(f"Error sending email: {str(e)}")
            raise Exception(f"Error sending email: {str(e)}")