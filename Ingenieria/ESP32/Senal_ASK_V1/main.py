from machine import Pin, PWM, ADC
import time

# Configuración del pin del LED (GPIO2)
salida_señal = Pin(25, Pin.OUT)

# Datos binarios que se transmitirán
data = [1, 0, 1, 1, 1, 0, 0, 1]  # Ejemplo de datos binarios
bit_duration = 0.5  # Duración de cada bit en segundos
muestras_maximas = 24
try:
    while True:
        for bit in data:
            if bit == 1:
                print("Bit 1")
                salida_señal.value(1)
            else:
                print("Bit 0")
                salida_señal.value(0)
            time.sleep(bit_duration)  # Mantiene el bit durante el tiempo especificado
        print("Mensaje [1, 0, 1, 1, 1, 0, 0, 1]")
        time.sleep(1)  # Pausa entre transmisiones
except KeyboardInterrupt:
    pwm.deinit()  # Apaga el PWM al terminar
    print("Modulación ASK finalizada.")