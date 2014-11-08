# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bucket', '0004_doing_done_to_do'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doing',
            name='card_name',
            field=models.CharField(max_length=400, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='done',
            name='card_name',
            field=models.CharField(max_length=400, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='to_do',
            name='card_name',
            field=models.CharField(max_length=400, null=True, blank=True),
            preserve_default=True,
        ),
    ]
