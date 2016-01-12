# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0002_auto_20160104_2243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='summary',
            field=models.CharField(help_text=b"<span style='color:red'>*</span> Provide a one sentence summary of the issue", max_length=120, db_index=True),
        ),
        migrations.AlterField(
            model_name='notification',
            name='expiration_date',
            field=models.DateField(default=datetime.date(2016, 2, 4)),
        ),
    ]
