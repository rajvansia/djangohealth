# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_auto_20151019_1859'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myfamily',
            name='thisroll',
        ),
        migrations.DeleteModel(
            name='Myrolls',
        ),
    ]
