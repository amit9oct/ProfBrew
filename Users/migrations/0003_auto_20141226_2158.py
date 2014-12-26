# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_auto_20141226_2024'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('users_ptr', models.OneToOneField(to='Users.Users', serialize=False, parent_link=True, auto_created=True, primary_key=True)),
                ('_contributing_factor', models.BigIntegerField(default=None)),
                ('_university', models.CharField(max_length=100, default=None)),
                ('_college', models.CharField(max_length=100, default=None)),
                ('_degree_pursued', models.CharField(max_length=100, default=None)),
                ('_discipline', models.CharField(max_length=100, default=None)),
            ],
            options={
            },
            bases=('Users.users',),
        ),
        migrations.AlterField(
            model_name='users',
            name='_date_joined',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 26, 16, 28, 30, 587815, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
