from django.urls import path, re_path
from . import views

urlpatterns = [
    path('traerImg', views.traerImg, name = 'traerImg'),
    path('infoDoc', views.infoDoc, name = 'infoDoc'),
    path('descargaDoc', views.descargaDoc, name = 'descargaDoc')
]