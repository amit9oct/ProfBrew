# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
        ('University', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BranchReviews',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('_review', models.CharField(null=True, default=None, max_length=2000)),
                ('_number_of_likes', models.IntegerField(default=0)),
                ('_branch', models.ForeignKey(default=None, to='Users.Branch')),
                ('_college', models.ForeignKey(default=None, to='University.College')),
                ('_student', models.ForeignKey(default=None, to='Users.Student')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CollegeReviews',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('_review', models.CharField(null=True, default=None, max_length=2000)),
                ('_number_of_likes', models.IntegerField(default=0)),
                ('_college', models.ForeignKey(default=None, to='University.College')),
                ('_student', models.ForeignKey(default=None, to='Users.Student')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProfessorReviews',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('_review', models.CharField(null=True, default=None, max_length=2000)),
                ('_number_of_likes', models.IntegerField(default=0)),
                ('_professor', models.ForeignKey(default=None, to='Users.Professor')),
                ('_student', models.ForeignKey(default=None, to='Users.Student')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
