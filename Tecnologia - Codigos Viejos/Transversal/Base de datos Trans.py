
from serial import*

serialPort='COM3'
baudRate=9600
mbed=Serial(serialPort,baudRate)

i=0
vector=[]

while True:
    while True:
        vector.insert(i,mbed.readline().decode('utf-8'))
        print(vector)
        if(vector[i][1]=='\r'):
            print(vector[i][0])#Tiempo Insertado un numero
        else:
            print(vector[i][0]+vector[i][1])#Tiempo Insertado dos numeros 
        print(i+1)#Numero de ciclos
        
        i+=1
        if(i>=10):#10
            i=0
            vector.clear()
            break