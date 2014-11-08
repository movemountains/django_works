# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bucket',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_email', models.EmailField(max_length=75)),
                ('bucket_name', models.CharField(max_length=120, null=True, blank=True)),
                ('bucket_description', models.CharField(max_length=150, null=True, blank=True)),
                ('bucket_open_date', models.DateTimeField(verbose_name=b'date started')),
                ('bucket_option', models.CharField(default=b'P', max_length=1, choices=[(b'P', b'Public'), (b'R', b'Private')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
