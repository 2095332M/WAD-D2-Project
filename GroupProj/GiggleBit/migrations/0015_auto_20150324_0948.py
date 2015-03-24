# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import GiggleBit.models


class Migration(migrations.Migration):

    dependencies = [
        ('GiggleBit', '0014_auto_20150319_2115'),
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
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(default=b'test.jpg', upload_to=GiggleBit.models.get_prof_pic_path),
            preserve_default=True,
        ),
    ]
