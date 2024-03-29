# Generated by Django 2.2.13 on 2020-06-30 17:47

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('end_date', models.DateField()),
                ('note', models.TextField(max_length=280)),
                ('adjunto', models.FileField(null=True, upload_to='adjuntos/')),
                ('task', models.BooleanField(default=False)),
                ('tag', models.CharField(max_length=280)),
                ('type', models.CharField(choices=[('BUG', 'Bug'), ('FEATURE', 'Feature'), ('WARNING', 'Warning')], max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
