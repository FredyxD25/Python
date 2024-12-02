from machine import Pin, PWM, ADC
import time

# Configuración del pin PWM
carrier_frequency = 1000  # Frecuencia de la portadora en Hz
duty_cycle_on = 512       # Ciclo de trabajo para señal alta (máximo es 1023)
duty_cycle_off = 0        # Ciclo de trabajo para señal baja
pin_pwm = 25              # Pin donde se genera la señal PWM (ajustar según hardware)

# Configuración del PWM en el pin
pwm = PWM(Pin(pin_pwm))
pwm.freq(carrier_frequency)
pwm.duty(duty_cycle_off)  # Inicialmente apagado

# Configuración del ADC en el pin
adc_pin = 36  # Pin para la entrada analógica (ajustar según el hardware)
adc = ADC(Pin(adc_pin))  # Configura el pin como entrada analógica
adc.atten(ADC.ATTN_11DB)  # Rango de lectura hasta ~3.6V
adc.width(ADC.WIDTH_10BIT)  # Resolución de 10 bits (valores de 0 a 1023)

# Parámetros de muestreo
sampling_frequency = 1000  # Frecuencia de muestreo en Hz
sampling_interval = 1 / sampling_frequency  # Intervalo de muestreo en segundos
num_samples = 100  # Número de muestras a capturar

# Almacenamiento de las muestras
samples = []
# Datos binarios que se transmitirán
data = [1, 0, 1, 1, 1, 0, 0, 1]  # Ejemplo de datos binarios
bit_duration = 0.5  # Duración de cada bit en segundos
muestras_maximas = 24
try:
    while True:
        for bit in data:
            if bit == 1:
                print("Bit 1")
                pwm.duty(duty_cycle_on)  # Activa la portadora
            else:
                print("Bit 0")
                pwm.duty(duty_cycle_off)  # Desactiva la portadora
            time.sleep(bit_duration)  # Mantiene el bit durante el tiempo especificado
        print("Mensaje [1, 0, 1, 1, 1, 0, 0, 1]")
        time.sleep(1)  # Pausa entre transmisiones
except KeyboardInterrupt:
    pwm.deinit()  # Apaga el PWM al terminar
    print("Modulación ASK finalizada.")