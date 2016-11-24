# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-24 20:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_pregnancy_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='blood_type',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AddField(
            model_name='client',
            name='bmi',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='client',
            name='dob',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='client',
            name='gp',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='client',
            name='gp_tel',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AddField(
            model_name='client',
            name='haemoglobin',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='client',
            name='hospital',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='client',
            name='parity',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='client',
            name='prev_pregs',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='client',
            name='serology',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='client',
            name='weight',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='pregnancy',
            name='consultant_clinic',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='pregnancy',
            name='placental_site',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='pregnancy',
            name='public_health_nurse',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='client',
            name='notes',
            field=models.TextField(default='Enter notes'),
        ),
        migrations.AlterField(
            model_name='pregnancy',
            name='notes',
            field=models.TextField(default='Enter notes'),
        ),
    ]
