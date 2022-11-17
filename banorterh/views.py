from django.http import JsonResponse
from .controllers.banorterh import BanorteRh
from django.views.decorators.http import require_GET, require_POST
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

@require_POST
@csrf_exempt
def extraccion(request):
    if 'source' not in request.POST:
        return JsonResponse({'msg': 'Params Incomplete', 'error':'true'}, safe=False, status=401)
    banorte  =  BanorteRh()
    return banorte.scandir(request.POST['source'])

@require_POST
@csrf_exempt
def copiado(request):
    if 'data' not in request.POST:
        return JsonResponse({'msg': 'Params Incomplete', 'error':'true'}, safe=False, status=401)
    if 'folder' not in request.POST:
        return JsonResponse({'msg': 'Params Incomplete', 'error':'true'}, safe=False, status=401)
    data     = json.loads(request.POST['data'])
    banorte  =  BanorteRh()
    return banorte.copiado(data, request.POST['folder'])

@require_POST
@csrf_exempt
def nofound(request):
    if 'data' not in request.POST:
        return JsonResponse({'msg': 'Params Incomplete', 'error':'true'}, safe=False, status=401)
    data     = json.loads(request.POST['data'])
    banorte  =  BanorteRh()
    return banorte.nofound(data)
 