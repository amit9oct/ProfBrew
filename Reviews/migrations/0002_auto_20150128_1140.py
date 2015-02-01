# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='branchreviews',
            name='_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 28, 6, 10, 15, 732364, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='collegereviews',
            name='_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 28, 6, 10, 15, 732364, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='professorreviews',
            name='_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 28, 6, 10, 15, 732364, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
