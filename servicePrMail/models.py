# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from servicePr.models_new import Branchen

class OffertenAnfrage(models.Model):
    branche = models.ForeignKey(Branchen, on_delete=models.CASCADE)
    name = models.CharField(db_index=True, max_length=200, null=True)
    plz = models.IntegerField(db_index=True)
    ort = models.CharField(db_index=True, max_length=200, null=True)
    tel = models.CharField(db_index=True, max_length=200, null=True)
    beschreibung = models.TextField()
    eMail = models.CharField(db_index=True, max_length=200, null=True)

    def __str__(self):
        return self.name + ' - ' + self.eMail

class Firmeneintrag(models.Model):
    branche = models.ForeignKey(Branchen, on_delete=models.CASCADE)
    name = models.CharField(db_index=True, max_length=200, null=True)
    firma = models.CharField(db_index=True, max_length=200, null=True)
    plz = models.IntegerField(db_index=True)
    ort = models.CharField(db_index=True, max_length=200, null=True)
    tel = models.CharField(db_index=True, max_length=200, null=True)
    eMail = models.CharField(db_index=True, max_length=200, null=True)

    def __str__(self):
        return self.name + ' - ' + self.eMail