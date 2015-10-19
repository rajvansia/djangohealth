# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20151018_1456'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parent',
            name='id',
        ),
        migrations.AlterField(
            model_name='parent',
            name='parent',
            field=models.ForeignKey(primary_key=True, serialize=False, to='profiles.Profile'),
        ),
    ]
