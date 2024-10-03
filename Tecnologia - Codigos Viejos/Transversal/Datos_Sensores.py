from serial import*
from time import*
import numpy as np
import pandas as pd

serial=Serial('COM4',9600)
i = 0
h = 0
z = 0
nMuestras = 5
cadena = list
vel = [nMuestras]
rpm = [nMuestras]
uvl = [nMuestras]
uvi = [nMuestras]

while(True):

    cadena=serial.readline().decode('utf-8')
    cadena=np.array(cadena.split('b'))

    '''
    s1=cadena[0]
    s2=cadena[1]
    s3=cadena[2]
    s4=cadena[3]

    
    s1=float(cadena[0])
    s2=float(cadena[1])
    s3=float(cadena[2])
    s4=float(cadena[3])'''

    #print(s1,s2,s3,s4) 
    print(cadena)
    '''
    vel.insert(0,s1) 
    rpm.insert(0,s2) 
    uvl.insert(0,s3) 
    uvi.insert(0,s4) 
    datos = {'RPM':vel,
            'Velocidad':rpm,
            'Uv Level':uvl,
            'Uv Intensity':uvi}

    if(h==nMuestras):
        while(h>z):

            df=pd.DataFrame(datos, columns=['RPM','Velocidad'])
            df.to_csv('D:/Datos Fredy/Trabajos U/Programacion/Python/10_Datos_Anenomemtro.csv', sep=';')  
    '''
    h=h+1
 
    
