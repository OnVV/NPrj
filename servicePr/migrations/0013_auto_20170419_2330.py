# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-19 21:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicePr', '0012_auto_20170418_2043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firmeneintrag',
            name='branche',
            field=models.CharField(choices=[('umzug', 'Umzug'), ('reingung', 'Reingung'), ('maler', 'Maler'), ('schreiner', 'Schreiner'), ('sanitaer', 'Sanitaer'), ('immobilien', 'Immobilien'), ('gartenbau', 'Gartenbau'), ('baufirma', 'Baufirma'), ('catering', 'Catering'), ('architekt', 'Architekt')], max_length=200),
        ),
    ]
