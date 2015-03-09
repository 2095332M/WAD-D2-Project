# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GiggleBit', '0002_auto_20150308_1758'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='fav_catgory',
            new_name='fav_category',
        ),
        migrations.RenameField(
            model_name='fav_category',
            old_name='catagory',
            new_name='category',
        ),
        migrations.AlterField(
            model_name='image',
            name='picture',
            field=models.ImageField(upload_to=b'images'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(upload_to=b'profile_images'),
            preserve_default=True,
        ),
    ]
