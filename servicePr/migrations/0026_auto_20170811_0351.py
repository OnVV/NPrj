# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-11 03:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicePr', '0025_remove_firma_geo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firma',
            name='plz',
            field=models.IntegerField(db_index=True),
        ),
    ]
