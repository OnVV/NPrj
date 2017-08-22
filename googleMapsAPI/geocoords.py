import googlemaps

class GeoCoords:

    def __init__(self):
        self.data = []

    def latLng(self, branche):
        self.branche = branche
        gmaps = googlemaps.Client(key='AIzaSyBCqMzTBiROM7g3PcHaG-PY2vTqXYYtWhU')
        lat = []
        lng = []

        for adress in branche:
            adressen = gmaps.geocode(adress.firm_adress + ' ' + adress.firm_plz)
            lat.append(adressen[0]['geometry']['location']['lat'])
            lng.append(adressen[0]['geometry']['location']['lng'])
        return (lat, lng)