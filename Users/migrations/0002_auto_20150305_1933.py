# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='_date_joined',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 5, 19, 33, 21, 522573, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='_date_joined',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 5, 19, 33, 21, 522573, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
