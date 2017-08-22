from servicePr.models_new import Firma

class Search:

    __init__(self, plz):
        self.data = []
        self.plz = plz

    def filter_plz(self, branche, range_list):
        self.branche = branche
        self.range_list = range_list

        #Filter branche firmen laden
        firma = Firma.objects.all()
        firma = firma.filter(branche=self.branche)
        firma = firma.filter(plz__contains=range_list)

        #Branche nach plz und umliegenden plz filtern
        #Firmen abspreichern
        #Firmen laden bei
        #return FirmenListe

        return firma

    def getRange(self, search_input):
        self.search_input = search_input

        n = int(search_input)
        rangeU = list(range(n-700, n+700))

        return rangeU



















