# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-09 22:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DID', '0003_scorer_score'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scorer',
            name='score',
        ),
        migrations.AddField(
            model_name='record',
            name='score',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
