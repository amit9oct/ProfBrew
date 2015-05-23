# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('SearchEngine', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='search',
            name='_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 5, 19, 33, 21, 537784, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
