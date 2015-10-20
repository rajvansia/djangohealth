# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_myid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Myfamily',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('myrelation', models.ForeignKey(to='profiles.Profile')),
                ('myself', models.ForeignKey(to='profiles.myid')),
            ],
        ),
    ]
