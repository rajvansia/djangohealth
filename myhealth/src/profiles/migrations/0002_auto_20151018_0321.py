# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='birthday',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='is_parent',
            field=models.BooleanField(default=False),
        ),
    ]
