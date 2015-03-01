# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('University', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('_branch_name', models.CharField(max_length=100, null=True, default=None)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('course_name', models.CharField(max_length=200, default=None)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Prof_Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('priority', models.BigIntegerField(null=True)),
                ('position_name', models.CharField(max_length=100, default=None)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('_username', models.CharField(primary_key=True, default=None, max_length=200, serialize=False)),
                ('name', models.CharField(max_length=200, default=None)),
                ('_password', models.CharField(max_length=30, default=None)),
                ('user_type', models.IntegerField(choices=[(1, 'Student'), (2, 'Professor'), (3, 'Visitor')], default=3)),
                ('_email', models.EmailField(max_length=75, default=None)),
                ('_mobile_number', models.BigIntegerField(null=True)),
                ('_date_joined', models.DateTimeField(default=datetime.datetime(2015, 3, 1, 16, 29, 26, 587318, tzinfo=utc))),
                ('_ratings', models.BigIntegerField(default=None)),
                ('_area_of_interest', models.CharField(max_length=200, default=None)),
                ('_best_known_for', models.CharField(max_length=200, default=None)),
                ('_popular_name', models.CharField(max_length=200, default=None)),
                ('_branch', models.ForeignKey(to='Users.Branch', default=None)),
                ('_college', models.ForeignKey(to='University.College', default=None)),
                ('_courses_teaching', models.ManyToManyField(to='Users.Course')),
                ('_position', models.ManyToManyField(to='Users.Prof_Position')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Qualification_Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('qualification_name', models.CharField(max_length=200, default=None)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('_username', models.CharField(primary_key=True, default=None, max_length=200, serialize=False)),
                ('name', models.CharField(max_length=200, default=None)),
                ('_password', models.CharField(max_length=30, default=None)),
                ('user_type', models.IntegerField(choices=[(1, 'Student'), (2, 'Professor'), (3, 'Visitor')], default=3)),
                ('_email', models.EmailField(max_length=75, default=None)),
                ('_mobile_number', models.BigIntegerField(null=True)),
                ('_date_joined', models.DateTimeField(default=datetime.datetime(2015, 3, 1, 16, 29, 26, 587318, tzinfo=utc))),
                ('_year', models.IntegerField(choices=[(0, 'Other'), (1, 'First Year'), (2, 'Second Year'), (3, 'Third Year'), (4, 'Fourth Year'), (5, 'Fifth Year')], default=0)),
                ('_contributing_factor', models.BigIntegerField(default=None)),
                ('_degree_pursued', models.CharField(max_length=100, default=None)),
                ('_branch', models.ForeignKey(to='Users.Branch', default=None)),
                ('_college', models.ForeignKey(to='University.College', default=None)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='professor',
            name='_qualifications',
            field=models.ManyToManyField(to='Users.Qualification_Type'),
            preserve_default=True,
        ),
    ]
