from urllib import response
from django.shortcuts import render
from django import http
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.http import require_GET, require_POST
from django.views.decorators.csrf import csrf_exempt
import os
from PIL import Image
import base64
from base64 import b64encode
import json
import fitz
import PyPDF2
from datetime import datetime

# import module
from pdf2image import convert_from_path


@require_POST
@csrf_exempt
def traerImg(request):
    ruta='/home/desarrollo/servidor/'+request.POST['ruta']
    nameFile=request.POST['nameFile']
    pagina=request.POST['pagina']
    images = convert_from_path(ruta+nameFile,dpi=200,size=(800,1024))
    output=ruta+'tmp/page'+ str(int(pagina)-1) +'.png'
    images[int(pagina)-1].save(output, 'PNG')

    verarchivo = open(output,'rb')
    verpdf = verarchivo.read()
    base64pdf = b64encode(verpdf).decode('utf-8')
    verarchivo.close()

    return JsonResponse({'error':False,'data':base64pdf}, safe=False, status=200)

@require_POST
@csrf_exempt
def infoDoc(request):
    ruta='/home/desarrollo/servidor/'+request.POST['ruta']
    nameFile=request.POST['nameFile']
    datosPdf = {}
    doc = fitz.open(ruta+nameFile)
    sizeFile = os.stat(ruta+nameFile).st_size
    print(doc.metadata)
    datosPdf["format"]=doc.metadata["format"]
    datosPdf["title"]=doc.metadata["title"]
    datosPdf["author"]=doc.metadata["author"]
    datosPdf["creator"]=doc.metadata["creator"]
    fechacreate=doc.metadata["creationDate"]
    fechacreate = datetime.strptime(fechacreate.replace("'", ""), "D:%Y%m%d%H%M%S%z")
    datosPdf["fechacreate"]=fechacreate

    fechamod=doc.metadata["modDate"]
    fechamod = datetime.strptime(fechamod.replace("'", ""), "D:%Y%m%d%H%M%S%z")
    datosPdf["moddate"]=fechamod
    hojas = len(doc)
    doc.close()
    datosPdf["hojas"]= hojas
    datosPdf["size"]= sizeFile

    return JsonResponse({'error':False,'data':datosPdf}, safe=False, status=200)

@require_POST
@csrf_exempt
def descargaDoc(request):
    ruta='/home/desarrollo/servidor/'+request.POST['ruta']
    nameFile=request.POST['nameFile']
    verarchivo = open(ruta+'/'+nameFile,'rb')
    verpdf = verarchivo.read()
    base64pdf = b64encode(verpdf).decode('utf-8')
    verarchivo.close()

    return JsonResponse({'error':False,'data':base64pdf}, safe=False, status=200)