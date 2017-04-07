from django.db import models

# Create your models here.
class Umzug(models.Model):
    firm_name = models.CharField(max_length=200)
    firm_adress = models.CharField(max_length=200)
    firm_plz = models.CharField(max_length=200)
    firm_homepage = models.CharField(max_length=200)
    firm_logo = models.ImageField(upload_to='treasure_images')
    updated = models.DateTimeField(auto_now=True, auto_now_add=False, blank=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True, blank=True)

    def __str__(self):
        return self.firm_name + ' - ' + self.firm_adress

class Reinigung(models.Model):
    firm_name = models.CharField(max_length=200, null=True)
    firm_adress = models.CharField(max_length=200, null=True)
    firm_plz = models.CharField(max_length=200, null=True)
    firm_homepage = models.CharField(max_length=200, null=True)
    firm_logo = models.ImageField(null=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False, null=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True, null=True)

    def __str__(self):
        return self.firm_name + ' - ' + self.firm_adress

class Architekt(models.Model):
    firm_name = models.CharField(max_length=200, null=True)
    firm_adress = models.CharField(max_length=200, null=True)
    firm_plz = models.CharField(max_length=200, null=True)
    firm_homepage = models.CharField(max_length=200, null=True)
    firm_logo = models.ImageField(null=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False, null=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True, null=True)

    def __str__(self):
        return self.firm_name + ' - ' + self.firm_adress

class Baufirma(models.Model):
    firm_name = models.CharField(max_length=200, null=True)
    firm_adress = models.CharField(max_length=200, null=True)
    firm_plz = models.CharField(max_length=200, null=True)
    firm_homepage = models.CharField(max_length=200, null=True)
    firm_logo = models.ImageField(null=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False, null=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True, null=True)

    def __str__(self):
        return self.firm_name + ' - ' + self.firm_adress

class Catering(models.Model):
    firm_name = models.CharField(max_length=200, null=True)
    firm_adress = models.CharField(max_length=200, null=True)
    firm_plz = models.CharField(max_length=200, null=True)
    firm_homepage = models.CharField(max_length=200, null=True)
    firm_logo = models.ImageField(null=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False, null=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True, null=True)

    def __str__(self):
        return self.firm_name + ' - ' + self.firm_adress

class Gartenbau(models.Model):
    firm_name = models.CharField(max_length=200, null=True)
    firm_adress = models.CharField(max_length=200, null=True)
    firm_plz = models.CharField(max_length=200, null=True)
    firm_homepage = models.CharField(max_length=200, null=True)
    firm_logo = models.ImageField(null=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False, null=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True, null=True)

    def __str__(self):
        return self.firm_name + ' - ' + self.firm_adress

class Immobilien(models.Model):
    firm_name = models.CharField(max_length=200, null=True)
    firm_adress = models.CharField(max_length=200, null=True)
    firm_plz = models.CharField(max_length=200, null=True)
    firm_homepage = models.CharField(max_length=200, null=True)
    firm_logo = models.ImageField(null=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False, null=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True, null=True)

    def __str__(self):
        return self.firm_name + ' - ' + self.firm_adress

class Maler(models.Model):
    firm_name = models.CharField(max_length=200, null=True)
    firm_adress = models.CharField(max_length=200, null=True)
    firm_plz = models.CharField(max_length=200, null=True)
    firm_homepage = models.CharField(max_length=200, null=True)
    firm_logo = models.ImageField(null=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False, null=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True, null=True)

    def __str__(self):
        return self.firm_name + ' - ' + self.firm_adress

class Sanitaer(models.Model):
    firm_name = models.CharField(max_length=200, null=True)
    firm_adress = models.CharField(max_length=200, null=True)
    firm_plz = models.CharField(max_length=200, null=True)
    firm_homepage = models.CharField(max_length=200, null=True)
    firm_logo = models.ImageField(null=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False, null=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True, null=True)

    def __str__(self):
        return self.firm_name + ' - ' + self.firm_adress

class Schreiner(models.Model):
    firm_name = models.CharField(max_length=200, null=True)
    firm_adress = models.CharField(max_length=200, null=True)
    firm_plz = models.CharField(max_length=200, null=True)
    firm_homepage = models.CharField(max_length=200, null=True)
    firm_logo = models.ImageField(null=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False, null=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True, null=True)

    def __str__(self):
        return self.firm_name + ' - ' + self.firm_adress

class Firmeneintrag(models.Model):
    name = models.CharField(max_length=200, null=True)
    firma = models.CharField(max_length=200, null=True)
    eMail = models.CharField(max_length=200, null=True)
    branche = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name + ' - ' + self.firma
