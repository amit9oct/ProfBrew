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
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('_number_of_likes', models.BigIntegerField(default=None)),
                ('_number_of_dislikes', models.BigIntegerField(default=None)),
                ('_rate', models.FloatField(default=0)),
                ('_prof', models.ForeignKey(default=None, to='Users.Professor')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
