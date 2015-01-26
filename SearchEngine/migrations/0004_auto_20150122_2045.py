# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('SearchEngine', '0003_auto_20150120_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='search',
            name='_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 22, 15, 15, 52, 479954, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
