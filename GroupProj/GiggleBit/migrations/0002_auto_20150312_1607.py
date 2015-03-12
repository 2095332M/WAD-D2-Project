# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import GiggleBit.models


class Migration(migrations.Migration):

    dependencies = [
        ('GiggleBit', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(upload_to=GiggleBit.models.get_prof_pic_path),
            preserve_default=True,
        ),
    ]
