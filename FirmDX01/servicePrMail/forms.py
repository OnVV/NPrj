from django import forms
from servicePrMail.models import OffertenAnfrage, Firmeneintrag

class EintragFormular(forms.ModelForm):
    class Meta:
        model = Firmeneintrag
        fields = ['name', 'firma', 'plz', 'ort', 'eMail', 'branche']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'firma': forms.TextInput(attrs={'class': 'form-control'}),
            'plz': forms.TextInput(attrs={'class': 'form-control'}),
            'ort': forms.TextInput(attrs={'class': 'form-control'}),
            'eMail': forms.TextInput(attrs={'class': 'form-control'}),
            'branche': forms.Select(attrs={'class': 'form-control'}),
        }

class Anfrage(forms.ModelForm):
    class Meta:
        model = OffertenAnfrage
        fields = ['name', 'plz', 'ort', 'eMail', 'tel', 'beschreibung', 'send']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'eMail': forms.TextInput(attrs={'class': 'form-control'}),
            'plz': forms.TextInput(attrs={'class': 'form-control'}),
            'ort': forms.TextInput(attrs={'class': 'form-control'}),
            'tel': forms.TextInput(attrs={'class': 'form-control'}),
            'beschreibung': forms.Textarea(attrs={'class': 'form-control'}),
            'send': forms.Textarea(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }