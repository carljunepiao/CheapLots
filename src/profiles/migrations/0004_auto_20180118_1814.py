# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-18 18:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20180118_1801'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='profiles',
            new_name='profile',
        ),
    ]
