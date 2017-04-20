from django import forms
from .models import Firmeneintrag, Suche, OffertAnfrage
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
            'branche': forms.Select(attrs={'class': 'form-control'}),
        }

class Suche(forms.ModelForm):
    class Meta:
        model = Suche
        fields = ['suche']
        widgets = {
            'suche': forms.TextInput(attrs={'class': 'form-control'}),
        }

class Anfrage(forms.ModelForm):
    class Meta:
        model = OffertAnfrage
        fields = ['name', 'adress', 'email', 'tel', 'branche', 'selected_firmen', 'description']
        widgets = {
            'adress': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'tel': forms.TextInput(attrs={'class': 'form-control'}),
            'branche': forms.Select(attrs={'class': 'form-control'}),
            'selected_firmen': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }