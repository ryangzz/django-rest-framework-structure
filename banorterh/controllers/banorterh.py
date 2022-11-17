from contextlib import nullcontext
from django.http import JsonResponse
import os, json, pathlib, time, math, shutil

class BanorteRh():
    respuesta  = nullcontext
    error      = ''
    
    #def __init__(self): 

    def scandir(self, directory):
        dirs = self.scandir2(directory)
        return JsonResponse({'files':self.files, 'folders':self.folders,'root': dirs,'error':'false'}, safe=False, status=200)

    folders = 0
    files   = 0

    def scandir2(self, directory):
        tree    = [{'files':0, 'folders':0}]
        for i in os.scandir(directory):
            element = {}
            if i.is_dir():
                self.folders += 1
                tree[0]['folders'] += 1
                element['folder'] = {'type':'1', 'name':i.name, 'path':str(i.path), 'dirs':self.scandir2(str(i.path))}
            else:
                self.files += 1
                tree[0]['files'] += 1
                element['file'] = {'type':'2', 'name':i.name, 'path':str(i.path)}
            tree.append(element)
        return tree
    
    def copiado(self, data, folderP):
        error = 'false'
        texto = 'Todo Bien'
        dirs  = {}
        try:
            for folder in data:
                carpeta      = '//'+folderP+'/'+folder
                if not os.path.exists(carpeta):
                    os.mkdir(carpeta)
                filesNoFound = []
                for files in data[folder]:
                    # print(files)
                    if os.path.exists(files):
                        shutil.copy(files, carpeta)
                    else:
                        filesNoFound.append(files)
                if len(filesNoFound) > 0: 
                    dirs[folder] = filesNoFound
            error = 'false'
        except Exception as e:
            error = 'true'
            texto = str(e)
        return JsonResponse({'msg': texto,'error':error, 'notFound':dirs}, safe=False, status=200)

    def nofound(self, data):
        error = 'false'
        texto = 'Todo Bien'
        dirs  = {}
        try:
            for folder in data:
                filesNoFound = []
                for files in data[folder]:
                    # print(files)
                    if not os.path.exists(files):
                        filesNoFound.append(files)
                if len(filesNoFound) > 0: 
                    dirs[folder] = filesNoFound
            error = 'false'
        except Exception as e:
            error = 'true'
            texto = str(e)
        return JsonResponse({'msg': texto,'error':error, 'notFound':dirs}, safe=False, status=200)