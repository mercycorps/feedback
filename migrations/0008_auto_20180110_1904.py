# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-10 19:04
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0007_auto_20171004_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='expiration_date',
            field=models.DateField(default=datetime.date(2018, 2, 9)),
        ),
    ]
