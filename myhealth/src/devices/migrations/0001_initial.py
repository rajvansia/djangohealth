# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0011_myfamily_thisroll'),
    ]

    operations = [
        migrations.CreateModel(
            name='Devices',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('deviceType', models.CharField(max_length=30, null=True, blank=True)),
                ('dateAdded', models.DateField(default=datetime.datetime.now)),
                ('owner', models.ForeignKey(to='profiles.Profile', null=True)),
            ],
        ),
    ]
