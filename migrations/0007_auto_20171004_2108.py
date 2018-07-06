# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0006_auto_20160510_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='expiration_date',
            field=models.DateField(default=datetime.date(2017, 11, 3)),
        ),
    ]
