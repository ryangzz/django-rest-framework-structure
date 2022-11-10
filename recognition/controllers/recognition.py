from contextlib import nullcontext
from django.http import JsonResponse
import speech_recognition as sr
import time
import base64
import os
class Reconnition():
    solicitud       = nullcontext
    method          = nullcontext
    method          = nullcontext
    reconocimiento  = nullcontext

    def __init__(self, request, method): 
        self.solicitud      = request
        self.method         = method
        self.reconocimiento = sr.Recognizer()

    def recognition_voice_source(self):
        error = 'false'
        texto = ''
        try:
            with sr.AudioFile(self.solicitud.POST['audio']) as archivo:
                audio = self.reconocimiento.record(archivo) 
            texto = self.reconocimiento.recognize_google(audio, language='es-MX')
            error = 'false'
        except Exception as e: # work on python 3.x
            error = 'true'
            texto = str(e)
        return JsonResponse({'texto': texto, 'error':error}, safe=False, status=200)

    def recognition_voice_base64(self, base64P ='', filenameP = ''):
        error       = 'false'
        filename    = str(time.time())+filenameP
        texto       = ''
        try:
            # try:
            #     decode_bytes = base64.b64decode(base64P)                
            #     audio = self.reconocimiento.record(b''+decode_bytes)
            #     audio = sr.AudioData(decode_bytes)
            #     texto = self.reconocimiento.recognize_google(audio, language='es-MX')
            # except Exception as e: # work on python 3.x
            #     error = 'true'
            #     texto = str(e)
            decode_bytes = base64.b64decode(base64P)
            with open(filename, "wb") as wav_file:
                    wav_file.write(decode_bytes)
            with sr.AudioFile(filename) as archivo:
                    audio = self.reconocimiento.record(archivo) 
            texto = self.reconocimiento.recognize_google(audio, language='es-MX')
            error = 'false'
            os.remove(filename)
        except Exception as e: # work on python 3.x
            error = 'true'
            texto = str(e)
        return JsonResponse({'texto': texto, 'error':error}, safe=False, status=200)