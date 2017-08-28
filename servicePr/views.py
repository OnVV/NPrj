from django.shortcuts import render
from servicePrMail.forms import EintragFormular, Anfrage
from .firm import Firmeneintrag_new
from search import search_plz
from googleMapsAPI.geocoords import GeoCoords
import googlemaps
import random

geocode = dict()

def index(request):

    if request.POST:
        try:
            s = request.POST.get('select')
            q = request.POST.get('query')
        except:
            print("ERROR")

        if s == 'X':
            return render(request, 'home.html')

        firma = Firmeneintrag_new()
        firma_new = firma.loadF(s)

        geo = GeoCoords()
        geocode[s] = geo.latLng(firma_new)
        lat, lng = geocode[s]
        contacts = firma.pagi(request, firma_new)
        anz = counter(firma_new)

        form = Anfrage()
        if request.POST.get(''):
            form = Anfrage(request.POST)
            if form.is_valid():
                form.save(commit=True)

        if q:
            search = search_plz.Search()
            res = search.filter_plz(firma_new, q)
            firma_search = res

        context = {
            'title': s,
            'firma_new': firma_new,
            'search_res': firma_search,
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
    req_name = request.POST.get("name")
    q = request.POST.get("query")

    firma = Firmeneintrag_new()
    firma_new = firma.loadF(n)

    f = random.sample(firma_new, len(firma_new))

    geo = GeoCoords()
    geocode[n] = geo.latLng(f)
    lat, lng = geocode[n]
    contacts = firma.pagi(request, f)
    anz = counter(f)

    form = Anfrage()
    if req_name:
        form = Anfrage(request.POST)
        if form.is_valid():
            form.save(commit=True)

    if q:
        y = int(q)

        if q == '' or y < 1000 or y > 10000:
            context = {
                'title': n,
                'firma_new': f,
                'search_res': search,
                'form': form,
                'lat': lat,
                'lng': lng,
                'anz': anz,
            }

            return render(request, 'branchen/show.html', context)

        search = search_plz.Search()
        firm_list = search.filter_plz(firma_new, y)
        #contacts = f.pagi(request, firm_list)

        context = {
            'title': n,
            'firma_new': firm_list,
            #'firma_new': contacts,
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