from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^vendor$', VendorList.as_view()),
    url(r'^vendor/(?P<pk>[0-9]+)$', VendorDetalhes.as_view()),
    url(r'^citys$', CityList.as_view()),
    url(r'^citys/(?P<pk>[0-9]+)$', CityDetalhes.as_view()),
]