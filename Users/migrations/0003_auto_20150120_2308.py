# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_auto_20150120_0100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='_date_joined',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 20, 17, 38, 29, 189414, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='_date_joined',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 20, 17, 38, 29, 189414, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
