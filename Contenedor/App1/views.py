from django.core.serializers import serialize
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import AutorDb, FraseDb
#from django.http import HttpResponse

def IndexView(request):
    
    objeto = AutorDb.objects.filter(nombre="Hola").order_by("-id")
    
    return render(request, "index.html", {"objeto":objeto})

def AutorView(request, id):
    autor = get_object_or_404(AutorDb, id=id)    
    return render(request, "autor.html", {"objeto":autor})
    

#Vistas API

def AutorAPIxml(request):
    autores = AutorDb.objects.all()
    autores_serializados = serialize('xml', autores)
    return HttpResponse(autores_serializados, content_type='text/xml')

def AutorAPIjson(request):
    autores = AutorDb.objects.all()
    autores_serializados = serialize('json', autores)
    return HttpResponse(autores_serializados, content_type='text/json')

