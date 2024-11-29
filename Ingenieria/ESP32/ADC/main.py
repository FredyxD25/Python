from machine import ADC, Pin
import time

# Configuración del ADC
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

print("Iniciando el muestreo de la señal...")

try:
    for _ in range(num_samples):
        sample = adc.read()  # Leer el valor analógico
        samples.append(sample)  # Guardar la muestra
        time.sleep(sampling_interval)  # Esperar el tiempo de muestreo

    print("Muestreo completado.")
    print("Datos capturados:", samples)

except KeyboardInterrupt:
    print("Muestreo interrumpido por el usuario.")

# Procesamiento adicional
# Si deseas realizar un análisis, exportar los datos o graficarlos,
# puedes trabajar con la lista `samples`.