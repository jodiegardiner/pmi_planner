# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-23 12:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20161117_2220'),
    ]

    operations = [
        migrations.AddField(
            model_name='pregnancy',
            name='notes',
            field=models.TextField(blank=True),
        ),
    ]