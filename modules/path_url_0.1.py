from wget import download_lista, download_m3u, leer
from sync_file import sync_files_from_list
from delete_list import Borrar, borrar_contenido_directorio
from compare_files import compare_files,copy_file, compare_lista
from get_ipaddress import get_ip_address

server ="192.168.152.43"
ip_address = get_ip_address()
def descargar_lista():
    url_lista = f"https://debianraspberry.ikeasi.com/vendors/ubicacionrp/{ip_address},'+'_lista.txt'"
    save_as_list = '../files_temp/lista.txt'
    download_lista(url_lista,save_as_list)

descargar_lista()

def descargar_m3u():
        save_as_list = '../files_temp/lista.txt'
        link1 = leer(save_as_list)
        link2 = str(link1)
        url_m3u = f"https://debianraspberry.ikeasi.com/vendors/ubicacionrp/listas/{link2}"
        save_m3u = '../files_temp/lista.m3u'
        download_m3u(url_m3u,save_m3u)
descargar_m3u()


estado_list = compare_files(file1="../files_temp/lista.txt", file2="../listas_sync/lista.txt")
estado_m3u = compare_files(file1="../files_temp/lista.m3u", file2="../listas_sync/lista.m3u")

def update_lista(estado_list):
    if estado_list == True:
        print("lista valida valida")
    else:
        descargar_lista()
        copy_file(file1="../files_temp/lista.txt", file2="../listas_sync/lista.txt")
        descargar_m3u()

def update_m3u(estado_m3u):
    if estado_m3u == True:
        print("lista M3U valida valida")
    else:
        descargar_lista()
        copy_file(file1="../files_temp/lista.m3u", file2="../listas_sync/lista.m3u")
        descargar_m3u()
        save_m3u = '../files_temp/lista.m3u'
        borrar_contenido_directorio(ruta_directorio="../videos")
        sync_files_from_list(save_m3u, server, "comun", "../videos", options=None)  

update_lista(estado_list)
update_m3u(estado_m3u)