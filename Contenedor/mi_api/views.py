from django.shortcuts import render
from rest_framework import generics     
from rest_framework import viewsets
from App1.models import AutorDb, FraseDb
from .serializers import AutorDbSerialiazer, FraseDbSerializer, AutorConFraseSerliazer


# Create your views here.
class AutorDbApiList(generics.ListAPIView):
    queryset = AutorDb.objects.all()
    serializer_class = AutorDbSerialiazer

class AutorConFraseDbApiList(generics.ListAPIView):
    queryset = AutorDb.objects.all()
    serializer_class = AutorConFraseSerliazer
    
class AutorDbApiCreate(generics.CreateAPIView):
    queryset = AutorDb.objects.all()
    serializer_class = AutorDbSerialiazer
    
class AutorDbApiRetrieve(generics.RetrieveAPIView):
    queryset = AutorDb.objects.all()
    serializer_class = AutorDbSerialiazer
    
#VIEWSETS

class FraseDbViewSet(viewsets.ModelViewSet):
    queryset = FraseDb.objects.all()
    serializer_class = FraseDbSerializer