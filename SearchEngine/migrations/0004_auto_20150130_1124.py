# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('SearchEngine', '0003_auto_20150130_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='search',
            name='_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 30, 5, 54, 37, 515815, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
