from django.urls import path
from .views import IndexView, AutorView, AutorAPIxml, AutorAPIjson


urlpatterns = [
    path('', IndexView),
    path('autor/<int:id>', AutorView),
    path('api/listado-autores-xml/', AutorAPIxml, name='autor_xml'),
    path('api/listado-autores-json/', AutorAPIjson, name='autor_json')
]
