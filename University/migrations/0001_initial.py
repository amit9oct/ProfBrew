# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('university_id', models.CharField(max_length=100, default=None)),
                ('_university_name', models.CharField(max_length=100, default=None)),
                ('_email', models.EmailField(max_length=75, default=None)),
                ('_address', models.CharField(null=True, max_length=500, default=None)),
                ('_mobile_number', models.BigIntegerField(null=True)),
                ('college_name', models.CharField(max_length=100, default=None)),
                ('college_id', models.CharField(primary_key=True, max_length=100, serialize=False, default=None)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
