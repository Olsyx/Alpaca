# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-22 15:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Alpaca', '0010_auto_20161122_1343'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='emails_are_sent',
            field=models.BooleanField(default=False),
        ),
    ]