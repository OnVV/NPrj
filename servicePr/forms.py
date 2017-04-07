from django import forms
from .models import Firmeneintrag
from captcha.fields import CaptchaField

class EintragFormular(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Firmeneintrag
        fields = ['name', 'firma', 'eMail', 'branche']