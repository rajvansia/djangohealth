# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0010_myrolls'),
    ]

    operations = [
        migrations.AddField(
            model_name='myfamily',
            name='thisroll',
            field=models.ForeignKey(blank=True, to='profiles.Myrolls', null=True),
        ),
    ]
