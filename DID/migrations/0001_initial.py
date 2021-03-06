# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-09 21:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('is_service', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('clas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DID.Clas')),
            ],
        ),
        migrations.CreateModel(
            name='Scorer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('is_service', models.BooleanField()),
                ('clases', models.ManyToManyField(to='DID.Clas')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('full_score', models.IntegerField()),
                ('is_service', models.BooleanField()),
            ],
        ),
        migrations.AddField(
            model_name='scorer',
            name='subjects',
            field=models.ManyToManyField(to='DID.Subject'),
        ),
        migrations.AddField(
            model_name='record',
            name='scorer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DID.Scorer'),
        ),
        migrations.AddField(
            model_name='record',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DID.Subject'),
        ),
    ]
