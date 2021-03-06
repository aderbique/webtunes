# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-21 05:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webtunesapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='title',
            field=models.CharField(default='UN-NAMED', max_length=100),
        ),
        migrations.AlterField(
            model_name='entry',
            name='audio_file',
            field=models.FileField(default='NULL', upload_to='webtunesapp/files'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='set_to_expire',
            field=models.CharField(max_length=1),
        ),
    ]
