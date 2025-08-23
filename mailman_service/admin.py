from django.contrib import admin
from .models import MailmanUser, ApiKey, EmailLog

admin.site.register(MailmanUser)
admin.site.register(ApiKey)
admin.site.register(EmailLog)
