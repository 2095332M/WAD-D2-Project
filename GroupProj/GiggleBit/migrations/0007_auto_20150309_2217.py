# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GiggleBit', '0006_auto_20150309_2217'),
    ]

    operations = [
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
