from urllib import response
from django.shortcuts import render
from django import http
from django.http import HttpResponse
from .controllers.recognition import Reconnition
from django.views.decorators.http import require_GET, require_POST
from django.views.decorators.csrf import csrf_exempt
import json


@require_POST
@csrf_exempt
def reconocimiento(request, param = 'external'):
    reconocimiento  = Reconnition(request, param)
    response        = None
    if param == 'external':
        params      = json.loads(request.body)
        response    = reconocimiento.recognition_voice_base64(params['audio'], params['name'])
        return response
    else:
        response = reconocimiento.recognition_voice_source()
    return response
