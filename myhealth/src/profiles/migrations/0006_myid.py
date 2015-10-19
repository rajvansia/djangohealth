# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_auto_20151018_1459'),
    ]

    operations = [
        migrations.CreateModel(
            name='myid',
            fields=[
                ('my_id', models.ForeignKey(primary_key=True, serialize=False, to='profiles.Profile')),
            ],
        ),
    ]
