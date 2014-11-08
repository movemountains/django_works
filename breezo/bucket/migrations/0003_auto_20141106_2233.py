# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bucket', '0002_remove_bucket_user_email'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Bucket',
            new_name='Bucket_list',
        ),
    ]
