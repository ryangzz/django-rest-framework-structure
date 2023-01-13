from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_GET, require_POST
from django.views.decorators.csrf import csrf_exempt
from .controllers.files import File
# Create your views here.

@require_POST
@csrf_exempt
def testing(request):
    archivo = File()
    base64  = archivo.devolverbase64file(request.POST['archivo'])
    return JsonResponse({'file': base64, 'error':'error', 'audio':'audioPath'}, safe=False, status=401)
