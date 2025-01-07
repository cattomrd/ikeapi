import shutil
import os

def compare_files(file1,file2):
    try:
        # Abrir ambos archivos en modo binario
        with open(file1, 'rb') as f1, open(file2, 'rb') as f2:
            while True:
                # Leer en bloques para manejar archivos grandes
                bloque1 = f1.read(4096)
                bloque2 = f2.read(4096)
                # Comparar bloques
                if bloque1 != bloque2:
                    #print("Los archivos no son iguales")
                    return False
                # Si ambos bloques están vacíos, se llegó al final de los archivos
                if not bloque1 and not bloque2:
                    break
        #print("Los archivos son iguales.")
        return True
    except Exception as e:
        print(f"Ocurrió un error al comparar los archivos: {e}")


compare_files(file1="../files_temp/lista.txt", file2="../listas_sync/lista.txt")


def compare_lista(lista1, lista2):
    try:
        # Abrir ambos archivos en modo binario
        with open(lista1, 'rb') as f1, open(lista2, 'rb') as f2:
            while True:
                # Leer en bloques para manejar archivos grandes
                bloque1 = f1.read(4096)
                bloque2 = f2.read(4096)
                # Comparar bloques
                if bloque1 != bloque2:
                    #print("Los archivos no son iguales")
                    return False
                # Si ambos bloques están vacíos, se llegó al final de los archivos
                if not bloque1 and not bloque2:
                    break
        #print("Los archivos son iguales.")
        return True
    except Exception as e:
        print(f"Ocurrió un error al comparar los archivos: {e}")

def copy_file(file1, file2):
    try:
        # Verificar si el archivo de origen existe
        if not os.path.exists(file1):
            print(f"El archivo '{file1}' no existe.")
            return

        # Crear el directorio de destino si no existe
        if not os.path.exists(os.path.dirname(file2)):
            os.makedirs(os.path.dirname(file2))

        # Mover el archivo
        shutil.copy(file1, file2)
        print(f"Archivo copiado de '{file1}' a '{file2}'.")
    except Exception as e:
        print(f"Ocurrió un error al mover el archivo: {e}")

#compare_files()