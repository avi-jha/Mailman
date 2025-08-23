from django.db import models
from django.contrib.auth.models import AbstractUser

class MailmanUser(AbstractUser):
    """
    Custom user model for Mailman.
    """
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.email
    

class ApiKey(models.Model):
    """
    Model to store API keys for Mailman
    """
    user = models.ForeignKey(MailmanUser, on_delete=models.CASCADE)
    key = models.CharField(max_length=500, unique=True)
    last_used = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Api key {self.key} for {self.user}"
    
    def generate_key(self):
        import secrets
        from django.utils import timezone
        self.key = secrets.token_urlsafe(32)
        self.is_active = True
        self.created = timezone.now()   
        self.save()
        return self.key

class EmailLog(models.Model):
    user = models.ForeignKey(MailmanUser, on_delete=models.CASCADE)
    to_address = models.EmailField()
    from_address = models.EmailField()
    subject = models.CharField(max_length=256)
    body = models.TextField()
    template = models.CharField(max_length=256, null=True, blank=True)
    params = models.JSONField(null=True, blank=True)
    status = models.CharField(
        max_length=32,
        choices=[
            ('success', 'Success'),
            ('failed', 'Failed'),
            ('pending', 'Pending'),
        ],
        default='pending'
    )
    error_message = models.CharField(max_length=100, null=True, blank=True)
    provider = models.CharField(max_length=100, null=True, blank=True)
    sent_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Email sent to {self.to_address} from {self.from_address} with status {self.status} at {self.sent_at}"