import subprocess
import argparse

def sync_files_from_list(file_list, remote_server, remote_zone, local_destination, options=None):
    """
    Sincroniza archivos desde una zona común en un servidor remoto leyendo una lista de archivos.
    
    :param file_list: Ruta del archivo que contiene la lista de archivos a sincronizar.
    :param remote_server: Dirección del servidor remoto (e.g., host.com).
    :param remote_zone: Ruta base en la zona común del servidor remoto.
    :param local_destination: Ruta local donde se descargarán los archivos.
    :param options: Lista de opciones para rsync (opcional).
    """
    if options is None:
        options = ["-avz"]  # Opciones predeterminadas
    
    try:
        # Leer la lista de archivos
        with open(file_list, "r") as file:
            files = [line.strip() for line in file if line.strip()]
        
        for file_name in files:
            # Construir la ruta completa del archivo remoto
            remote_file = f"rsync://{remote_server}/{remote_zone}/{file_name}"
            command = ["rsync"] + options + [remote_file, local_destination]
            
            print(f"Sincronizando: {remote_file} -> {local_destination}")
            result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            
            # Mostrar salida y errores
            print(result.stdout)
            if result.stderr:
                print(f"Errores al sincronizar {file_name}:", result.stderr)
    
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")

if __name__ == "__main__":
    # Configurar el analizador de argumentos
    parser = argparse.ArgumentParser(description="Sincroniza archivos desde una zona común de un servidor rsync leyendo una lista de archivos.")
    parser.add_argument("file_list", help="Archivo que contiene la lista de archivos a sincronizar.")
    parser.add_argument("remote_server", help="Servidor remoto (e.g., host.com).")
    parser.add_argument("remote_zone", help="Zona común en el servidor remoto.")
    parser.add_argument("local_destination", help="Directorio local donde se descargarán los archivos.")
    parser.add_argument("-o", "--options", nargs="*", default=["-avz"], 
                        help="Opciones adicionales para rsync (e.g., -a, -v, -z).")
    
    # Parsear los argumentos
    args = parser.parse_args()
    
    # Llamar a la función de sincronización
    sync_files_from_list(args.file_list, args.remote_server, args.remote_zone, args.local_destination, args.options)
