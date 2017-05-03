from django.shortcuts import render
from .forms import EintragFormular, Anfrage
from .firm import Firmeneintrag
from .search import Search
import googlemaps

geocode = dict()

def latLng(branche):
    gmaps = googlemaps.Client(key='AIzaSyBCqMzTBiROM7g3PcHaG-PY2vTqXYYtWhU')
    lat = []
    lng = []
    for adress in branche:
        adressen = gmaps.geocode(adress.firm_adress + ' ' + adress.firm_plz)
        lat.append(adressen[0]['geometry']['location']['lat'])
        lng.append(adressen[0]['geometry']['location']['lng'])
    return (lat, lng)

def show(request, name):

    n = name
    print(n)
    U = Firmeneintrag()
    f = U.loadFirma(n)

    geocode[n] = latLng(f)
    lat, lng = geocode[n]
    contacts = U.pagi(request, f)
    anz = counter(f)

    form = Anfrage()
    if request.POST:
        form = Anfrage(request.POST)
        if form.is_valid():
            form.save(commit=True)

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
        contacts = U.pagi(request, firm_list)

        context = {
            'title': n,
            'firma': firm_list,
            'firma': contacts,
            'form': form,
            'lat': lat,
            'lng': lng,
            'anz': anz,
        }

        return render(request, 'branchen/show.html', context)

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

def index(request):

    if request.POST:
        s = request.POST.get("select")
        q = request.POST.get("query")

        if s == 'X':
            return render(request, 'home.html')
        if q < '1000' or q > '10000':
            print('false!!')

        x = Firmeneintrag()
        indexFirm = x.loadFirma(s)

        geocode[s] = latLng(indexFirm)
        lat, lng = geocode[s]
        contacts = x.pagi(request, indexFirm)
        anz = counter(indexFirm)

        form = Anfrage()
        if request.POST:
            form = Anfrage(request.POST)
            if form.is_valid():
                form.save(commit=True)

        if q:
            query = int(q)
            search = Search()
            firm_list = search.plz(query, s)
            contacts = x.pagi(request, firm_list)

            context = {
                'title': s,
                'firma': firm_list,
                'firma': contacts,
                'form': form,
                'lat': lat,
                'lng': lng,
                'anz': anz,
            }

            return render(request, 'branchen/show.html', context)

        context = {
            'title': s,
            'firma': x,
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