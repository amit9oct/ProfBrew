# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('University', '0001_initial'),
        ('Users', '0002_auto_20150305_1933'),
    ]

    operations = [
        migrations.CreateModel(
            name='BranchReviews',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('_review', models.CharField(max_length=2000, null=True, default=None)),
                ('_number_of_likes', models.IntegerField(default=0)),
                ('_date_time', models.DateTimeField(default=datetime.datetime(2015, 3, 5, 19, 33, 21, 546075, tzinfo=utc))),
                ('_branch', models.ForeignKey(to='Users.Branch', default=None)),
                ('_college', models.ForeignKey(to='University.College', default=None)),
                ('_student', models.ForeignKey(to='Users.Student', default=None)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CollegeReviews',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('_review', models.CharField(max_length=2000, null=True, default=None)),
                ('_number_of_likes', models.IntegerField(default=0)),
                ('_date_time', models.DateTimeField(default=datetime.datetime(2015, 3, 5, 19, 33, 21, 546075, tzinfo=utc))),
                ('_college', models.ForeignKey(to='University.College', default=None)),
                ('_student', models.ForeignKey(to='Users.Student', default=None)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProfessorReviewLikes',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('_liked', models.BooleanField(default=False)),
                ('_disliked', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProfessorReviews',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('_review', models.CharField(max_length=2000, null=True, default=None)),
                ('_number_of_likes', models.IntegerField(default=0)),
                ('_date_time', models.DateTimeField(default=datetime.datetime(2015, 3, 5, 19, 33, 21, 546075, tzinfo=utc))),
                ('_professor', models.ForeignKey(to='Users.Professor', default=None)),
                ('_student', models.ForeignKey(to='Users.Student', default=None)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='professorreviewlikes',
            name='_review',
            field=models.ForeignKey(to='Reviews.ProfessorReviews', default=None),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='professorreviewlikes',
            name='_student',
            field=models.ForeignKey(to='Users.Student', default=None),
            preserve_default=True,
        ),
    ]
