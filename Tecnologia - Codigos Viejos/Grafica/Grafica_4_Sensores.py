from serial import*
from matplotlib import*
import matplotlib.pyplot as plt 
import matplotlib.animation as animation 
from matplotlib.lines import Line2D
from time import*
import numpy as np
import pandas as pd
from gettext import npgettext

#py -m pip install pyserial

#serial=Serial('/dev/ttyACM0',9600)
serial=Serial('COM4',9600)
cadena=list

AnchoGrafica = 20

#vectores para guardar datos del sensor
v1=[]
v2=[]
v3=[]
v4=[]

#Graficas
fig=plt.figure()
ax1=fig.add_subplot(221)
ax2=fig.add_subplot(222)
ax3=fig.add_subplot(223) 
ax4=fig.add_subplot(224)
x=np.linspace(0,1,1)

x=[]

y1=[]
y2=[]
y3=[]
y4=[]

#Codigo de lectura
while True:
    def animacion(i):
        cadena=serial.readline().decode('utf-8')
        
        cadena=np.array(cadena.split(','))
        
        presion=cadena[0]
        temperatura=cadena[1]
        potenciometro=cadena[2]
        lm35=cadena[3]

        s1=np.array(presion.split(':'))[-1]
        s2=np.array(temperatura.split(':'))[-1]
        s3=np.array(potenciometro.split(':'))[-1]
        s4=np.array(lm35.split(':'))[-1]

        s1=float(s1)
        s2=float(s2)
        s3=float(s3)
        s4=float(s4)

        v1.insert(0,s1)
        v2.insert(0,s2)
        v3.insert(0,s3)
        v4.insert(0,s4)

        
        if (len(v1)>AnchoGrafica):
            v1.pop()
            v2.pop()
            v3.pop()
            v4.pop()
            
            data={'Presion':[v1[0],v1[1],v1[2],v1[3],v1[4],v1[5],v1[6],v1[7],v1[8],v1[9]],'Temperatura':[v2[0],v2[1],v2[2],v2[3],v2[4],v2[5],v2[6],v2[7],v2[8],v2[9]],
            'Potenciometro':[v3[0],v3[1],v3[2],v3[3],v3[4],v3[5],v3[6],v3[7],v3[8],v3[9]],'Lm35':[v4[0],v4[1],v4[2],v4[3],v4[4],v4[5],v4[6],v4[7],v4[8],v4[9]]}
            df=pd.DataFrame(data, columns=['Presion','Temperatura','Potenciometro','Lm35'])
            df.to_csv('D:/Datos Fredy/Trabajos U/Programacion/Python/Ultimos_10_Datos.csv', sep=';') 

        #print(s1,s2,s3,s4)
        print(v1,'\n',v2,'\n',v3,'\n',v4,'\n')

        

        x.insert(0,i)

        y1.insert(0,s1)
        y2.insert(0,s2)
        y3.insert(0,s3)
        y4.insert(0,s4)

        if (len(y1)>AnchoGrafica):
            y1.pop()
            y2.pop()
            y3.pop()
            y4.pop()

        ax1.clear()
        ax1.plot(x[0:AnchoGrafica],y1[0:AnchoGrafica],'Red')

        ax2.clear()
        ax2.plot(x[0:AnchoGrafica],y2[0:AnchoGrafica])

        ax3.clear()
        ax3.plot(x[0:AnchoGrafica],y3[0:AnchoGrafica],'Green')

        ax4.clear()
        ax4.plot(x[0:AnchoGrafica],y4[0:AnchoGrafica],'Orange')

        ax1.title.set_text('Sensor de Presion')
        ax1.set_xlabel("Tiempo")
        ax1.set_ylabel("Presion")
        
    anim=animation.FuncAnimation(fig,animacion, interval=1000)    
    plt.show()