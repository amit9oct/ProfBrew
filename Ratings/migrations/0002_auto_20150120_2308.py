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
            name='_number_of_dislikes',
            field=models.BigIntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='profratings',
            name='_number_of_likes',
            field=models.BigIntegerField(default=0),
            preserve_default=True,
        ),
    ]
