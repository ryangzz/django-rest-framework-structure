from django.urls import path, re_path
from . import views

urlpatterns = [
    path('banorterh/extraccion', views.extraccion, name = 'extraccion'),
    path('banorterh/copiado', views.copiado, name = 'copiado'),
    path('banorterh/nofound', views.nofound, name = 'nofound'),
]
