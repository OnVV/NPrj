from .models import Umzug, Reinigung, Maler, Catering, Baufirma
from .models import Sanitaer, Gartenbau, Architekt, Schreiner, Immobilien
from .models_new import Firma
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import random

class Firmenenitrag_new:
    def __init__(self):
        self.data = []

    def loadF(self, name):
        self.name = name

        branchen = {'Umzug': 1, 'Reinigung': 2, 'Maler': 3, 'Baufirma': 4, 'Architekt': 5,
                    'Catering': 6, 'Schreiner': 7, 'Gartenbau': 8, 'Immobilien': 9, 'Sanitaer': 10, }

        branche_auswahl = branchen.get(self.name)

        firm = Firma.objects.all()
        firm_list = firm.filter(branche=branche_auswahl)

        return firm_list

class Firmeneintrag:

    def __init__(self):
        self.data = []

    def loadFirma(self, name):

        self.name = name

        if name == 'Umzug':
            firma = Umzug.objects.all()
            pass
        elif name == 'Reinigung':
            firma = Reinigung.objects.all()
            pass
        elif name == 'Maler':
            firma = Maler.objects.all()
            pass
        elif name == 'Baufirma':
            firma = Baufirma.objects.all()
            pass
        elif name == 'Catering':
            firma = Catering.objects.all()
            pass
        elif name == 'Architekt':
            firma = Architekt.objects.all()
            pass
        elif name == 'Sanitaer':
            firma = Sanitaer.objects.all()
            pass
        elif name == 'Schreiner':
            firma = Schreiner.objects.all()
            pass
        elif name == 'Immobilien':
            firma = Immobilien.objects.all()
            pass
        elif name == 'Gartenbau':
            firma = Gartenbau.objects.all()
            pass
        else:
            print('***************************')

        firma = list(firma)

        return firma

    def pagi(self, request, f):

        self.request = request
        self.f = f

        paginator = Paginator(f, 10)
        page = request.GET.get('page')

        try:
            sites = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            sites = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            sites = paginator.page(paginator.num_pages)

        return sites
