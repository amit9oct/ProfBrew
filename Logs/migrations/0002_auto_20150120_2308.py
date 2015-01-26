# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0003_auto_20150120_2308'),
        ('Logs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfDislikeLog',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('_professor', models.ForeignKey(to='Users.Professor')),
                ('dislike_student', models.ForeignKey(to='Users.Student')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProfDontKnowLog',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('_professor', models.ForeignKey(to='Users.Professor')),
                ('dont_know_student', models.ForeignKey(to='Users.Student')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProfLikeLog',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('_professor', models.ForeignKey(to='Users.Professor')),
                ('like_student', models.ForeignKey(to='Users.Student')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='proflog',
            name='_professor',
        ),
        migrations.RemoveField(
            model_name='proflog',
            name='_student',
        ),
        migrations.DeleteModel(
            name='ProfLog',
        ),
    ]
