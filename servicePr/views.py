from django.shortcuts import render
from servicePr.models import Umzug, Reinigung, Maler, Catering, Schreiner, Baufirma, Immobilien
from servicePr.models import Sanitaer, Gartenbau, Architekt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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

# Schreiner
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

def search(s, q, f):

    print(q)
    sL = list(q)
    del(sL[1])
    del(sL[2])
    del(sL[1])
    q = "".join(sL)
    print(q)

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

def index(request):

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

    return render(request, 'home.html', context)

def umzug(request):

    # Umzug
    firma['umzug'] = Umzug.objects.all()
    geocode['umzug'] = latLng(firma['umzug'])

    q = request.POST.get("query")

    if q:
        firma['umzug'] = search('umzug', q, firma['umzug'])

    lat, lng = geocode['umzug']
    anz = counter(firma['umzug'])

    paginator = Paginator(firma['umzug'], 18)
    page = request.GET.get('page')

    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)

    context = {
            'title': 'Umzug',
            'firma': firma['umzug'],
            'firma': contacts,
            'lat': lat,
            'lng': lng,
            'anz': anz,
            }

    return render(request, 'branchen/show.html', context)

def schreiner(request):

    # Schreiner
    firma['schreiner'] = Schreiner.objects.all()
    geocode['schreiner'] = latLng(firma['schreiner'])

    q = request.POST.get("query")

    if q:
        firma['schreiner'] = search('schreiner', q, firma['schreiner'])

    lat, lng = geocode['schreiner']
    anz = counter(firma['schreiner'])

    paginator = Paginator(firma['schreiner'], 18)
    page = request.GET.get('page')

    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)

    context = {
            'title': 'Schreiner',
            'firma': firma['schreiner'],
            'firma': contacts,
            'lat': lat,
            'lng': lng,
            'anz': anz,
            }
    return render(request, 'branchen/show.html', context)

def sanitaer(request):

    # Sanitaer
    firma['sanitaer'] = Sanitaer.objects.all()
    geocode['sanitaer'] = latLng(firma['sanitaer'])

    q = request.POST.get("query")

    if q:
        firma['sanitaer'] = search('sanitaer', q, firma['sanitaer'])

    lat, lng = geocode['sanitaer']
    anz = counter(firma['sanitaer'])

    paginator = Paginator(firma['sanitaer'], 18)
    page = request.GET.get('page')

    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)

    context = {
            'title': 'Sanitaer',
            'firma': firma['sanitaer'],
            'firma': contacts,
            'lat': lat,
            'lng': lng,
            'anz': anz,
            }
    return render(request, 'branchen/show.html', context)

def immobilien(request):
    # immobilien
    firma['immobilien'] = Immobilien.objects.all()
    geocode['immobilien'] = latLng(firma['immobilien'])

    q = request.POST.get("query")

    if q:
        firma['immobilien'] = search('immobilien', q, firma['immobilien'])

    lat, lng = geocode['immobilien']
    anz = counter(firma['immobilien'])

    paginator = Paginator(firma['immobilien'], 18)
    page = request.GET.get('page')

    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)

    context = {
            'title': 'Immobilien',
            'firma': firma['immobilien'],
            'firma': contacts,
            'lat': lat,
            'lng': lng,
            'anz': anz,
            }
    return render(request, 'branchen/show.html', context)

def gartenbau(request):

    # Gartenbau
    firma['gartenbau'] = Gartenbau.objects.all()
    geocode['gartenbau'] = latLng(firma['gartenbau'])

    q = request.POST.get("query")

    if q:
        firma['gartenbau'] = search('gartenbau', q, firma['gartenbau'])

    lat, lng = geocode['gartenbau']
    anz = counter(firma['gartenbau'])

    paginator = Paginator(firma['gartenbau'], 18)
    page = request.GET.get('page')

    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)

    context = {
            'title': 'Gartenbau',
            'firma': firma['gartenbau'],
            'firma': contacts,
            'lat': lat,
            'lng': lng,
            'anz': anz,
            }
    return render(request, 'branchen/show.html', context)

def baufirma(request):
    # Baufirma
    firma['baufirma'] = Baufirma.objects.all()
    geocode['baufirma'] = latLng(firma['baufirma'])

    q = request.POST.get("query")

    if q:
        firma['baufirma'] = search('baufirma', q, firma['baufirma'])

    lat, lng = geocode['baufirma']
    anz = counter(firma['baufirma'])

    paginator = Paginator(firma['baufirma'], 18)
    page = request.GET.get('page')

    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)

    context = {
        'title': 'Baufirma',
        'firma': firma['baufirma'],
        'firma': contacts,
        'lat': lat,
        'lng': lng,
        'anz': anz,
            }
    return render(request, 'branchen/show.html', context)

def architekt(request):
    # Architekt
    firma['architekt'] = Architekt.objects.all()
    geocode['architekt'] = latLng(firma['architekt'])

    q = request.POST.get("query")

    if q:
        firma['architekt'] = search('architekt', q, firma['architekt'])

    lat, lng = geocode['architekt']
    anz = counter(firma['architekt'])

    paginator = Paginator(firma['architekt'], 18)
    page = request.GET.get('page')

    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)

    context = {
        'title': 'Architekt',
        'firma': firma['architekt'],
        'firma': contacts,
        'lat': lat,
        'lng': lng,
        'anz': anz,
    }
    return render(request, 'branchen/show.html', context)

def reinigung(request):
    # Reinigung
    firma['reinigung'] = Reinigung.objects.all()
    geocode['reinigung'] = latLng(firma['reinigung'])

    q = request.POST.get("query")

    if q:
        firma['reinigung'] = search('reinigung', q, firma['reinigung'])

    lat, lng = geocode['reinigung']
    anz = counter(firma['reinigung'])

    paginator = Paginator(firma['reinigung'], 18)
    page = request.GET.get('page')

    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)

    context = {
        'title': 'Reinigung',
        'firma': firma['reinigung'],
        'firma': contacts,
        'lat': lat,
        'lng': lng,
        'anz': anz,
    }
    return render(request, 'branchen/show.html', context)

def maler(request):
    # Maler
    firma['maler'] = Maler.objects.all()
    geocode['maler'] = latLng(firma['maler'])

    q = request.POST.get("query")

    if q:
        firma['maler'] = search('maler', q, firma['maler'])

    lat, lng = geocode['maler']
    anz = counter(firma['maler'])

    paginator = Paginator(firma['maler'], 18)
    page = request.GET.get('page')

    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)

    context = {
        'title': 'Maler',
        'firma': firma['maler'],
        'firma': contacts,
        'lat': lat,
        'lng': lng,
        'anz': anz,
    }

    return render(request, 'branchen/show.html', context)

def catering(request):
    # Catering
    firma['catering'] = Catering.objects.all()
    geocode['catering'] = latLng(firma['catering'])

    q = request.POST.get("query")

    if q:
        firma['catering'] = search('catering', q, firma['catering'])

    lat, lng = geocode['catering']
    anz = counter(firma['catering'])

    paginator = Paginator(firma['catering'], 18)
    page = request.GET.get('page')

    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)

    context = {
        'title': 'Catering',
        'firma': firma['catering'],
        'firma': contacts,
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


# ***COUNTER****
def counter(branche):
    index = 0
    for branche in branche:
        index += 1
    return index