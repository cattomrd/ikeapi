import os, shutil

#path_delete = "../listas_sync"
def Borrar(path_delete):
    try:
        # Verificar si el directorio existe
        if not os.path.exists(path_delete):
            print(f"El directorio '{path_delete}' no existe.")
            return

        # Iterar sobre el contenido del directorio
        for elemento in os.listdir(path_delete):
            ruta_elemento = os.path.join(path_delete, elemento)

            # Si es un archivo, eliminarlo
            if os.path.isfile(ruta_elemento) or os.path.islink(ruta_elemento):
                os.unlink(ruta_elemento)
            # Si es un directorio, eliminarlo recursivamente
            elif os.path.isdir(ruta_elemento):
                shutil.rmtree(ruta_elemento)

        print(f"Todo el contenido del directorio '{path_delete}' ha sido eliminado.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")


def borrar_contenido_directorio(ruta_directorio):
    try:
        # Verificar si el directorio existe
        if not os.path.exists(ruta_directorio):
            print(f"El directorio '{ruta_directorio}' no existe.")
            return

        # Iterar sobre los elementos dentro del directorio
        for elemento in os.listdir(ruta_directorio):
            ruta_elemento = os.path.join(ruta_directorio, elemento)

            # Si es un archivo, eliminarlo
            if os.path.isfile(ruta_elemento) or os.path.islink(ruta_elemento):
                os.unlink(ruta_elemento)
            # Si es un directorio, eliminarlo recursivamente
            elif os.path.isdir(ruta_elemento):
                shutil.rmtree(ruta_elemento)

        print(f"Todo el contenido del directorio '{ruta_directorio}' ha sido eliminado.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")
