# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-07 10:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DID', '0012_auto_20171201_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='reason',
            field=models.TextField(blank=True, null=True),
        ),
    ]
