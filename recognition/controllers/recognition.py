from contextlib import nullcontext
from django import http
from django.http import HttpResponse, JsonResponse

class Reconnition():
    solicitud = nullcontext

    def __init__(self, request): 
        self.solicitud = request

    def recognition_voice(self):
        return JsonResponse({'texto': "Esto es un testo de prueba"}, safe=False, status=200)
         #HttpResponse("Hola")