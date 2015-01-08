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
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('_branch_name', models.CharField(max_length=100, null=True, default=None)),
                ('_job_satisifaction', models.IntegerField(default=None, null=True)),
                ('_research_opportunities', models.IntegerField(default=None, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('course_name', models.CharField(max_length=200, default=None)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Prof_Position',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
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
                ('_username', models.CharField(max_length=15, default=None, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200, default=None)),
                ('_password', models.CharField(max_length=30, default=None)),
                ('user_type', models.IntegerField(default=3, choices=[(1, 'Student'), (2, 'Professor'), (3, 'Visitor')])),
                ('_email', models.EmailField(max_length=75, default=None)),
                ('_mobile_number', models.BigIntegerField(null=True)),
                ('_date_joined', models.DateTimeField(default=datetime.datetime(2015, 1, 8, 6, 4, 1, 733044, tzinfo=utc))),
                ('_ratings', models.BigIntegerField(default=None)),
                ('_area_of_interest', models.CharField(max_length=200, default=None)),
                ('_courses_teaching', models.CharField(max_length=200, default=None)),
                ('_best_known_for', models.CharField(max_length=200, default=None)),
                ('_popular_name', models.CharField(max_length=200, default=None)),
                ('_branch', models.ForeignKey(default=None, to='Users.Branch')),
                ('_college', models.ForeignKey(default=None, to='University.College')),
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
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('qualification_name', models.CharField(max_length=200, default=None)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('_username', models.CharField(max_length=15, default=None, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200, default=None)),
                ('_password', models.CharField(max_length=30, default=None)),
                ('user_type', models.IntegerField(default=3, choices=[(1, 'Student'), (2, 'Professor'), (3, 'Visitor')])),
                ('_email', models.EmailField(max_length=75, default=None)),
                ('_mobile_number', models.BigIntegerField(null=True)),
                ('_date_joined', models.DateTimeField(default=datetime.datetime(2015, 1, 8, 6, 4, 1, 733044, tzinfo=utc))),
                ('_year', models.IntegerField(default=0, choices=[(0, 'Other'), (1, 'First Year'), (2, 'Second Year'), (3, 'Third Year'), (4, 'Fourth Year'), (5, 'Fifth Year')])),
                ('_contributing_factor', models.BigIntegerField(default=None)),
                ('_degree_pursued', models.CharField(max_length=100, default=None)),
                ('_discipline', models.CharField(max_length=100, default=None)),
                ('_branch', models.ForeignKey(default=None, to='Users.Branch')),
                ('_college', models.ForeignKey(default=None, to='University.College')),
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
