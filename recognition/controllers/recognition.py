from contextlib import nullcontext
from django.http import JsonResponse
import speech_recognition as sr
import time
import base64
import os
class Reconnition():
    reconocimiento  = nullcontext

    def __init__(self): 
        self.reconocimiento = sr.Recognizer()

    def recognition_voice_source(self, audioPath):
        error = 'false'
        texto = ''
        try:
            with sr.AudioFile(audioPath) as archivo:
                audio = self.reconocimiento.record(archivo) 
            texto = self.reconocimiento.recognize_google(audio, language='es-MX')
            error = 'false'
        except Exception as e:
            error = 'true'
            texto = str(e)
        return JsonResponse({'texto': texto, 'error':error}, safe=False, status=200)

    def recognition_voice_base64(self, base64P ='', filenameP = ''):
        error       = 'false'
        filename    = str(time.time())+filenameP
        texto       = ''
        try:
            decode_bytes = base64.b64decode(base64P)
            with open(filename, "wb") as wav_file:
                    wav_file.write(decode_bytes)
            with sr.AudioFile(filename) as archivo:
                    audio = self.reconocimiento.record(archivo) 
            texto = self.reconocimiento.recognize_google(audio, language='es-MX')
            error = 'false'
            os.remove(filename)
        except Exception as e:
            error = 'true'
            texto = str(e)
        return JsonResponse({'texto': texto, 'error':error}, safe=False, status=200)