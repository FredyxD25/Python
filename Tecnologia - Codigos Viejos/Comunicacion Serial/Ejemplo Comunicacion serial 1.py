
from serial import*
#py -m pip install pyserial
serialPort='COM3'
baudRate=9600
ser=Serial(serialPort,baudRate)

while 1:
    cadena=ser.readline().decode('utf-8')
    temp=cadena[0:2] 
    print(temp)

    
  