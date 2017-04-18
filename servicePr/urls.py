from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^umzug/', views.umzug, name="umzug"),
    url(r'^reinigung/', views.reinigung, name="reinigung"),
    url(r'^baufirma/', views.baufirma, name="baufirma"),
    url(r'^catering/', views.catering, name="catering"),
    url(r'^gartenbau/', views.gartenbau, name="gartenbau"),
    url(r'^immobilien/', views.immobilien, name="immobilien"),
    url(r'^sanitaer/', views.sanitaer, name="sanitaer"),
    url(r'^architekt/', views.architekt, name="architekt"),
    url(r'^schreiner/', views.schreiner, name="schreiner"),
    url(r'^maler/', views.maler, name="maler"),
    url(r'^anmelden/', views.firmaForm, name="firmaForm"),
    url(r'^search/', views.filter, name="filter"),
]
