# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-08 07:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DID', '0013_auto_20171207_1023'),
    ]

    operations = [
        migrations.AddField(
            model_name='scorer',
            name='admin',
            field=models.BooleanField(default=False),
        ),
    ]
