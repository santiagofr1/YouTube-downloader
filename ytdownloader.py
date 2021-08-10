from pytube import YouTube
from pytube.request import stream
from pytube.cli import on_progress

datoformato=0
contador=0
print("--------------Convertidor de YouTube--------------")

#importa el url y la funcion de la barra de carga
url=input("URL: ")
yt = YouTube(url, on_progress_callback=on_progress) 
nombre=yt.title

#el usuario elige el formato + control de errores
while datoformato == 0:          
    print("Elija el formato: 1-mp4, 2-mp3")
    datoformato=input("Formato: ")
    try:
        datoformato=int(datoformato)
        if datoformato != 1 or datoformato != 2:
            datoformato=0
    except:
        print("debe ingresar un numero")


#se elige la calidad del archivo + control de errores, y se busca y almacena el archivo a descargar
if datoformato==1 :         
    calidad=0                  
    while calidad==0:
        print("Calidad: 1-720, 2-1080 ")
        calidad=input("Calidad: ")
        try:
            calidad=int(calidad)
            if calidad != 1 or calidad != 2:
                print("ingrese un numero valido")   
                calidad=0             
        except:
            print("debe ingresar un numero")    
    stream=yt.streams.filter(resolution=("720p" if calidad==1 else "1080p"))
else:
    stream=yt.streams.get_by_itag(251)

print("Preparando descarga...")

#se elige si cambiar o no el nombre por defecto
while True:                 
    print("El archivo se llamara: " + nombre)
    change=input("Desea cambiarlo? y/n ").lower()    
    if change != "y" and change != "n":
        print("opcion incorrecta")
    elif change=="y":
        nombre=input("Nuevo nombre: ")
    break

#se descarga y muestra la barra de descarga o da error y cierra
try:       
    print("Descargando: ")                         
    if datoformato==1: stream.first().download(filename=nombre + ".mp4")
    else: stream.download(filename=nombre + ".mp3")
    print("")
    print("Descarga exitosa")
except:
    print("el video no esta disponible en esa calidad o formato")