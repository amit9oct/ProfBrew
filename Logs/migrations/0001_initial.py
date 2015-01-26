# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_auto_20150120_0100'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfLog',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('_professor', models.ForeignKey(to='Users.Professor')),
                ('_student', models.ForeignKey(to='Users.Student')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
