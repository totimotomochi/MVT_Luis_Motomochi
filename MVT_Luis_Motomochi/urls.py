
from ast import Import
from django.contrib import admin
from django.urls import path

from MVT_Luis_Motomochi.views import (
    family,
    bienvenida,
    diaDeHoy,)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('family/', family),
    path('bienvenida/',bienvenida),
    path('diaDeHoy/',diaDeHoy)
    
]
