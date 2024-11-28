# boot.py -- run on boot-up
def conexion_espera():
    contador=0
    while not sta_if.isconnected():
            contador+=1
            if (contador==tiempo_espera):
                print('network config:', sta_if.ipconfig('addr4')) 
                break
            pass

def wifi():
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('Carolina', 'JK8519Min')
        conexion_espera()
        sta_if.active(False)
        sta_if.active(True)
        sta_if.connect('AP-Fe', 'Fe123456')
        conexion_espera()

import network
sta_if = network.WLAN(network.STA_IF)
tiempo_espera=100000
wifi()