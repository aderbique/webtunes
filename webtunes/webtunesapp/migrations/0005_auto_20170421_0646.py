# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-21 06:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webtunesapp', '0004_auto_20170421_0607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='audio_file',
            field=models.FileField(default='NULL', upload_to='webtunesapp/files/'),
        ),
    ]
