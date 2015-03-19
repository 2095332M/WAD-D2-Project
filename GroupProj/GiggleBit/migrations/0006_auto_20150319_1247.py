# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GiggleBit', '0005_auto_20150319_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(to='GiggleBit.Userprofile'),
            preserve_default=True,
        ),
    ]
