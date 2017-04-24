from django.shortcuts import render
from servicePr.models import Umzug, Reinigung, Maler, Catering, Schreiner, Baufirma, Immobilien
from servicePr.models import Sanitaer, Gartenbau, Architekt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import EintragFormular, Anfrage
from .firm import Firmeneintrag
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

def search(s, q, f):

    sL = list(q)
    del(sL[1])
    del(sL[2])
    del(sL[1])
    q = "".join(sL)

    if s == 'umzug':
        firma[f] = Umzug.objects.filter(firm_plz__contains=q)
    elif s == 'reinigung':
        firma[f] = Reinigung.objects.filter(firm_plz__contains=q)
    elif s == 'maler':
        firma[f] = Maler.objects.filter(firm_plz__contains=q)
    elif s == 'catering':
        firma[f] = Catering.objects.filter(firm_plz__contains=q)
    elif s == 'baufirma':
        firma[f] = Baufirma.objects.filter(firm_plz__contains=q)
    elif s == 'architekt':
        firma[f] = Architekt.objects.filter(firm_plz__contains=q)
    elif s == 'schreiner':
        firma[f] = Schreiner.objects.filter(firm_plz__contains=q)
    elif s == 'sanitaer':
        firma[f] = Sanitaer.objects.filter(firm_plz__contains=q)
    elif s == 'immobilien':
        firma[f] = Immobilien.objects.filter(firm_plz__contains=q)
    elif s == 'gartenbau':
        firma[f] = Gartenbau.objects.filter(firm_plz__contains=q)
    else:
        print('PLZ nicht gefunden!!')

    return firma[f]

def filter(request):

    s = request.POST.get("select")
    q = request.POST.get("query")

    context = {

    }

    for f in firma:
        if f == s:
            if q:
                firma[f] = search(s, q, f)
            lat, lng = geocode[f]
            anz = counter(firma[f])
            paginator = Paginator(firma[f], 18)

            page = request.GET.get('page')
            try:
                sites = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                sites = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                sites = paginator.page(paginator.num_pages)

            context = {
                'firma': firma[f],
                'firma': sites,
                'lat': lat,
                'lng': lng,
                'anz': anz,
            }

    return render(request, 'branchen/show.html', context)

def index(request):

    context = {
    }

    return render(request, 'home.html', context)

def show(request, name):

    n = name

    U = Firmeneintrag()
    f = U.loadFirma(n)

    geocode[n] = latLng(f)
    lat, lng = geocode[n]
    contacts = U.pagi(request, f)
    anz = counter(f)

    q = request.POST.get("query")
    if q:
        f = search(n, q, f)

    form = Anfrage()
    if request.POST:
        form = Anfrage(request.POST)
        if form.is_valid():
            form.save(commit=True)

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

# ****FORM****
def firmaForm(request):
    form = EintragFormular(request.POST)
    if form.is_valid():
        form.save(commit=True)
        return render(request, 'nav/form_bestaetigung.html', {})
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


# ***COUNTER****
def counter(branche):
    index = 0
    for branche in branche:
        index += 1
    return index