# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0011_myfamily_thisroll'),
        ('measurements', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='calories',
            name='owner',
            field=models.ForeignKey(to='profiles.Profile', null=True),
        ),
        migrations.AddField(
            model_name='steps',
            name='owner',
            field=models.ForeignKey(to='profiles.Profile', null=True),
        ),
        migrations.AlterField(
            model_name='calories',
            name='deviceId',
            field=models.ForeignKey(to='devices.Devices', null=True),
        ),
        migrations.AlterField(
            model_name='steps',
            name='deviceId',
            field=models.ForeignKey(to='devices.Devices', null=True),
        ),
    ]
