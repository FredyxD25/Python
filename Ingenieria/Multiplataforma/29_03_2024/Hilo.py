import threading
import time

def tempo_1():
    global bandera
    print("\n Se activo el hilo 1")
    bandera = False

if __name__ == "__main__":
    global bandera
    # Crear un hilo
    hilo_1 = threading.Thread(target=tempo_1, args=())
    # Iniciar el hilo
    hilo_1.start()
    # Esperar a que el hilo termine
    hilo_1.join()
    print("El hilo 1 ha terminado")
    print("Fin del programa")