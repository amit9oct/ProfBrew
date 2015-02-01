# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Reviews', '0007_auto_20150130_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branchreviews',
            name='_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 30, 17, 37, 17, 584759, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='collegereviews',
            name='_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 30, 17, 37, 17, 584759, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='professorreviews',
            name='_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 30, 17, 37, 17, 584759, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
