import machine
import time

led_pin = machine.Pin(2, machine.Pin.OUT)
while True:
    led_pin.value(1)
    print("Turning ON again...")
    time.sleep(5)
    led_pin.value(0)
    print("Turning OFF again...")
    time.sleep(5)