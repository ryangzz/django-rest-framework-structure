from django.urls import path, re_path
from . import views

urlpatterns = [
    # path('voice-text/internal', views.reconocimiento, name = 'voz'),
    path('voice-text/', views.reconocimiento, name = 'voz'),
    re_path(r'^voice-text/(?P<param>(internal))', views.reconocimiento),

]
