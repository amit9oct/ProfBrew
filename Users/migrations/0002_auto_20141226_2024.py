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
        migrations.RenameField(
            model_name='users',
            old_name='email',
            new_name='_email',
        ),
        migrations.RenameField(
            model_name='users',
            old_name='mobile_number',
            new_name='_mobile_number',
        ),
        migrations.RenameField(
            model_name='users',
            old_name='password',
            new_name='_password',
        ),
        migrations.RenameField(
            model_name='users',
            old_name='username',
            new_name='_username',
        ),
        migrations.RemoveField(
            model_name='users',
            name='date_joined',
        ),
        migrations.AddField(
            model_name='users',
            name='_date_joined',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 26, 14, 53, 56, 220066, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='users',
            name='user_type',
            field=models.IntegerField(default=3, choices=[(1, 'Student'), (2, 'Professor'), (3, 'Visitor')]),
            preserve_default=True,
        ),
    ]
