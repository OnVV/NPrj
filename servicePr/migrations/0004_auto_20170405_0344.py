# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-05 01:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicePr', '0003_auto_20170331_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='umzug',
            name='firm_adress',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='umzug',
            name='firm_homepage',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='umzug',
            name='firm_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='umzug',
            name='firm_plz',
            field=models.CharField(max_length=200),
        ),
    ]
