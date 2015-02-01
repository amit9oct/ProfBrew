# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('SearchEngine', '0007_auto_20150130_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='search',
            name='_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 30, 17, 37, 17, 553512, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
