from django.shortcuts import render
from servicePr.models import Umzug, Reinigung, Maler, Catering, Schreiner, Baufirma, Immobilien
from servicePr.models import Sanitaer, Gartenbau, Architekt
from .forms import EintragFormular
import googlemaps

def latLng(branche):
    gmaps = googlemaps.Client(key='AIzaSyBCqMzTBiROM7g3PcHaG-PY2vTqXYYtWhU')
    lat = []
    lng = []
    for adress in branche:
        adressen = gmaps.geocode(adress.firm_adress + ' ' + adress.firm_plz)
        lat.append(adressen[0]['geometry']['location']['lat'])
        lng.append(adressen[0]['geometry']['location']['lng'])
    return (lat, lng)

#Umzug
global umzug_firma
umzug_firma = Umzug.objects.all()
umzugGeoCode = latLng(umzug_firma)
print(umzug_firma)
print(umzugGeoCode)

#Reinigung
reinigung_firma = Reinigung.objects.all()
reinigungGeoCode = latLng(reinigung_firma)
print(reinigung_firma)

#Maler
maler_firma = Maler.objects.all()
malerGeoCode = latLng(maler_firma)
print(maler_firma)

#Catering
catering_firma = Catering.objects.all()
cateringGeoCode = latLng(catering_firma)
print(catering_firma)

#Immobilien
immobilien_firma = Immobilien.objects.all()
immobilienGeoCode = latLng(immobilien_firma)
print(immobilien_firma)

#Schreiner
schreiner_firma = Schreiner.objects.all()
schreinerGeoCode = latLng(schreiner_firma)
print(schreiner_firma)

#Sanitär
sanitaer_firma = Sanitaer.objects.all()
sanitaerGeoCode = latLng(sanitaer_firma)
print(sanitaer_firma)

#Gartenbau
gartenbau_firma = Gartenbau.objects.all()
gartenbauGeoCode = latLng(gartenbau_firma)
print(gartenbau_firma)

#Baufirma
baufirma_firma = Baufirma.objects.all()
baufirmaGeoCode = latLng(baufirma_firma)
print(baufirma_firma)

#Architekt
architekt_firma = Architekt.objects.all()
architektGeoCode = latLng(architekt_firma)
print(architekt_firma)

def index(request):


    TitleText = 'Sie suchen einen Fachmann? Bei uns finden Sie professionelle Dienstleister aus Ihrer Umgebung.\
            Sparen Sie sich die lange suche nach Experten. Bei uns erreichen Sie mit einer Anfrage mehrere Anbieter.\
            Sie entscheiden an welche Anbieter die Anfrage gehen soll.\
            und verlangen Sie unverbindlich eine Offerte'

    context = {
        'TitleText': TitleText,
    }

    return render(request, 'home.html', context)

def schreiner(request):
    lat, lng = schreinerGeoCode
    anz = counter(schreiner_firma)

    context = {
        'firma': schreiner_firma,
        'lat': lat,
        'lng': lng,
        'anz': anz,
                }
    return render(request, 'branchen/schreiner.html', context)

def sanitaer(request):
    lat, lng = sanitaerGeoCode
    anz = counter(sanitaer_firma)
    context = {
        'firma': sanitaer_firma,
        'lat': lat,
        'lng': lng,
        'anz': anz,
                }
    return render(request, 'branchen/sanitaer.html', context)

def immobilien(request):
    lat, lng = immobilienGeoCode
    anz = counter(immobilien_firma)
    context = {
        'firma': immobilien_firma,
        'lat': lat,
        'lng': lng,
        'anz': anz,
                }
    return render(request, 'branchen/immobilien.html', context)

def gartenbau(request):
    lat, lng = gartenbauGeoCode
    anz = counter(gartenbau_firma)
    context = {
        'firma': gartenbau_firma,
        'lat': lat,
        'lng': lng,
        'anz': anz,
                }
    return render(request, 'branchen/gartenbau.html', context)

def baufirma(request):
    lat, lng = baufirmaGeoCode
    anz = counter(baufirma_firma)
    context = {
        'firma': baufirma_firma,
        'lat': lat,
        'lng': lng,
        'anz': anz,
                }
    return render(request, 'branchen/baufirma.html', context)

def architekt(request):
    lat, lng = architektGeoCode
    anz = counter(architekt_firma)
    context = {
        'firma': architekt_firma,
        'lat': lat,
        'lng': lng,
        'anz': anz,
                }
    return render(request, 'branchen/architekt.html', context)


def umzug(request):
    title = "Umzugsfirmen"
    lat, lng = umzugGeoCode
    anz = counter(umzug_firma)
    print(title)
    context = {
        'title': title,
        'firma': umzug_firma,
        'lat': lat,
        'lng': lng,
        'anz': anz,
                }
    return render(request, 'branchen/umzug.html', context)

def reinigung(request):
    lat, lng = reinigungGeoCode
    anz = counter(reinigung_firma)
    context = {
           'firma': reinigung_firma,
           'lat': lat,
           'lng': lng,
           'anz': anz,
    }
    return render(request, 'branchen/reinigung.html', context)

def maler(request):
    lat, lng = malerGeoCode
    anz = counter(maler_firma)
    context = {
        'firma': maler_firma,
        'lat': lat,
        'lng': lng,
        'anz': anz,
    }

    return render(request, 'branchen/maler.html', context)

def catering(request):

    lat, lng = cateringGeoCode
    anz = counter(catering_firma)

    context = {
         'firma': catering_firma,
         'lat': lat,
         'lng': lng,
         'anz': anz,
        }
    return render(request, 'branchen/catering.html', context)


# ****FORM****
def firmaForm(request):
    form = EintragFormular(request.POST)
    if form.is_valid():
        form.save(commit=True)

    context = {
        'form': form,
    }

    return render(request, 'nav/firmaForm.html', context)

# ***COUNTER****
def counter(branche):
    index = 0
    for branche in branche:
        index += 1
    return index