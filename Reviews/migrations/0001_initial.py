# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0003_auto_20150108_1303'),
        ('University', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BranchReviews',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('_review', models.CharField(null=True, max_length=2000, default=None)),
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
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('_review', models.CharField(null=True, max_length=2000, default=None)),
                ('_college', models.ForeignKey(to='University.College', default=None)),
                ('_student', models.ForeignKey(to='Users.Student', default=None)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProfessorReviews',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('_review', models.CharField(null=True, max_length=2000, default=None)),
                ('_professor', models.ForeignKey(to='Users.Professor', default=None)),
                ('_student', models.ForeignKey(to='Users.Student', default=None)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
