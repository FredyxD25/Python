from serial import*

serialPort='COM3'
baudRate=9600
seri=Serial(serialPort,baudRate)
while(True):
    datos = seri.readline().decode('utf-8')
    print(datos)