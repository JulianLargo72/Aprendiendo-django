from django.shortcuts import render, get_object_or_404
from .models import AutorDb, FraseDb
#from django.http import HttpResponse

def IndexView(request):
    
    objeto = AutorDb.objects.filter(nombre="Hola").order_by("-id")
    
    return render(request, "index.html", {"objeto":objeto})

def AutorView(request, id):
    autor = get_object_or_404(AutorDb, id=id)    
    return render(request, "autor.html", {"objeto":autor})
    
