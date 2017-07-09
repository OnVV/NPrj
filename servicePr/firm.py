from .models import Umzug, Reinigung, Maler, Catering, Baufirma
from .models import Sanitaer, Gartenbau, Architekt, Schreiner, Immobilien
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import random

class Firmeneintrag:

    def __init__(self):
        self.data = []

    def loadFirma(self, name):

        self.name = name

        if name == 'Umzug':
            x = Umzug.objects.all()
            pass
        elif name == 'Reinigung':
            x = Reinigung.objects.all()
            pass
        elif name == 'Maler':
            x = Maler.objects.all()
            pass
        elif name == 'Baufirma':
            x = Baufirma.objects.all()
            pass
        elif name == 'Catering':
            x = Catering.objects.all()
            pass
        elif name == 'Architekt':
            x = Architekt.objects.all()
            pass
        elif name == 'Sanitaer':
            x = Sanitaer.objects.all()
            pass
        elif name == 'Schreiner':
            x = Schreiner.objects.all()
            pass
        elif name == 'Immobilien':
            x = Immobilien.objects.all()
            pass
        elif name == 'Gartenbau':
            x = Gartenbau.objects.all()
            pass
        else:
            print('***************************')

        x = list(x)

        return x

    def pagi(self, request, f):

        self.request = request
        self.f = f

        paginator = Paginator(f, 17)
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
