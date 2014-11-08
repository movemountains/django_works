# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bucket', '0005_auto_20141106_2330'),
    ]

    operations = [
        migrations.AddField(
            model_name='doing',
            name='doing_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 7, 0, 24, 48, 99079, tzinfo=utc), verbose_name=b'starting date', blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='done',
            name='done_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 7, 0, 25, 14, 51669, tzinfo=utc), verbose_name=b'Finished date', blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='to_do',
            name='dead_line',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 7, 0, 25, 25, 768827, tzinfo=utc), verbose_name=b'deadline date', blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bucket_list',
            name='bucket_open_date',
            field=models.DateTimeField(verbose_name=b'date started', blank=True),
            preserve_default=True,
        ),
    ]
