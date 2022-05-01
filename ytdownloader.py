 # imports
from pytube import YouTube
from pytube.request import *
from pytube.cli import  on_progress
from pytube import Playlist
from getpass import getuser
import os

usuario = getuser()

print("----- Convertidor 3 -------")

# Control de disponibilidad del Url, retorna:
#       error = 1 si la Url ingresada no esta disponible
#       error = None si la Url esta disponible
#       video = True si es video
#       video = False si es playlist
def controlUrl(url):
    error = 0
    video = False
    if url.find("playlist") >= 0: 
        video = False
        return error, video
    else:
        yt = YouTube(url,on_progress_callback=on_progress)
        try:
            yt.check_availability()
            video = True
            return error, video
        except Exception as e:
            error = str(e)
            return error, video

# Creacion de la carpeta donde se descargaran los archivos
# Ruta predeterminada: Descargas
def pathtoDownload(newPath):
    if len(newPath) == 0:
        newPath = "C:/Users/" + usuario + "/Downloads/Musica/"
        if os.path.exists(newPath) == False:
            os.mkdir(newPath)
    else:
        if os.path.exists(newPath) == False:
            os.mkdir(newPath)
    return newPath

# Obtiene el Stream
# Descarga el Stream
def download(format,newName,newPath,calidad):
    try:
        if format == str(1):
            stream = yt.streams.filter(resolution = ("720" if calidad == str(2) else "1080"))
        else:
            stream = yt.streams.get_by_itag(251)
        if format == str(1):
            stream.first().download(filename = newName + ".mp4", output_path = newPath)
        else:
            stream.download(filename=newName + ".mp3", output_path = newPath)
    except Exception as e:
        print(e)
    
#--------------main loop-----------
while True:
    calidad = 0
    url = input("URL: ")
    error, video = controlUrl(url)
    if error != 0:
        print(error)
        break
    newPath = input("Desea cambiar la ruta de descarga? \nEnter para descargar en Descargas/Musica: ")
    newPath = pathtoDownload(newPath)
 
    while format != str(1) and format != str(2) :
        print("Elija el formato: 1-mp4, 2-mp3")
        format = input("Fortmato: ")
    if format == str(1):
        while calidad != str(1) and calidad != str(2) :
            print("Elija la calidad: 1-1080, 2-720")
            calidad = input("Calidad: ")  
    if video == True:
        yt = YouTube(url,on_progress_callback=on_progress)
        print("El nombre del video es " + yt.title)
        newName = input("Si desea cambiar el nombre ingreselo \nEnter si no desea cambiar el nombre: ")
        if len(newName) == 0:
            newName = yt.title
        print("Descargand...")
        download(format,newName,newPath,calidad)
    else:
        playlist = Playlist(url)
        toDownload = playlist.video_urls[:len(playlist)]
        for url in playlist.video_urls[:len(playlist)]:
            try:
                yt = YouTube(url,on_progress_callback=on_progress)
                yt.check_availability()
                print("Descargando: " + newName)
            except Exception as e:
                error = True
                print(e)
            if error == False:
                newName = yt.title
                download(format,newName,newPath,calidad)        
