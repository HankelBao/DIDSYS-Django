# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-10 21:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DID', '0006_auto_20170811_0527'),
    ]

    operations = [
        migrations.AddField(
            model_name='clas',
            name='register_year',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
