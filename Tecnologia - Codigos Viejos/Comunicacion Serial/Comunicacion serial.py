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
serial=Serial('COM3',9600)
cadena=list


#vectores para guardar datos del sensor
v1=[]
v2=[]
v3=[]

y1=[]
y2=[]
y3=[]

#Codigo de lectura
while True: 
        cadena=serial.readline().decode('utf-8')
        cadena=np.array(cadena.split(','))
        
        s1=cadena[0]
        s2=cadena[1]
        s3=cadena[2]

        s1=float(s1)
        s2=float(s2)
        s3=float(s3)

        v1.insert(0,s1)
        v2.insert(0,s2)
        v3.insert(0,s3)

        #print(s1,s2,s3,s4)
        print(v1,'\n',v2,'\n',v3,'\n')
        
