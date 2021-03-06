# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-31 18:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicePr', '0002_architekt_baufirma_catering_gartenbau_immobilien_maler_reinigung_sanitaer_schreiner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='umzug',
            name='firm_adress',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='umzug',
            name='firm_homepage',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='umzug',
            name='firm_logo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='umzug',
            name='firm_name',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='umzug',
            name='firm_plz',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='umzug',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='umzug',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
