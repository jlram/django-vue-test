import datetime

from django.contrib.auth.models import User
from django.db import models

TIPO_CHOICES = (
    ('BUG', "Bug"),
    ('FEATURE', "Feature"),
    ('WARNING', "Warning"),
)


class Note(models.Model):
    date = models.DateField(null=False, default=datetime.date.today)
    end_date = models.DateField(default=datetime.date.today)
    note = models.TextField(max_length=280, null=False)
    adjunto = models.FileField(upload_to='adjuntos/', null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user', null=False)
    task = models.BooleanField(default=False)
    tag = models.CharField(max_length=280, null=False)
    type = models.CharField(choices=TIPO_CHOICES, max_length=50, null=False)

    def __str__(self):
        return str(self.id) + ' Nota ' + str(self.user) + ' ' + str(self.date)

