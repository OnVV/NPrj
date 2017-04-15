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

geocode = dict()
firma = dict()

#Umzug
firma['umzug'] = Umzug.objects.all()
geocode['umzug'] = latLng(firma['umzug'])

#Reinigung
firma['reinigung'] = Reinigung.objects.all()
geocode['reinigung'] = latLng(firma['reinigung'])

#Maler
firma['maler'] = Maler.objects.all()
geocode['maler']= latLng(firma['maler'])

#Catering
firma['catering'] = Catering.objects.all()
geocode['catering'] = latLng(firma['catering'])

#Immobilien
firma['immobilien'] = Immobilien.objects.all()
geocode['immobilien'] = latLng(firma['immobilien'])

#Schreiner
firma['schreiner'] = Schreiner.objects.all()
geocode['schreiner'] = latLng(firma['schreiner'])

#Sanitär
firma['sanitaer'] = Sanitaer.objects.all()
geocode['sanitaer'] = latLng(firma['sanitaer'])

#Gartenbau
firma['gartenbau'] = Gartenbau.objects.all()
geocode['gartenbau'] = latLng(firma['gartenbau'])

#Baufirma
firma['baufirma'] = Baufirma.objects.all()
geocode['baufirma'] = latLng(firma['baufirma'])

#Architekt
firma['architekt'] = Architekt.objects.all()
geocode['architekt'] = latLng(firma['architekt'])

# key = 'umzug'
# if key in firma:
#     print(firma.keys())
#     print('+++++++++++++++++++++++++++++++++++++')
#
#     print(firma.values())
#
#     print('+++++++++++++++++++++++++++++++++++++')
#     value = '8050'
#     plz = Umzug.objects.filter(firm_plz__contains=value)
#     print(plz)
#     for firma in firma:
#         print(firma)

def index(request):

    s = request.POST.get("select")
    q = request.POST.get("query")

    print(s)
    print(q)

    TitleText = 'Sie suchen einen Fachmann?Sie finden hier professionelle Dienstleister aus Ihrer Umgebung.\
                Sparen Sie sich die lange suche nach Experten. Bei uns erreichen Sie mit einer Anfrage mehrere Anbieter.\
                Sie entscheiden an welche Anbieter die Anfrage gehen soll.'

    context = {
        'TitleText': TitleText,
    }
    for f in firma:
        if f == s:
            lat, lng = geocode[f]
            anz = counter(firma[f])

            context = {
                'firma': firma[f],
                'lat': lat,
                'lng': lng,
                'anz': anz,
            }

            return render(request, 'branchen/show.html', context)

    return render(request, 'home.html', context)

def schreiner(request):

    lat, lng = geocode['schreiner']
    anz = counter(firma['schreiner'])

    context = {
        'title': 'Schreiner',
        'firma': firma['schreiner'],
        'lat': lat,
        'lng': lng,
        'anz': anz,
                }
    return render(request, 'branchen/show.html', context)

def sanitaer(request):
    lat, lng = geocode['sanitaer']
    anz = counter(firma['sanitaer'])

    context = {
        'title': 'Sanitär',
        'firma': firma['sanitaer'],
        'lat': lat,
        'lng': lng,
        'anz': anz,
                }
    return render(request, 'branchen/show.html', context)

def immobilien(request):
    lat, lng = geocode['immobilien']
    anz = counter(firma['immobilien'])

    context = {
        'title': 'Immobilien',
        'firma': firma['immobilien'],
        'lat': lat,
        'lng': lng,
        'anz': anz,
                }
    return render(request, 'branchen/show.html', context)

def gartenbau(request):
    lat, lng = geocode['gartenbau']
    anz = counter(firma['gartenbau'])

    context = {
        'title': 'Gartenbau',
        'firma': firma['gartenbau'],
        'lat': lat,
        'lng': lng,
        'anz': anz,
                }
    return render(request, 'branchen/show.html', context)

def baufirma(request):
    lat, lng = geocode['baufirma']
    anz = counter(firma['baufirma'])

    context = {
        'title': 'Baufirma',
        'firma': firma['baufirma'],
        'lat': lat,
        'lng': lng,
        'anz': anz,
                }
    return render(request, 'branchen/show.html', context)

def architekt(request):
    lat, lng = geocode['architekt']
    anz = counter(firma['architekt'])

    context = {
        'title': 'Architekt',
        'firma': firma['architekt'],
        'lat': lat,
        'lng': lng,
        'anz': anz,
                }
    return render(request, 'branchen/show.html', context)


def umzug(request):

    lat, lng = geocode['umzug']
    anz = counter(firma['umzug'])

    context = {
        'title': 'Umzug',
        'firma': firma['umzug'],
        'lat': lat,
        'lng': lng,
        'anz': anz,
                }

    return render(request, 'branchen/show.html', context)

def reinigung(request):
    lat, lng = geocode['reinigung']
    anz = counter(firma['reinigung'])

    context = {
        'title': 'Reinigung',
            'firma': firma['reinigung'],
           'lat': lat,
           'lng': lng,
           'anz': anz,
    }
    return render(request, 'branchen/show.html', context)

def maler(request):
    lat, lng = geocode['maler']
    anz = counter(firma['maler'])

    context = {
        'title': 'Maler',
        'firma': firma['maler'],
        'lat': lat,
        'lng': lng,
        'anz': anz,
    }

    return render(request, 'branchen/show.html', context)

def catering(request):
    lat, lng = geocode['catering']
    anz = counter(firma['catering'])

    context = {
        'title': 'Catering',
        'firma': firma['catering'],
         'lat': lat,
         'lng': lng,
         'anz': anz,
        }
    return render(request, 'branchen/show.html', context)


# ****FORM****
def firmaForm(request):
    form = EintragFormular(request.POST)
    if form.is_valid():
        form.save(commit=True)

    context = {
        'form': form,
    }

    return render(request, 'nav/firmaForm.html', context)

# ****Search****
def suche(request):

    form = Suche(request.POST)
    if form.is_valid():
        form.save(commit=True)

    context = {
        'form': form
    }

    return render(request, 'nav/suche.html', context)

def search(request):
    s = request.POST.get("select")
    q = request.POST.get("query")

    print(s)
    print(q)

    for f in firma:
        if f == s:
            lat, lng = geocode[f]
            anz = counter(firma[f])

            context = {
                'firma': firma[f],
                'lat': lat,
                'lng': lng,
                'anz': anz,
            }
            return render(request, 'branchen/show.html', context)

# ***COUNTER****
def counter(branche):
    index = 0
    for branche in branche:
        index += 1
    return index