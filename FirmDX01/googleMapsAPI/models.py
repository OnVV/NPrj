from __future__ import unicode_literals
from django.db import models
from servicePr.models_new import Firma

class Geo(models.Model):
    firm = models.ForeignKey(Firma, on_delete=models.CASCADE, null=True)
    lan = models.CharField(db_index=True, max_length=200, null=True)
    lat = models.CharField(db_index=True, max_length=200, null=True)

    def __str__(self):
        return 'lan: ' + self.lan + ' lat: ' + self.lat
