from django.db import models

class Branchen(models.Model):
    name = models.CharField(db_index=True, max_length=200, null=True)

    def __str__(self):
        return self.name

class Firma(models.Model):
    branche = models.ForeignKey(Branchen, on_delete=models.CASCADE)
    name = models.CharField(db_index=True, max_length=200, null=True)
    plz = models.CharField(db_index=True, max_length=5, null=True)
    ort = models.CharField(db_index=True, max_length=200, null=True)
    beschreibung = models.TextField()
    eMail = models.CharField(db_index=True, max_length=200, null=True)
    homepage = models.CharField(db_index=True, max_length=200, null=True)
    firm_logo = models.ImageField(db_index=True, upload_to='treasure_images')
    updated = models.DateTimeField(auto_now=True, auto_now_add=False, blank=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True, blank=True)

    def __str__(self):
        return self.name


