# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-21 06:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webtunesapp', '0002_auto_20170421_0559'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='title',
            new_name='file_name',
        ),
    ]
