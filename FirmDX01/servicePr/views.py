from django.core.mail import send_mail
from django.core.mail import send_mass_mail
from django.shortcuts import render
from servicePrMail.forms import EintragFormular, Anfrage
from .firm import Firmeneintrag_new
from search import search_plz
from googleMapsAPI.geocoords import GeoCoords
from .models_new import Firma
import random

geocode = dict()
firm_list = Firma.objects.all()
geo = GeoCoords()
geocode = geo.getAllGeocoords(firm_list)

def index(request):

    firma = Firmeneintrag_new()
    global firm_list

    if request.POST:
        try:
            s = request.POST.get('select')
            q = request.POST.get('query')
        except:
            print("ERROR")

        if s == 'X':
            return render(request, 'home.html')

        firma_new = firma.getFirm(s, firm_list)
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
    global firm_list

    req_name = request.POST.get("name")
    q = request.POST.get("query")

    firma = Firmeneintrag_new()
    firma_new = firma.getFirm(n, firm_list)

    # f = random.sample(firma_new, len(firma_new))
    f = firma_new
    lat, lng = geocode[n]

    pagi = firma.pagi(request, f)
    anz = counter(f)

    form = Anfrage()
    if req_name:
        form = Anfrage(request.POST)
        if form.is_valid():
            mail_list = request.POST.get("mailList")
            mailList = mail_list.split(" ")
            del mailList[0]

            subject = request.POST.get("name")
            message = request.POST.get("beschreibung")
            send_from = 'test@mail.com'

            m = 0
            while m < len(mailList):
                send_mail(subject, message, send_from, [mailList[m]])
                m = m+1

            form.save(commit=True)

    if q:
        y = int(q)

        if q == '' or y < 1000 or y > 10000:
            context = {
                'title': n,
                'fi': list(f),
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

        lat, lng = geocode[n]

        context = {
            'title': n,
            'fi': list(f),
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
        'fi': list(f),
        'firma_new': f,
        'firma_new': pagi,
        'form': form,
        'lat': lat,
        'lng': lng,
        'anz': anz,
    }

    return render(request, 'branchen/show.html', context)

def impressum(request):

    context = {
        'title': 'Impressum',
    }

    return render(request, 'nav/impressum.html', context)


def aboutUs(request):
    context = {
        'title': 'About us',
    }

    return render(request, 'nav/aboutUs.html', context)


def agb(request):
    context = {
        'title': 'AGB',
    }

    return render(request, 'nav/agb.html', context)

def kontakt(request):
    context = {
        'title': 'Kontakt',
    }

    return render(request, 'nav/kontakt.html', context)


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