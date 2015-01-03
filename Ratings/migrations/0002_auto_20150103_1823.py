# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Ratings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profratings',
            name='_no_of_likes',
            field=models.BigIntegerField(default=None),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='profratings',
            name='_rate',
            field=models.BigIntegerField(default=None),
            preserve_default=True,
        ),
    ]
