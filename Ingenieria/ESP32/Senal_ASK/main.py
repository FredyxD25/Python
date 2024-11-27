import machine
import time
import math

# Parámetros de la señal ASK
carrier_frequency = 10      # Frecuencia de la señal portadora (Hz)
amplitude_high = 1          # Amplitud para el bit 1
amplitude_low = 0           # Amplitud para el bit 0 (silencio en el bit 0)

# Parámetros Universales
sample_rate = 1000          # Frecuencia de muestreo
bit_duration = math.pi           # Duración de cada bit en segundos
w = 1

# Mensaje binario a modular 
message = [1, 0, 1, 1, 1, 0, 0, 1]

def linspace(start, stop, num):
    """
    Genera un array de valores igualmente espaciados entre start y stop.

    Args:
        start (float): Valor inicial.
        stop (float): Valor final.
        num (int): Número de puntos (por defecto, 50).

    Returns:
        list: Lista de valores igualmente espaciados.
    """
    
    if num <= 1:
        return [start]  # Si num es 1 o menos, devuelve el valor inicial.
    step = (stop - start) / (num - 1)
    return [start + step * i for i in range(num)]

def zeros_like(arr):
    """
    Crea un array con la misma forma y tipo que el array de entrada, pero con todos los valores en cero.

    Args:
        arr (list): El arreglo de entrada, que puede ser una lista anidada (como un arreglo multidimensional).

    Returns:
        list: Un nuevo arreglo con los mismos tamaños y forma que `arr`, pero con todos los valores a 0.
    """
    if isinstance(arr, list):
        # Si arr es una lista, lo manejamos de forma recursiva.
        return [zeros_like(item) if isinstance(item, list) else 0 for item in arr]
    return 0  # Para los casos donde arr es una lista de un solo nivel.

# Generación del tiempo total de la señal
t_total = linspace(0, bit_duration * 8, sample_rate * bit_duration * 8)

# Inicialización de la señal ASK y la señal binaria
ask_signal = zeros_like(t_total)
binary_signal = zeros_like(t_total)

# Generación de la señal ASK y la señal binaria bit a bit
for i, bit in enumerate(message):
    # Rango de tiempo para el bit actual
    t_bit_start = i * bit_duration
    t_bit_end = (i + 1) * bit_duration
    t_bit = linspace(t_bit_start, t_bit_end, int(sample_rate * bit_duration))
    
    # Modulación ASK: ajustamos la amplitud según el valor del bit
    if bit == 1:
        ask_signal[i * int(sample_rate * bit_duration):(i + 1) * int(sample_rate * bit_duration)] = amplitude_high * math.sin(1 * w * carrier_frequency * t_bit)
        binary_signal[i * int(sample_rate * bit_duration):(i + 1) * int(sample_rate * bit_duration)] = 1  # Representación de bit alto
    else:
        ask_signal[i * int(sample_rate * bit_duration):(i + 1) * int(sample_rate * bit_duration)] = amplitude_low
        binary_signal[i * int(sample_rate * bit_duration):(i + 1) * int(sample_rate * bit_duration)] = 0  # Representación de bit bajo
        
while(True):
    time.sleep_ms(100)
    #print("Adios")
