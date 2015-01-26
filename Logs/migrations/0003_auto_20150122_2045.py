# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0004_auto_20150122_2045'),
        ('Logs', '0002_auto_20150120_2308'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('_like', models.BooleanField(default=False)),
                ('_dislike', models.BooleanField(default=False)),
                ('_dont_know', models.BooleanField(default=False)),
                ('_professor', models.ForeignKey(to='Users.Professor')),
                ('_student', models.ForeignKey(to='Users.Student')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='profdislikelog',
            name='_professor',
        ),
        migrations.RemoveField(
            model_name='profdislikelog',
            name='dislike_student',
        ),
        migrations.DeleteModel(
            name='ProfDislikeLog',
        ),
        migrations.RemoveField(
            model_name='profdontknowlog',
            name='_professor',
        ),
        migrations.RemoveField(
            model_name='profdontknowlog',
            name='dont_know_student',
        ),
        migrations.DeleteModel(
            name='ProfDontKnowLog',
        ),
        migrations.RemoveField(
            model_name='proflikelog',
            name='_professor',
        ),
        migrations.RemoveField(
            model_name='proflikelog',
            name='like_student',
        ),
        migrations.DeleteModel(
            name='ProfLikeLog',
        ),
    ]
