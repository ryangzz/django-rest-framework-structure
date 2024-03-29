
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('projects.urls')),
    path('reconocimiento/', include('recognition.urls')),
    path('', include('banorterh.urls')),
    path('vision/', include('vision.urls')),
    path('fiduciariio/', include('fiduciariio.urls')),
]
