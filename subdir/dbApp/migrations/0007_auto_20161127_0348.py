# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-27 03:48
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dbApp', '0006_auto_20161126_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albums',
            name='copyrightdate',
            field=models.DateField(default=datetime.datetime(2016, 11, 27, 3, 48, 19, 939103, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='instruments',
            name='key',
            field=models.CharField(choices=[('Ab', 'A Flat'), ('A', 'A'), ('A#', 'A Sharp'), ('Bb', 'B Flat'), ('B', 'B'), ('C', 'C'), ('C#', 'C Sharp'), ('Db', 'D Flat'), ('D', 'D'), ('D#', 'D Sharp'), ('Eb', 'E Flat'), ('E', 'E'), ('F', 'F'), ('F#', 'F Sharp'), ('Gb', 'G Flat'), ('G', 'G'), ('G#', 'G Sharp')], default='Bb', max_length=2),
        ),
    ]