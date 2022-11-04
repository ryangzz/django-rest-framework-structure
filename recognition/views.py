from django.shortcuts import render
from django import http
from django.http import HttpResponse
from .controllers.recognition import Reconnition
from django.views.decorators.http import require_GET, require_POST
from django.views.decorators.csrf import csrf_exempt


@require_POST
@csrf_exempt
def reconocimiento(request):
    reconocimiento = Reconnition(request)
    return reconocimiento.recognition_voice()