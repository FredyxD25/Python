from itertools import count
import collections
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from serial import *
import numpy as np

def getSerialData(self,Samples,serialConnection, lines, lineValueText, lineLabel):
    data = ser.readline().decode('utf-8')
    data = data.split(", ")
    x = int(data[0])
    y = int(data[1])
    z = int(data[2])
    R = int(data[3].replace("\n", ""))
    data1.append(x) #Guarda lectura en la última posición / #Save reading in the end position
    lines.set_data(range(Samples),data1) # Dibujar nueva linea / Drawn new line
    data2.append(y) #Guarda lectura en la última posición / #Save reading in the end position
    lines1.set_data(range(Samples),data2) # Dibujar nueva linea / Drawn new line
    data3.append(z) #Guarda lectura en la última posición / #Save reading in the end position
    lines2.set_data(range(Samples),data3) # Dibujar nueva linea / Drawn new line
    data4.append(R) #Guarda lectura en la última posición / #Save reading in the end position
    lines3.set_data(range(Samples),data4) # Dibujar nueva linea / Drawn new line
    lineValueText.set_text(lineLabel+' = ' + str(round(x,2))) # Mostrar valor del sensor / Show sensor value
    lineValueText1.set_text(lineLabel1+' = ' + str(round(y,2))) # Mostrar valor del sensor / Show sensor value
    lineValueText2.set_text(lineLabel2+' = ' + str(round(z,2))) # Mostrar valor del sensor / Show sensor value 
    lineValueText3.set_text(lineLabel3+' = ' + str(round(R,2))) # Mostrar valor del sensor / Show sensor value 

serialPort = "COM3"
baudRate = 9600
ser = Serial(serialPort, baudRate)

Samples = 100  #Muestras / Samples

data1 = collections.deque([0] * Samples, maxlen=Samples) # Vector de muestras/ Sample Vector
data2 = collections.deque([0] * Samples, maxlen=Samples) # Vector de muestras/ Sample Vector
data3 = collections.deque([0] * Samples, maxlen=Samples) # Vector de muestras/ Sample Vector
data4 = collections.deque([0] * Samples, maxlen=Samples) # Vector de muestras/ Sample Vector

sampleTime = 200  #Tiempo de muestreo / Sample Time

# Limites de los ejes / Axis limit
xmin = 0
xmax = Samples
ymin = [-300, -10]
ymax = [300, 10]

# fig = plt.figure(figsize=(13,6))# Crea una nueva figura #Create a new figure.
fig = plt.figure()
ax = fig.add_subplot(1,2,1,xlim=(xmin, xmax), ylim=(ymin[0], ymax[0]))
ax.title.set_text("ADXL345") #Titulo de la figura # Figure title
ax.set_xlabel("Lecturas")
ax.set_ylabel("Aceleración")

ax1 = fig.add_subplot(1,2,2,xlim=(xmin, xmax), ylim=(ymin[1], ymax[1]))
ax1.title.set_text("RFID-RC522") #Titulo de la figura # Figure title
ax1.set_xlabel("Tiempo")
ax1.set_ylabel("Lectura")
 
lineLabel = 'X'
lineLabel1 = 'Y'
lineLabel2 = 'Z'
lineLabel3 = 'R'

lines = ax.plot([], [], label=lineLabel)[0] # Grafica datos iniciales y retorna lineas que representan la gráfica/ Plot initial data and Return a list of Line2D objects representing the plotted data.
lines1 = ax.plot([], [], label=lineLabel1)[0] # Grafica datos iniciales y retorna lineas que representan la gráfica/ Plot initial data and Return a list of Line2D objects representing the plotted data.
lines2 = ax.plot([], [], label=lineLabel2)[0] # Grafica datos iniciales y retorna lineas que representan la gráfica/ Plot initial data and Return a list of Line2D objects representing the plotted data.
lines3 = ax1.plot([], [], label=lineLabel3)[0] # Grafica datos iniciales y retorna lineas que representan la gráfica/ Plot initial data and Return a list of Line2D objects representing the plotted data.

lineValueText = ax.text(0.88, 0.10, '', transform=ax.transAxes) #Agregue texto en la ubicación x , y (0 a 1) / Add text at location x, y (0 to 1)
lineValueText1 = ax.text(0.88, 0.07, '', transform=ax.transAxes) #Agregue texto en la ubicación x , y (0 a 1) / Add text at location x, y (0 to 1)
lineValueText2 = ax.text(0.88, 0.04, '', transform=ax.transAxes) #Agregue texto en la ubicación x , y (0 a 1) / Add text at location x, y (0 to 1)
lineValueText3 = ax1.text(0.88, 0.04, '', transform=ax1.transAxes) #Agregue texto en la ubicación x , y (0 a 1) / Add text at location x, y (0 to 1)

anim = animation.FuncAnimation(fig, getSerialData, fargs=(Samples,ser,lines, lineValueText, lineLabel), interval=sampleTime)
plt.show()
 
ser.close() # cerrar puerto serial/ close serial port