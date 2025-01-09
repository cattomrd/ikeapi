import pycurl
import urllib.request
import subprocess

## Funcion para descargar lista
def download_lista(url_lista, save_list):
    with open(save_list, 'wb') as file:
        curl = pycurl.Curl()
        curl.setopt(curl.URL, url_lista)
        curl.setopt(curl.WRITEDATA, file)
        curl.perform()
        curl.close()

## Leer el contenido de la lista para poder concatenar con la url del servidor
def leer(contenido):
    try:
        with open(contenido, 'r') as archivo:
            contenido = archivo.read()
        return contenido
    except FileNotFoundError:
        #print(f"El archivo '{contenido}' no se encontró.")
        return None

# Descartar lista m3u
def download_m3u(url_m3u,save_m3u):
    urllib.request.urlretrieve(url_m3u,save_m3u)

def download_with_wget(url_lista, save_list=None):
    options = "--no-check-certificate -P" 
    try:
        # Construir el comando wget
        command = ["wget",options,url_lista]
        if save_list:
            command += ["-O", save_list]  # Especificar la ruta de destino
        
        # Ejecutar el comando
        subprocess.run(command, check=True)
        print(f"Archivo descargado con éxito desde: {url}")
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar wget: {e}")
    except FileNotFoundError:
        print("Error: 'wget' no está instalado en el sistema.")
        
        

# download_lista(url = 'https://debianraspberry.ikeasi.com/vendors/ubicacionrp/172-19-14-14_lista.txt', save_list = '../files_temp/lista.txt')
