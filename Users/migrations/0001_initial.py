# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('University', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('_username', models.CharField(default=None, primary_key=True, serialize=False, max_length=15)),
                ('name', models.CharField(default=None, max_length=200)),
                ('_password', models.CharField(default=None, max_length=30)),
                ('user_type', models.IntegerField(default=3, choices=[(1, 'Student'), (2, 'Professor'), (3, 'Visitor')])),
                ('_email', models.EmailField(default=None, max_length=75)),
                ('_mobile_number', models.BigIntegerField(null=True)),
                ('_date_joined', models.DateTimeField(default=datetime.datetime(2015, 1, 1, 8, 17, 21, 139092, tzinfo=utc))),
                ('_ratings', models.BigIntegerField(default=None)),
                ('_qualifications', models.CharField(default=None, max_length=200)),
                ('_area_of_interest', models.CharField(default=None, max_length=200)),
                ('_courses_teaching', models.CharField(default=None, max_length=200)),
                ('_best_known_for', models.CharField(default=None, max_length=200)),
                ('_popular_name', models.CharField(default=None, max_length=200)),
                ('_college', models.ForeignKey(to='University.College', default=None)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('_username', models.CharField(default=None, primary_key=True, serialize=False, max_length=15)),
                ('name', models.CharField(default=None, max_length=200)),
                ('_password', models.CharField(default=None, max_length=30)),
                ('user_type', models.IntegerField(default=3, choices=[(1, 'Student'), (2, 'Professor'), (3, 'Visitor')])),
                ('_email', models.EmailField(default=None, max_length=75)),
                ('_mobile_number', models.BigIntegerField(null=True)),
                ('_date_joined', models.DateTimeField(default=datetime.datetime(2015, 1, 1, 8, 17, 21, 139092, tzinfo=utc))),
                ('_contributing_factor', models.BigIntegerField(default=None)),
                ('_degree_pursued', models.CharField(default=None, max_length=100)),
                ('_discipline', models.CharField(default=None, max_length=100)),
                ('_college', models.ForeignKey(to='University.College', default=None)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
