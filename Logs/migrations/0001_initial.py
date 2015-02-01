# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfLog',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
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
    ]
