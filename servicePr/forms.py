from django import forms
from .models import Firmeneintrag, Suche
from captcha.fields import CaptchaField

class EintragFormular(forms.ModelForm):

    captcha = CaptchaField()

    class Meta:
        model = Firmeneintrag
        fields = ['name', 'firma', 'eMail', 'branche']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'firma': forms.TextInput(attrs={'class': 'form-control'}),
            'eMail': forms.TextInput(attrs={'class': 'form-control'}),
            'branche': forms.TextInput(attrs={'class': 'form-control'}),
        }

class Suche(forms.ModelForm):
    class Meta:
        model = Suche
        fields = ['suche']
        widgets = {
            'suche': forms.TextInput(attrs={'class': 'form-control'}),
        }