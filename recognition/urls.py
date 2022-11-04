from django.urls import path, include
from . import views

urlpatterns = [
    path('voz/', views.reconocimiento, name = 'voz'),
]
