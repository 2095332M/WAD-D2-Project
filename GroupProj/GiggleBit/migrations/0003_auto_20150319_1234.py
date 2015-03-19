# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GiggleBit', '0002_auto_20150312_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='slug',
            field=models.SlugField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='liked',
            name='user',
            field=models.ForeignKey(to='GiggleBit.userprofile'),
            preserve_default=True,
        ),
    ]
