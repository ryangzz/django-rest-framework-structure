from contextlib import nullcontext
from django.http import JsonResponse
import os, json, pathlib, time, math, shutil

class BanorterhFiles():
    respuesta  = nullcontext
    error      = ''

    def getFileBase64():
        error = 'false'
        
        return JsonResponse({'file': file, 'error':error}, safe=False, status=200)

    