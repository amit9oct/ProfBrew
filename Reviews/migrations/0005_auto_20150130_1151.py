# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Reviews', '0004_auto_20150130_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branchreviews',
            name='_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 30, 6, 21, 55, 73235, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='collegereviews',
            name='_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 30, 6, 21, 55, 73235, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='professorreviews',
            name='_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 30, 6, 21, 55, 73235, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
