# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Reviews', '0006_auto_20150130_2250'),
    ]

    operations = [
        migrations.RenameField(
            model_name='professorreviewlikes',
            old_name='_like',
            new_name='_liked',
        ),
        migrations.AlterField(
            model_name='branchreviews',
            name='_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 30, 17, 21, 9, 439034, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='collegereviews',
            name='_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 30, 17, 21, 9, 439034, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='professorreviews',
            name='_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 30, 17, 21, 9, 439034, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
