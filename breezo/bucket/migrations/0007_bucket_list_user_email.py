# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bucket', '0006_auto_20141107_0025'),
    ]

    operations = [
        migrations.AddField(
            model_name='bucket_list',
            name='user_email',
            field=models.EmailField(default=datetime.datetime(2014, 11, 11, 20, 31, 50, 720853, tzinfo=utc), max_length=75),
            preserve_default=False,
        ),
    ]
