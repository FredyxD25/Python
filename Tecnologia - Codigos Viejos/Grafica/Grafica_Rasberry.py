
from serial import*
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.lines as line2D
import time
import numpy as np
import pandas as pd

serial=Serial('COM3',9600)
cadena=list
cadena=serial.readline().decode('utf-8')
contador=0

#vectores para guardar datos del sensor
v1=[]
v2=[]
v3=[]
v4=[]

#Codigo de lectura
while(True):
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

    
    if (len(v1)>10):
        v1.pop()
        v2.pop()
        v3.pop()
        v4.pop()
        
        data={'Presion':[v1[0],v1[1],v1[2],v1[3],v1[4],v1[5],v1[6],v1[7],v1[8],v1[9]],'Temperatura':[v2[0],v2[1],v2[2],v2[3],v2[4],v2[5],v2[6],v2[7],v2[8],v2[9]],
        'Potenciometro':[v3[0],v3[1],v3[2],v3[3],v3[4],v3[5],v3[6],v3[7],v3[8],v3[9]],'Lm35':[v4[0],v4[1],v4[2],v4[3],v4[4],v4[5],v4[6],v4[7],v4[8],v4[9]]}
        df=pd.DataFrame(data, columns=['Presion','Temperatura','Potenciometro','Lm35'])
        df.to_csv('ejemplo1.csv', sep=';') 

    #print(s1,s2,s3,s4)
    print(v1,'\n',v2,'\n',v3,'\n',v4,'\n')
    print(contador)

    contador=contador+1
    if (contador>3):
        contador=0

    time.sleep(1)

    
