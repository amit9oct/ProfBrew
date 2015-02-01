# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('SearchEngine', '0005_auto_20150130_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='search',
            name='_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 30, 17, 20, 34, 848675, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
