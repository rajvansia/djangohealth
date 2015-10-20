# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0009_auto_20151019_1903'),
    ]

    operations = [
        migrations.CreateModel(
            name='Myrolls',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('roll', models.CharField(max_length=30, null=True, blank=True)),
            ],
        ),
    ]
