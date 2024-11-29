from machine import Pin, PWM, ADC
import math
import time

# Configuración del pin PWM
pwm_pin = 25  # Pin donde se genera la señal PWM (ajustar según hardware)
pwm_frequency = 1000  # Frecuencia base de la señal PWM en Hz
pwm = PWM(Pin(pwm_pin))
pwm.freq(pwm_frequency)

# Parámetros de la señal sinusoidal
sin_frequency = 100  # Frecuencia de la señal sinusoidal en Hz
resolution = 1000  # Número de pasos para aproximar la onda (mayor = más suave)
max_duty = 1023  # Ciclo de trabajo máximo permitido para PWM
amplitude = max_duty // 2 # Amplitud máxima de la onda sinusoidal
offset = max_duty // 2  # Offset para centrar la onda en el rango permitido

# Generar una tabla de valores sinusoidales
sin_table = [int(offset + (amplitude-1) * math.sin(2 * math.pi * i / resolution)) for i in range(resolution)]
# Datos binarios que se transmitirán
data = [1, 0, 1, 1, 0, 0, 1]  # Ejemplo de datos binarios
bit_duration = 1  # Duración de cada bit en segundos

try:
    while True:
        for bit in data:
            señales = 0
            if bit == 1:
                print("Generando 1...")
                for value in sin_table:
                    while(señales<10):
                        pwm.duty(value)  # Ajusta el ciclo de trabajo según la tabla
                        señales += 1
                        #time.sleep(1 / (sin_frequency * resolution))  # Tiempo entre pasos
            else:
                print("Generando 0...")
                pwm.duty(0)  # Desactiva la portadora
            time.sleep(bit_duration)  # Mantiene el bit durante el tiempo especificado

except KeyboardInterrupt:
    pwm.deinit()  # Apaga el PWM al terminar
    print("Modulación ASK finalizada.")
