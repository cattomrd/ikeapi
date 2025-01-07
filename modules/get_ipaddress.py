import subprocess

def get_ip_address(interface="eth0"):
    try:
        # Ejecuta el comando para obtener la dirección IP
        result = subprocess.run(
            ["ip", "address", "show", interface],
            capture_output=True,
            text=True,
            check=True
        )
        # Busca la dirección IP en la salida
        for line in result.stdout.splitlines():
            if "inet " in line:
                # Extrae la dirección IP antes del símbolo "/"
                ip_address = line.split()[1].split("/")[0]
                ip_interfaces = (ip_address.replace(".","-"))
                return ip_interfaces
    except subprocess.CalledProcessError:
        print("Error al ejecutar el comando.")
    except IndexError:
        print("No se encontró una dirección IP.")
    return None

#Obtén y muestra la dirección IP
#ip_address = get_ip_address()
# if ip_address:
#     print(f"La dirección IP es: {ip_address}")

# else:
#     print("No se pudo obtener la dirección IP.")

