import matplotlib.pyplot as plt
import numpy as np
import time

if __name__=="__main__":
    x = np.linspace(0 , 2 * np.pi, 200)
    y1 = np.tan(x)
    y2 = np.cos(x)

    plt.ion()
    
    #fig, (ax1, ax2, ax3) = plt.subplots(3,1)
    fig, ax1 = plt.subplots()

    marcas = ['Mazda','Toyota','Mercedez','Fiat']
    cantidad = [40,100,30,55]
    colores = {'tab:red', 'tab:blue', 'tab:green', 'tab:orange'}

    linea1, = ax1.plot(x,y1,'bo')
    ax1.plot(x,y1)
    '''ax2.plot(x,y2)
    ax3.bar(marcas,cantidad, color = colores)
    plt.show()'''

    for i in range(len(x)):
        new_y = np.zeros(len(x))
        new_y[i] = y1[i]
        linea1.set_xdata(x)
        linea1.set_ydata(new_y)
        fig.canvas.draw() #dibujar valores actualizados
        fig.canvas.flush_events() #Vaciar buffer
        time.sleep(0.1)