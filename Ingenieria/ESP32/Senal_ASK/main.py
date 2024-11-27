import machine
import time

# Parámetros de la señal ASK
carrier_frequency = 10      # Frecuencia de la señal portadora (Hz)
amplitude_high = 1          # Amplitud para el bit 1
amplitude_low = 0           # Amplitud para el bit 0 (silencio en el bit 0)

# Parámetros Universales
sample_rate = 1000          # Frecuencia de muestreo
bit_duration = np.pi            # Duración de cada bit en segundos
w = 1

# Mensaje binario a modular 
message = [1, 0, 1, 1, 1, 0, 0, 1, 0, 1]

# Generación del tiempo total de la señal
t_total = np.linspace(0, bit_duration * len(message), int(sample_rate * bit_duration * len(message)), endpoint=False)

# Inicialización de la señal ASK y la señal binaria
ask_signal = np.zeros_like(t_total)
binary_signal = np.zeros_like(t_total)

# Generación de la señal ASK y la señal binaria bit a bit
for i, bit in enumerate(message):
    # Rango de tiempo para el bit actual
    t_bit_start = i * bit_duration
    t_bit_end = (i + 1) * bit_duration
    t_bit = np.linspace(t_bit_start, t_bit_end, int(sample_rate * bit_duration), endpoint=False)
    
    # Modulación ASK: ajustamos la amplitud según el valor del bit
    if bit == 1:
        ask_signal[i * int(sample_rate * bit_duration):(i + 1) * int(sample_rate * bit_duration)] = amplitude_high * np.sin(1 * w * carrier_frequency * t_bit)
        binary_signal[i * int(sample_rate * bit_duration):(i + 1) * int(sample_rate * bit_duration)] = 1  # Representación de bit alto
    else:
        ask_signal[i * int(sample_rate * bit_duration):(i + 1) * int(sample_rate * bit_duration)] = amplitude_low
        binary_signal[i * int(sample_rate * bit_duration):(i + 1) * int(sample_rate * bit_duration)] = 0  # Representación de bit bajo
while(True):
    time.sleep_ms(100)
    print("Adios")
