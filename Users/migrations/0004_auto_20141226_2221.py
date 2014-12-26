# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0003_auto_20141226_2158'),
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('users_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='Users.Users')),
                ('_ratings', models.BigIntegerField(default=None)),
                ('_university', models.CharField(default=None, max_length=100)),
                ('_college', models.CharField(default=None, max_length=100)),
                ('_qualifications', models.CharField(default=None, max_length=200)),
                ('_area_of_interest', models.CharField(default=None, max_length=200)),
                ('_courses_teaching', models.CharField(default=None, max_length=200)),
                ('_best_known_for', models.CharField(default=None, max_length=200)),
                ('_popular_name', models.CharField(default=None, max_length=200)),
            ],
            options={
            },
            bases=('Users.users',),
        ),
        migrations.AlterField(
            model_name='users',
            name='_date_joined',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 26, 16, 51, 59, 268249, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
