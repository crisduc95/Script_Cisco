import re
import getpass
from netmiko import (
    ConnectHandler,
    NetMikoTimeoutException,
    NetMikoAuthenticationException,
    NetmikoBaseException,
)


def conexion(ip, comando):
    salida = []
    int = r'\bGigabitEthernet\d*\b'
    intB = r'\bFastEthernet\d*\b'
    try:
        with ConnectHandler(**ip) as ssh:
            ssh.enable()
            salida = ssh.send_command(comando)
            for i in salida.splitlines():
                if re.search(int, i, re.IGNORECASE):
                    interfaz = i
                    print(interfaz)
                elif re.search(intB, i, re.IGNORECASE):
                    interfaz = i
                    print(interfaz)
                if ' Last input' in i:
                    ultimo = i
                    print(ultimo)
        print("Cerrando la conexion SSH")
        ssh.disconnect()
    except Exception as e:
        print(f"ERROR {e}")


if __name__ == "__main__":
    carac = 'y'
    while carac == 'y':

        user = input("Ingrese usuario: ")
        password = getpass.getpass("Contraseña: ")
        dispo = input("Ingrese IP: ")

        ip =  {"device_type": "cisco_ios", "host": dispo, "username": user, "password": password}
        comando = "show interfaces"
        conexion(ip, comando)
        carac = input("¿Desea hacer mas consultas(y = si n = no): ?")
        carac = carac.lower()
'''
trae la confliguracion de las interfaces, y filtra por el parámetro de last input, el cual muestra la ultima vez en la que la interfaz
fue usada
'''

