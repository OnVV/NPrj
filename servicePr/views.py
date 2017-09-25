from django.shortcuts import render
from servicePrMail.forms import EintragFormular, Anfrage
from .firm import Firmeneintrag_new
from search import search_plz
from googleMapsAPI.geocoords import GeoCoords
from .models_new import Firma
import googlemaps
import random

geocode = dict()

def index(request):

    firma = Firmeneintrag_new()

    if request.POST:
        try:
            s = request.POST.get('select')
            q = request.POST.get('query')
        except:
            print("ERROR")

        if s == 'X':
            return render(request, 'home.html')

        firma_new = firma.loadF(s)

        geo = GeoCoords()
        geocode[s] = geo.latLng(firma_new)
        lat, lng = geocode[s]
        pagi = firma.pagi(request, firma_new)
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
            geocode[s] = geo.latLng(firma_search)
            lat, lng = geocode[s]

            context = {
                'title': s,
                'firma_new': firma_new,
                'search_res': firma_search,
                'query': q,
                'firma': pagi,
                'form': form,
                'lat': lat,
                'lng': lng,
                'anz': anz,
            }
            
        else:

            context = {
                'title': s,
                'firma_new': firma_new,
                'query': q,
                'firma': pagi,
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
    pagi = firma.pagi(request, f)
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
                'form': form,
                'lat': lat,
                'lng': lng,
                'anz': anz,
            }

            return render(request, 'branchen/show.html', context)

        search = search_plz.Search()
        firm_list = search.filter_plz(firma_new, y)
        pagi = firma.pagi(request, firm_list)
        geocode[req_name] = geo.latLng(firm_list)
        lat, lng = geocode[req_name]

        context = {
            'title': n,
            'firma_new': pagi,
            'search_res': firm_list,
            'query': q,
            'form': form,
            'lat': lat,
            'lng': lng,
            'anz': anz,
        }

        return render(request, 'branchen/show.html', context)

    context = {
        'title': n,
        'firma_new': f,
        'firma_new': pagi,
        'form': form,
        'lat': lat,
        'lng': lng,
        'anz': anz,
    }

    return render(request, 'branchen/show.html', context)


# ****FORM****
def firmaForm(request):
    form = EintragFormular()
    if request.POST.get("name"):
        form = EintragFormular(request.POST)
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