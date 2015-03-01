# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OtherDetails',
            fields=[
                ('_email', models.EmailField(primary_key=True, default=None, max_length=75, serialize=False)),
                ('_job_satisfaction', models.CharField(max_length=2000)),
                ('_research_avenues', models.CharField(max_length=2000)),
                ('_job_satisfaction_rate', models.CharField(max_length=10)),
                ('_research_avenues_rate', models.CharField(max_length=10)),
                ('_college_review_rate', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
