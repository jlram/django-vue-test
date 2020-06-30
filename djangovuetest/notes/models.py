from datetime import datetime

from django.contrib.auth.models import User
from django.db import models

TIPO_CHOICES = (
    ('BUG', "Bug"),
    ('FEATURE', "Feature"),
    ('WARNING', "Warning"),
)


class Note(models.Model):
    date = models.DateField(null=False, default=datetime.now)
    end_date = models.DateField()
    note = models.TextField(max_length=280)
    adjunto = models.FileField(upload_to='adjuntos/', null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    task = models.BooleanField(default=False)
    tag = models.CharField(max_length=280)
    type = models.CharField(choices=TIPO_CHOICES, max_length=50)
