# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-07 12:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DID', '0010_record_reason'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clas',
            name='day_total',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='clas',
            name='is_service',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='clas',
            name='month_total',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='clas',
            name='semister_total',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='clas',
            name='week_total',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='scorer',
            name='is_service',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='subject',
            name='full_score',
            field=models.IntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='subject',
            name='is_service',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='subject',
            name='weeky',
            field=models.BooleanField(default=False),
        ),
    ]