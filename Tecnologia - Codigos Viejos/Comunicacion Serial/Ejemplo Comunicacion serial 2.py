
from serial import*
import matplotlib.pyplot as plt
import matplotlib.animation as animation
#from random import ramdom


serialPort='COM3'
baudRate=9600
mbed=Serial(serialPort,baudRate)

figure1 = plt.figure()
axes1 = figure1.add_subplot(1,1,1)
ys=[]

    
def animar(i):
    cadena = mbed.readline().decode('utf-8')
    ys.append(cadena[0:2])
     
    axes1.clear()
    axes1.plot(ys)

anim = animation.FuncAnimation(figure1, animar, interval=1000)
plt.show()    
