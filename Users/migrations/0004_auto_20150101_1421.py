# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0003_auto_20150101_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='_date_joined',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 1, 8, 51, 16, 544677, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='_date_joined',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 1, 8, 51, 16, 544677, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
