# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-24 20:36
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('threads', '0002_auto_20161123_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 24, 20, 36, 28, 620000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='thread',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 24, 20, 36, 28, 619000, tzinfo=utc)),
        ),
    ]
