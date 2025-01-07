import pycurl
import urllib.request

## Funcion para descargar lista
def download_lista(url, save_list):
    with open(save_list, 'wb') as file:
        curl = pycurl.Curl()
        curl.setopt(curl.URL, url)
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



# download_lista(url = 'https://debianraspberry.ikeasi.com/vendors/ubicacionrp/172-19-14-14_lista.txt', save_list = '../files_temp/lista.txt')
