# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfRatings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('_number_of_likes', models.BigIntegerField(default=0)),
                ('_number_of_dislikes', models.BigIntegerField(default=0)),
                ('_rate', models.FloatField(default=0)),
                ('_prof', models.ForeignKey(to='Users.Professor', default=None)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
