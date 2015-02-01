# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0007_auto_20150130_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='_date_joined',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 30, 17, 37, 17, 522258, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='_date_joined',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 30, 17, 37, 17, 522258, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
