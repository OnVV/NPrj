# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-18 21:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('servicePr', '0030_delete_offertanfrage'),
        ('servicePrMail', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Firmeneintrag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, null=True)),
                ('firma', models.CharField(db_index=True, max_length=200, null=True)),
                ('plz', models.IntegerField(db_index=True)),
                ('ort', models.CharField(db_index=True, max_length=200, null=True)),
                ('tel', models.CharField(db_index=True, max_length=200, null=True)),
                ('eMail', models.CharField(db_index=True, max_length=200, null=True)),
                ('branche', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicePr.Branchen')),
            ],
        ),
    ]
