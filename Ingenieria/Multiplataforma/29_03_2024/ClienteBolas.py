# -- coding: utf-8 --
"""Importar librería socket"""
import socket
import json

"""Crear una variable que almacena al socket"""
Nombre_Socket = socket.socket()

"""Llamar al metodo connect para establecer una 
conexión con el servidor. Teniendo en cuenta que
tiene dos parámetros la dirección IP y el puerto"""
IP_Servidor='127.0.0.1'
Puerto=1234

with open(r"D:\Programacion GIT\Python\Ingenieria\Multiplataforma\29_03_2024\posiciones.json", 'r') as file:

    position_dict = json.load(file)


"""Está estructura intenta establecer una conexión"""
try:
    Bandera=True
    Nombre_Socket.connect((IP_Servidor, Puerto))
except ConnectionRefusedError:
    Bandera=False 
    print('Intente conectarse al servidor nuevamente')
def enviar():
    """En este caso la estructra while mantiene la conexión"""
    while Bandera:
        """Solicitud del mensaje a enviar"""
        x = 0
        if x < len(position_dict):
            texto = list(position_dict.values())[x]
            print(texto)
            """Cambio de formato del paquete a enviar (str-byte)"""
            paquete = str(texto).encode('utf-8')  # Convertimos la lista a string y luego la codificamos
            
            """Intente enviar un paquete si no termine la conexión"""
            try:
                Nombre_Socket.send(paquete)
                if(texto=='cerrar'):
                    break
            except ConnectionResetError:
                break
            """Recibir mensaje del servidor"""
            bytes_a_recibir = 1024
            mensaje_recibido = Nombre_Socket.recv(bytes_a_recibir)
            texto = mensaje_recibido.decode("utf8")
            print(texto)
            x += 1
    print('Termino la aplicación')
    """Cerrar el socket"""
    Nombre_Socket.close()

if __name__ == "__main__":
    enviar()
