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
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('_branch_name', models.CharField(default=None, max_length=100, null=True)),
                ('_job_satisifaction', models.IntegerField(default=None, null=True)),
                ('_research_opportunities', models.IntegerField(default=None, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('course_name', models.CharField(default=None, max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Prof_Position',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('priority', models.BigIntegerField(null=True)),
                ('position_name', models.CharField(default=None, max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('_username', models.CharField(serialize=False, max_length=15, default=None, primary_key=True)),
                ('name', models.CharField(default=None, max_length=200)),
                ('_password', models.CharField(default=None, max_length=30)),
                ('user_type', models.IntegerField(default=3, choices=[(1, 'Student'), (2, 'Professor'), (3, 'Visitor')])),
                ('_email', models.EmailField(default=None, max_length=75)),
                ('_mobile_number', models.BigIntegerField(null=True)),
                ('_date_joined', models.DateTimeField(default=datetime.datetime(2015, 1, 8, 7, 26, 40, 594307, tzinfo=utc))),
                ('_ratings', models.BigIntegerField(default=None)),
                ('_area_of_interest', models.CharField(default=None, max_length=200)),
                ('_best_known_for', models.CharField(default=None, max_length=200)),
                ('_popular_name', models.CharField(default=None, max_length=200)),
                ('_branch', models.ForeignKey(default=None, to='Users.Branch')),
                ('_college', models.ForeignKey(default=None, to='University.College')),
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
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('qualification_name', models.CharField(default=None, max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('_username', models.CharField(serialize=False, max_length=15, default=None, primary_key=True)),
                ('name', models.CharField(default=None, max_length=200)),
                ('_password', models.CharField(default=None, max_length=30)),
                ('user_type', models.IntegerField(default=3, choices=[(1, 'Student'), (2, 'Professor'), (3, 'Visitor')])),
                ('_email', models.EmailField(default=None, max_length=75)),
                ('_mobile_number', models.BigIntegerField(null=True)),
                ('_date_joined', models.DateTimeField(default=datetime.datetime(2015, 1, 8, 7, 26, 40, 594307, tzinfo=utc))),
                ('_year', models.IntegerField(default=0, choices=[(0, 'Other'), (1, 'First Year'), (2, 'Second Year'), (3, 'Third Year'), (4, 'Fourth Year'), (5, 'Fifth Year')])),
                ('_contributing_factor', models.BigIntegerField(default=None)),
                ('_degree_pursued', models.CharField(default=None, max_length=100)),
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
