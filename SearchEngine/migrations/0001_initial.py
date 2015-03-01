# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('_search_type', models.IntegerField(choices=[(1, 'Search by College'), (3, 'Search by Professor'), (1, 'Search by College')])),
                ('_search_key_word', models.CharField(max_length=200)),
                ('_time', models.DateTimeField(default=datetime.datetime(2015, 3, 1, 16, 29, 26, 602939, tzinfo=utc))),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SearchMadeByProfessor',
            fields=[
                ('search_ptr', models.OneToOneField(auto_created=True, to='SearchEngine.Search', serialize=False, primary_key=True, parent_link=True)),
                ('_user', models.ForeignKey(to='Users.Professor')),
            ],
            options={
            },
            bases=('SearchEngine.search',),
        ),
        migrations.CreateModel(
            name='SearchMadeByStudent',
            fields=[
                ('search_ptr', models.OneToOneField(auto_created=True, to='SearchEngine.Search', serialize=False, primary_key=True, parent_link=True)),
                ('_user', models.ForeignKey(to='Users.Student')),
            ],
            options={
            },
            bases=('SearchEngine.search',),
        ),
        migrations.CreateModel(
            name='SearchMadeByVisitor',
            fields=[
                ('search_ptr', models.OneToOneField(auto_created=True, to='SearchEngine.Search', serialize=False, primary_key=True, parent_link=True)),
                ('_user', models.IPAddressField()),
            ],
            options={
            },
            bases=('SearchEngine.search',),
        ),
    ]
