from .models import Umzug, Reinigung, Maler, Catering, Baufirma
from .models import Sanitaer, Gartenbau, Architekt, Schreiner, Immobilien
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class Firmeneintrag:

    def __init__(self):
        self.data = []

    def loadFirma(self, name):

        self.name = name

        if name == 'Umzug':
            x = Umzug.objects.all()
        elif name == 'Reinigung':
            x = Reinigung.objects.all()
        elif name == 'Maler':
            x = Maler.objects.all()
        elif name == 'Baufirma':
            x = Baufirma.objects.all()
        elif name == 'Catering':
            x = Catering.objects.all()
        elif name == 'Architekt':
            x = Architekt.objects.all()
        elif name == 'Sanitaer':
            x = Sanitaer.objects.all()
        elif name == 'Schreiner':
            x = Schreiner.objects.all()
        elif name == 'Immobilien':
            x = Immobilien.objects.all()
        elif name == 'Gartenbau':
            x = Gartenbau.objects.all()
        else:
            print('Wahr wohl nix, ihr luschen!!!')
        return x

    def pagi(self, request, f):

        self.request = request
        self.f = f

        paginator = Paginator(f, 18)
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
