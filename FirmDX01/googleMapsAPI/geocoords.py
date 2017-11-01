import googlemaps
from servicePr.firm import Firmeneintrag_new

geocode = dict()

class GeoCoords:

    def __init__(self):
        self.data = []

    def latLng(self, branche):

        gmaps = googlemaps.Client(key='AIzaSyAURdzuM6v9QzqP5KqBuRF0k00uFfif3-w')
        lat = []
        lng = []

        for adress in branche:
            adressen = gmaps.geocode(adress.ort + " " + str(adress.plz))
            lat.append(adressen[0]['geometry']['location']['lat'])
            lng.append(adressen[0]['geometry']['location']['lng'])

        return (lat, lng)

    def getAllGeocoords(self, f):

        firma = Firmeneintrag_new()
        branchen = ('Umzug', 'Reinigung', 'Maler', 'Baufirma', 'Architekt',
                    'Catering', 'Schreiner', 'Gartenbau', 'Immobilien', 'Sanitaer')

        for b in branchen:
            firma_n = firma.getFirm(b, f)

            geo = GeoCoords()
            geocode[b] = geo.latLng(firma_n)

        return geocode