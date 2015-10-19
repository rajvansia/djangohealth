# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20151018_1421'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='child',
            name='id',
        ),
        migrations.AlterField(
            model_name='child',
            name='child',
            field=models.ForeignKey(primary_key=True, serialize=False, to='profiles.Profile'),
        ),
    ]
