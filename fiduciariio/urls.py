from django.urls import path, re_path
from . import views

urlpatterns = [
    path('testing/', views.testing, name = 'testing'),
]
