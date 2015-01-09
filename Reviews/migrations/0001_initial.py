# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('University', '0001_initial'),
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BranchReviews',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('_review', models.CharField(default=None, null=True, max_length=2000)),
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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('_review', models.CharField(default=None, null=True, max_length=2000)),
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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('_review', models.CharField(default=None, null=True, max_length=2000)),
                ('_professor', models.ForeignKey(default=None, to='Users.Professor')),
                ('_student', models.ForeignKey(default=None, to='Users.Student')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
