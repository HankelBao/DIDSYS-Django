# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-10 03:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('DID', '0004_auto_20170810_0604'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='datetime',
        ),
        migrations.AddField(
            model_name='record',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]