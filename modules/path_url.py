from delete_list import borrar_contenido_directorio
from wget import download_lista, download_m3u,leer
from compare_files import copy_file
from sync_file import sync_files_from_list
from compare_files import compare_files

url_lista = 'https://debianraspberry.ikeasi.com/vendors/ubicacionrp/172-19-14-14_lista.txt'
save_as_list = '../files_temp/lista.txt'
download_lista(url_lista,save_as_list)

# link1 = leer(save_as_list)
# link2 = str(link1)
# url_m3u = f"https://debianraspberry.ikeasi.com/vendors/ubicacionrp/listas/{link2}"
# save_m3u = '../files_temp/lista.m3u'
# download_m3u(url_m3u,save_m3u)

server = '192.168.152.43'
# #borrar_contenido_directorio(ruta_directorio="../files_temp")

# ##DESCARGAR NOMBRE DE LISTA##
# estado_list_tmp = compare_files(file1="../files_temp/lista.txt", file2="../listas_sync/lista.txt")
estado_m3u = compare_files(file1="../files_temp/lista.m3u", file2="../listas_sync/lista.m3u")
estado_list = compare_files(file1="../files_temp/lista.txt", file2="../listas_sync/lista.txt")


# if estado_list and estado_m3u == True: 
#     print("NO DESCARGAR LISTA NI VIDEOS")
# elif estado_list == False:
#     print("DESCARGAR LISTA Y VIDEOS")

def validar_contenidos(estado_list):
    if estado_list == True: 
            print("Lista actualzada")
            return "Lista actualizada"
    else:
        url_lista = 'https://debianraspberry.ikeasi.com/vendors/ubicacionrp/172-19-14-33_lista.txt'
        save_as_list = '../files_temp/lista.txt'
        download_lista(url_lista,save_as_list)
        copy_file(file1="../files_temp/lista.txt", file2="../listas_sync/lista.txt")
        ##############################################################################
        ### DESCARGAR LISTA DE REPRODUCCION Y VIDEOS
        link1 = leer(save_as_list)
        link2 = str(link1)
        url_m3u = f"https://debianraspberry.ikeasi.com/vendors/ubicacionrp/listas/{link2}"
        save_m3u = '../files_temp/lista.m3u'
        print(url_m3u)
        download_m3u(url_m3u,save_m3u)
        copy_file(file1="../files_temp/lista.m3u", file2="../listas_sync/lista.m3u")
        borrar_contenido_directorio(ruta_directorio="../videos")
        sync_files_from_list(save_m3u, server, "comun", "../videos", options=None)              
        ############################################################################


validar_contenidos(estado_list)

match estado_list:
    case True:
        print("True")
    case False:
        print("False")
    case _:
        print("no existe")