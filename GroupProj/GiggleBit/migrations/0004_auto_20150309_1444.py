# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('GiggleBit', '0003_auto_20150309_1013'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='upload_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 9, 14, 44, 31, 690465)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='image',
            field=models.ForeignKey(to='GiggleBit.Image'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='liked',
            name='image',
            field=models.ForeignKey(to='GiggleBit.Image'),
            preserve_default=True,
        ),
    ]
