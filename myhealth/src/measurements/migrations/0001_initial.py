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
            name='Calories',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('calories', models.DecimalField(null=True, max_digits=13, decimal_places=8, blank=True)),
                ('unit', models.CharField(max_length=30, null=True, blank=True)),
                ('dateAdded', models.DateField(default=datetime.datetime.now)),
                ('deviceId', models.ForeignKey(to='profiles.Profile', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Steps',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('steps', models.DecimalField(null=True, max_digits=13, decimal_places=8, blank=True)),
                ('unit', models.CharField(max_length=30, null=True, blank=True)),
                ('dateAdded', models.DateField(default=datetime.datetime.now)),
                ('deviceId', models.ForeignKey(to='profiles.Profile', null=True)),
            ],
        ),
    ]
