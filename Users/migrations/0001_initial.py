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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('users_ptr', models.OneToOneField(to='Users.Users', parent_link=True, serialize=False, primary_key=True, auto_created=True)),
            ],
            options={
            },
            bases=('Users.users',),
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('users_ptr', models.OneToOneField(to='Users.Users', parent_link=True, serialize=False, primary_key=True, auto_created=True)),
            ],
            options={
            },
            bases=('Users.users',),
        ),
    ]
