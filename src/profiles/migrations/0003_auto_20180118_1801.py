# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-18 18:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_profiles_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiles',
            name='description',
            field=models.TextField(default='Description default text'),
        ),
    ]
