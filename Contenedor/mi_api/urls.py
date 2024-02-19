from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    AutorDbApiList, 
    AutorDbApiCreate,
    AutorDbApiRetrieve,
    AutorConFraseDbApiList,
    FraseDbViewSet,
)

router = DefaultRouter()
router.register('frases', FraseDbViewSet, basename='frases')

urlpatterns = [
    path('autores-list/', AutorDbApiList.as_view(), name='autores_list'),
    path('autores-frases/', AutorConFraseDbApiList.as_view(), name="autores_frase"),
    path('autores-create/', AutorDbApiCreate.as_view(), name='autores_create'),
    path('autores-retrieve/<int:pk>/', AutorDbApiRetrieve.as_view(), name="autores_retrieve"),
]

urlpatterns += router.urls
