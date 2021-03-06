from servicePr.models import Umzug, Reinigung, Baufirma, Architekt, Gartenbau
from servicePr.models import Maler, Sanitaer, Schreiner, Catering, Immobilien
from .firm import Firmeneintrag

class Search:

    def __init__(self):
        self.data = []

    def plz(self, p, n):
        self.p = p
        self.n = n

        r = Region()
        r_list = r.input(p)
        f_list = self.filter_plz(n, r_list)

        return f_list

    def filter_plz(self, name, r_list):
        self.name = name
        self.r_list = r_list

        if name == 'Umzug':
            firma = Umzug.objects.all()
            firm_list = []
            for r in r_list:
                if firma.filter(firm_plz__icontains=r):
                    firm_list += firma.filter(firm_plz__contains=r)
            pass
        elif name == 'Reinigung':
            firma = Reinigung.objects.all()
            firm_list = []
            for r in r_list:
                if firma.filter(firm_plz__icontains=r):
                    firm_list += firma.filter(firm_plz__contains=r)
            pass
        elif name == 'Maler':
            firma = Maler.objects.all()
            firm_list = []
            for r in r_list:
                if firma.filter(firm_plz__icontains=r):
                    firm_list += firma.filter(firm_plz__contains=r)
            pass
        elif name == 'Catering':
            firma = Catering.objects.all()
            firm_list = []
            for r in r_list:
                if firma.filter(firm_plz__icontains=r):
                    firm_list += firma.filter(firm_plz__contains=r)
            pass
        elif name == 'Baufirma':
            firma = Baufirma.objects.all()
            firm_list = []
            for r in r_list:
                if firma.filter(firm_plz__icontains=r):
                    firm_list += firma.filter(firm_plz__contains=r)
        elif name == 'Architekt':
            firma = Architekt.objects.all()
            firm_list = []
            for r in r_list:
                if firma.filter(firm_plz__icontains=r):
                    firm_list += firma.filter(firm_plz__contains=r)
            pass
        elif name == 'Schreiner':
            firma = Schreiner.objects.all()
            firm_list = []
            for r in r_list:
                if firma.filter(firm_plz__icontains=r):
                    firm_list += firma.filter(firm_plz__contains=r)
            pass
        elif name == 'Sanitaer':
            firma = Sanitaer.objects.all()
            firm_list = []
            for r in r_list:
                if firma.filter(firm_plz__icontains=r):
                    firm_list += firma.filter(firm_plz__contains=r)
            pass
        elif name == 'Immobilien':
            firma = Immobilien.objects.all()
            firm_list = []
            for r in r_list:
                if firma.filter(firm_plz__icontains=r):
                    firm_list += firma.filter(firm_plz__contains=r)
            pass
        elif name == 'Gartenbau':
            firma = Gartenbau.objects.all()
            firm_list = []
            for r in r_list:
                if firma.filter(firm_plz__icontains=r):
                    firm_list += firma.filter(firm_plz__contains=r)
            pass
        return firm_list

class Region:

    def __init__(self):
        self.data = []

    def input(self, n):
        self.n = n

        n = int(n)

        if n >= 1000 and n <= 1997:
            return list(range(1000, 1997))
        elif n >= 2000 and n <= 2954:
            return list(range(2000, 2954))
        elif n >= 3000 and n <= 3999:
            return list(range(3000, 3999))
        elif n >= 4000 and n <= 4955:
            return list(range(4000, 4955))
        elif n >= 5000 and n <= 5746:
            return list(range(5000, 5746))
        elif n >= 6000 and n <= 6999:
            return list(range(6000, 6999))
        elif n >= 7000 and n <= 7748:
            return list(range(7000, 7748))
        elif n >= 8000 and n <= 8967:
            return list(range(8000, 8967))
        elif n >= 9000 and n <= 9658:
            return list(range(9000, 9658))
        else:
            return '0'
