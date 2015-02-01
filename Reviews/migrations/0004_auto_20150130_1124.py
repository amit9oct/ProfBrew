# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0004_auto_20150130_1124'),
        ('Reviews', '0003_auto_20150130_1121'),
    ]

    operations = [
        migrations.AddField(
            model_name='professorreviewlikes',
            name='_student',
            field=models.ForeignKey(to='Users.Student', default=None),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='branchreviews',
            name='_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 30, 5, 54, 37, 515815, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='collegereviews',
            name='_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 30, 5, 54, 37, 515815, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='professorreviewlikes',
            name='_review',
            field=models.ForeignKey(to='Reviews.ProfessorReviews', default=None),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='professorreviews',
            name='_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 30, 5, 54, 37, 515815, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
