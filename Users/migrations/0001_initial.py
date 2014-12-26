# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('username', models.CharField(serialize=False, primary_key=True, max_length=15, default=None)),
                ('name', models.CharField(max_length=200, default=None)),
                ('password', models.CharField(max_length=30, default=None)),
                ('user_type', models.CharField(choices=[(1, 'Student'), (2, 'Professor'), (3, 'Visitor')], max_length=10, default=3)),
                ('email', models.EmailField(max_length=75, default=None)),
                ('mobile_number', models.BigIntegerField(default=None, null=True)),
                ('date_joined', models.DateTimeField(default=None)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
