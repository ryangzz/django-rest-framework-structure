from django.urls import path, re_path
from . import views

urlpatterns = [
    # path('voice-text/internal', views.reconocimiento, name = 'voz'),
    path('voice-text/', views.reconocimiento, name = 'voz'),
    re_path(r'^voice-text/(?P<param>(internal))', views.reconocimiento, name = 'voz'),
    path('voicetext/', views.reconocimiento_offline, name = 'vozSphinx'),
    path('voicetext/', views.reconocimiento_offline, name = 'vozSphinx'),
    re_path(r'^voicetext/(?P<param>(internal)|(external2))', views.reconocimiento_offline, name = 'vozSphinx'),
]
