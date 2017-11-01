from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models_new import Firma

class Firmeneintrag_new:

    def __init__(self):
        self.data = []

    def loadF(self, name):
        self.name = name

        branchen = {'Umzug': 1, 'Reinigung': 2, 'Maler': 3, 'Baufirma': 4, 'Architekt': 5,
                    'Catering': 6, 'Schreiner': 7, 'Gartenbau': 8, 'Immobilien': 9, 'Sanitaer': 10, }

        branche_auswahl = branchen.get(self.name)
        firm_list = Firma.objects.filter(branche=branche_auswahl)

        return firm_list

    def getFirm(self, name, firm_list):
        self.name = name
        self.firm_list = firm_list

        branchen = {'Umzug': 1, 'Reinigung': 2, 'Maler': 3, 'Baufirma': 4, 'Architekt': 5,
                    'Catering': 6, 'Schreiner': 7, 'Gartenbau': 8, 'Immobilien': 9, 'Sanitaer': 10, }

        branche_auswahl = branchen.get(self.name)
        firm_list = firm_list.filter(branche=branche_auswahl)

        return firm_list

    def pagi(self, request, f):

        self.request = request
        self.f = f

        paginator = Paginator(f, 12)
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