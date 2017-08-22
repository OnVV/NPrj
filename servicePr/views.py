from django.shortcuts import render
from servicePrMail.forms import EintragFormular, Anfrage
from .firm import Firmeneintrag_new
from .search import Search
from googleMapsAPI.geocoords import GeoCoords
import googlemaps
import random

geocode = dict()

def index(request):

    if request.POST:
        s = request.POST.get("select")
        q = request.POST.get("query")

        firma = Firmeneintrag_new()
        firma_new = firma.loadF(s)
        print('Test1: ', firma_new)

        if s == 'X':
            return render(request, 'home.html')

        # if q < '1000' or q > '10000':
        #     return render(request, 'home.html')

        geo = GeoCoords()
        geocode[s] = geo.latLng(firma_new)
        lat, lng = geocode[s]
        contacts = firma.pagi(request, firma_new)
        anz = counter(firma_new)

        form = Anfrage()
        if request.POST:
            form = Anfrage(request.POST)
            if form.is_valid():
                form.save(commit=True)

        else:
            query = int(q)
            # search = Search()
            # firm_list = search.plz(query, s)
            # contacts = x.pagi(request, firm_list)

            context = {
                'title': s,
                'firma': firm_list,
                #'firma': contacts,
                'firma_new': firma_new,
                'form': form,
                'lat': lat,
                'lng': lng,
                'anz': anz,
            }

            return render(request, 'branchen/show.html', context)

        context = {
            'title': s,
            'firma_new': firma_new,
            'firma': contacts,
            'form': form,
            'lat': lat,
            'lng': lng,
            'anz': anz,
        }

        return render(request, 'branchen/show.html', context)

    context = {
    }

    return render(request, 'home.html', context)

def show(request, name):

    n = name

    firma = Firmeneintrag_new()
    firma_new = firma.loadF(n)
    print('Test1: ', firma_new)

    f = firma_new
    f = random.sample(f, len(f))

    geo = GeoCoords()
    geocode[n] = geo.latLng(f)
    lat, lng = geocode[n]
    contacts = firma.pagi(request, f)
    anz = counter(f)

    form = Anfrage()
    if request.POST:
        form = Anfrage(request.POST)
        if form.is_valid():
            form.save(commit=True)

    else:
        if request.POST.get("query"):

            s = request.POST.get("query")
            y = int(s)

            if s == '' or y < 1000 or y > 10000:
                context = {
                    'title': n,
                    'firma': f,
                    'firma': contacts,
                    'form': form,
                    'lat': lat,
                    'lng': lng,
                    'anz': anz,
                }

                return render(request, 'branchen/show.html', context)

            search = Search()
            firm_list = search.plz(y, n)
            contacts = f.pagi(request, firm_list)

            context = {
                'title': n,
                'firma_new': firm_list,
                'firma_new': contacts,
                'firma_new': f,
                'form': form,
                'lat': lat,
                'lng': lng,
                'anz': anz,
            }

            return render(request, 'branchen/show.html', context)

    context = {
        'title': n,
        'firma_new': f,
        'firma_new': contacts,
        'form': form,
        'lat': lat,
        'lng': lng,
        'anz': anz,
    }

    return render(request, 'branchen/show.html', context)


# ****FORM****
def firmaForm(request):
    form = EintragFormular(request.POST)
    if request.POST.get("name"):
        if form.is_valid():
            form.save(commit=True)
            return render(request, 'nav/form_bestaetigung.html', {})

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