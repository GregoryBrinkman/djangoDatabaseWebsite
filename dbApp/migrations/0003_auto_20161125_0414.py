# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-25 04:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dbApp', '0002_auto_20161124_2216'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='albums',
            name='producer',
        ),
        migrations.RemoveField(
            model_name='appearson',
            name='song',
        ),
        migrations.RemoveField(
            model_name='musicians',
            name='address',
        ),
        migrations.RemoveField(
            model_name='performs',
            name='musician',
        ),
        migrations.RemoveField(
            model_name='performs',
            name='song',
        ),
        migrations.RemoveField(
            model_name='plays',
            name='instrument',
        ),
        migrations.RemoveField(
            model_name='plays',
            name='musician',
        ),
        migrations.DeleteModel(
            name='Address',
        ),
        migrations.DeleteModel(
            name='Albums',
        ),
        migrations.DeleteModel(
            name='AppearsOn',
        ),
        migrations.DeleteModel(
            name='Instruments',
        ),
        migrations.DeleteModel(
            name='Musicians',
        ),
        migrations.DeleteModel(
            name='Performs',
        ),
        migrations.DeleteModel(
            name='Plays',
        ),
        migrations.DeleteModel(
            name='Songs',
        ),
    ]
