import matplotlib.pyplot as plt
import numpy as np
import time

if __name__ == "__main__":
    x = np.linspace(0, 10, 100)  
    y = np.linspace(0, 100, 100)

    plt.ion()  # Modo interactivo
    figure, ax = plt.subplots()
    ax.set_xlim(0, 3)
    ax.set_ylim(0, 100)

    ancho = 0.4  # Ancho de las barras
    barra1 = ax.bar(1, 0, width=ancho, color='red')   # Barra inicial
    barra2 = ax.bar(2, 100, width=ancho, color='blue')  # Segunda barra

    while True:
        for i in range(len(y)):
            # Actualizar la altura de las barras
            barra1[0].set_height(y[i])  
            barra2[0].set_height(y[-i-1])  

            figure.canvas.draw()
            figure.canvas.flush_events()
            time.sleep(0.000001)

        # Cambiar la dirección de movimiento
        y = y[::-1]