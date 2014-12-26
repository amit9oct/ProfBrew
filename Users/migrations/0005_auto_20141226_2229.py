# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0004_auto_20141226_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='_date_joined',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 26, 16, 59, 23, 324382, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='users',
            name='_mobile_number',
            field=models.BigIntegerField(null=True),
            preserve_default=True,
        ),
    ]
