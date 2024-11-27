# boot.py -- run on boot-up
def wifi():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('Carolina', 'JK8519Min')
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ipconfig('addr4'))

wifi()