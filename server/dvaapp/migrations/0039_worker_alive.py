# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-23 07:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dvaapp', '0038_auto_20171022_0642'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker',
            name='alive',
            field=models.BooleanField(default=True),
        ),
    ]