# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0002_remove_signup_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='Gender_option',
            field=models.CharField(default=datetime.datetime(2014, 11, 18, 21, 40, 56, 899263, tzinfo=utc), max_length=1, choices=[(b'F', b'Female'), (b'M', b'Male')]),
            preserve_default=False,
        ),
    ]
