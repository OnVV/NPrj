from django.contrib import admin
from servicePr.models import Umzug, Architekt, Baufirma, Catering, Gartenbau
from servicePr.models import Immobilien, Maler, Reinigung, Sanitaer, Schreiner, Firmeneintrag

# Register your models here.
admin.site.register(Umzug)
admin.site.register(Architekt)
admin.site.register(Baufirma)
admin.site.register(Catering)
admin.site.register(Gartenbau)
admin.site.register(Immobilien)
admin.site.register(Maler)
admin.site.register(Reinigung)
admin.site.register(Sanitaer)
admin.site.register(Schreiner)
admin.site.register(Firmeneintrag)