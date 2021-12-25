from pytube import YouTube
from pytube.request import stream
from pytube.cli import download_caption, on_progress


print("--------------Convertidor de YouTube 2--------------")

dcalidad=0

#seleccion del formato
def formato(url):
    while True:
        print("Elija el formato: 1-mp4, 2-mp3")
        dformato = input("Formato: ")
        if dformato == str(1) or dformato == str(2):
            return dformato
        else:
            print("Ingrese una opcion valida")


#se selecciona calidad de descarga de mp4
def calidad(url): #si se da el enter sin nada se descarga igual
    while True:
        print("En que calidad desea descargar su archivo: 1-720, 2-1080")
        dcalidad=input("Calidad: ")
        if dcalidad != str(1) and dcalidad != str(2):
            print("Ingrese una opcion valida")
        else:
            return dcalidad

#se obtiene el stream
def captura(dformato, dcalidad):
    try:
        if dformato == str(1):
            stream=yt.streams.filter(resolution=("720p" if dcalidad == str(1) else "1080p"))
        else:
            stream=yt.streams.get_by_itag(251)
    except:
        print("Hubo un problema al obtener su video")
        stream = 0
    return stream

#se le asigna un nombre
def nombre(dnombre):
    print("El nombre del archivo sera: " +  dnombre)
    print("Desea cambiarlo?")
    while True:
        change=input("Y/N: ")
        if change.lower() == "y":
            dnombre=input("nuevo nombre: ") 
            break  
        elif change.lower() == "n":
            dnombre=yt.title
            break
        else:
            print("Ingrese una opcion valida")
            continue
    return dnombre


#se descarga 
def descarga(dformato, dnombre):
    print("Descargando...")
    try:
        if dformato == str(1):
            stream.first().download(filename = dnombre + ".mp4")
        else:
            stream.download(filename = dnombre + ".mp3")
        print("")
        print("Descagra exitosa")
        print("")
    except:
        print("Hubo un problema al intentar descargar su archivo")
        return
   

def repetision():
    while True:
        print("Desea descargar otro archivo?") 
        change=input("Y/N ")
        if change.lower() == "n":
            print("Finalizando ejecucion")
            exit()
        elif change.lower() == "y":
            return
        else:
            print("Opcion invalida")



#main loop
while True:
    url = input("URL: ")

    try:
        yt = YouTube(url, on_progress_callback=on_progress) 
        dnombre = yt.title
    except:
        print("hubo un problema con su link")
        break

    dformato = formato(url)
    if dformato == str(1):
        dcalidad = calidad(url)
    stream = captura(dformato, dcalidad)
    dnombre = nombre(dnombre) 
    descarga(dformato, dnombre)

    repetision()