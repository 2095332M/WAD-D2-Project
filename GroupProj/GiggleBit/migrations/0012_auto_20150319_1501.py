# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GiggleBit', '0011_auto_20150319_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(to='GiggleBit.Userprofile'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='fav_category',
            name='user',
            field=models.ForeignKey(to='GiggleBit.Userprofile'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='liked',
            name='user',
            field=models.ForeignKey(to='GiggleBit.Userprofile'),
            preserve_default=True,
        ),
    ]
