# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('_search_type', models.IntegerField(choices=[(1, 'Search by College'), (3, 'Search by Professor'), (1, 'Search by College')])),
                ('_search_key_word', models.CharField(max_length=200)),
                ('_time', models.DateTimeField(default=datetime.datetime(2015, 3, 5, 2, 42, 28, 352664, tzinfo=utc))),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SearchMadeByProfessor',
            fields=[
                ('search_ptr', models.OneToOneField(auto_created=True, parent_link=True, serialize=False, primary_key=True, to='SearchEngine.Search')),
                ('_user', models.ForeignKey(to='Users.Professor')),
            ],
            options={
            },
            bases=('SearchEngine.search',),
        ),
        migrations.CreateModel(
            name='SearchMadeByStudent',
            fields=[
                ('search_ptr', models.OneToOneField(auto_created=True, parent_link=True, serialize=False, primary_key=True, to='SearchEngine.Search')),
                ('_user', models.ForeignKey(to='Users.Student')),
            ],
            options={
            },
            bases=('SearchEngine.search',),
        ),
        migrations.CreateModel(
            name='SearchMadeByVisitor',
            fields=[
                ('search_ptr', models.OneToOneField(auto_created=True, parent_link=True, serialize=False, primary_key=True, to='SearchEngine.Search')),
                ('_user', models.IPAddressField()),
            ],
            options={
            },
            bases=('SearchEngine.search',),
        ),
    ]
