from datetime import datetime
from re import TEMPLATE
from django.http import HttpResponse
from django.template import Template, Context,loader

class personas(object):
    def __init__(self,nombre, apellido,parentesco):
        self.nombre=nombre
        self.apellido=apellido
        self.parentesco=parentesco
        


def family(request):

    dia = datetime.now()

    p1=personas("Cynthia", "Cruz","Wife")
    p2=personas("Luis", "Motomochi","Son")
    p3=personas("Aurora","Flores", "Mother")
    

    doc_info=open("C:/Users/Familia Motomochi/Desktop/python/mi_primer_mvt/MVT_Luis_Motomochi/MVT_Luis_Motomochi/templates/templates.html")

    template1=Template(doc_info.read())

    doc_info.close()

    ctx=Context({"person_name":p1.nombre,"last_name":p1.apellido,"relative":p1.parentesco,
    "person_name2":p2.nombre,"last_name2":p2.apellido,"relative2":p2.parentesco,"person_name3":p3.nombre,
    "last_name3":p3.apellido,"relative3":p3.parentesco,"hora":dia})


    documento=template1.render(ctx)


    return HttpResponse(documento)


def bienvenida(request):
    return HttpResponse("Te doy la bienvenida a mi primer sitio web")


def diaDeHoy(request):
    dia = datetime.now()

    documentoDeTexto = f"Hoy es día: <br> {dia}"

    return HttpResponse(documentoDeTexto)