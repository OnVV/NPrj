# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-06 17:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicePr', '0005_auto_20170406_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='umzug',
            name='firm_logo',
            field=models.ImageField(upload_to='treasure_images'),
        ),
    ]
