# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-28 17:19
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dbApp', '0011_auto_20161128_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albums',
            name='copyrightdate',
            field=models.DateField(default=datetime.datetime(2016, 11, 28, 17, 19, 53, 400681, tzinfo=utc)),
        ),
    ]
