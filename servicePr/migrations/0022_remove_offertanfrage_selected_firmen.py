# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-29 03:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicePr', '0021_umzug_firm_beschreibung'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offertanfrage',
            name='selected_firmen',
        ),
    ]
