import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la señal
one_frequency  = 5          # Frecuencia de la señal bit 1 (Hz)
zero_frequency = 1          # Frecuencia de la señal bit 0 (Hz)
sample_rate = 1000          # Frecuencia de muestreo
bit_duration = np.pi        # Duración de cada bit en segundos
w = 1      

# Mensaje binario a modular 
message = [1, 0, 1, 1, 1, 0, 0, 1, 0, 1]

# Generación del tiempo total de la señal
t_total = np.linspace(0, bit_duration * len(message), len(message) * sample_rate, endpoint=False)
t_total_binary = np.linspace(0, bit_duration * len(message), int(sample_rate * bit_duration * len(message)), endpoint=False)

# Inicialización de la señal ASK y la señal binaria
signal_FSK = np.zeros(len(t_total))
binary_signal = np.zeros_like(t_total_binary)

# Modulación FSK y la señal binaria bit a bit
for i, bit in enumerate(message):
    # Rango de tiempo para el bit actual
    t_bit_start = i * bit_duration
    t_bit_end = (i + 1) * bit_duration
    t_bit = np.linspace(t_bit_start, t_bit_end, int(sample_rate * bit_duration), endpoint=False)
    
    # Modulación FSK: ajustamos la amplitud según el valor del bit
    if bit == 0:
        signal_FSK[i * sample_rate:(i + 1) * sample_rate] = np.sin(2 * w * zero_frequency * t_total[i * sample_rate:(i + 1) * sample_rate])
        binary_signal[i * int(sample_rate * bit_duration):(i + 1) * int(sample_rate * bit_duration)] = 0  # Representación de bit bajo
    else:
        signal_FSK[i * sample_rate:(i + 1) * sample_rate] = np.sin(2 * w * one_frequency * t_total[i * sample_rate:(i + 1) * sample_rate])
        binary_signal[i * int(sample_rate * bit_duration):(i + 1) * int(sample_rate * bit_duration)] = 1  # Representación de bit alto
    
# Visualización de la señal FSK y la señal binaria
plt.figure(figsize=(12, 6))

# Graficar la señal binaria
plt.subplot(2, 1, 1)
plt.plot(t_total_binary, binary_signal, drawstyle='steps-pre', color='r')
plt.title("Señal Binaria")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.ylim(-0.2, 1.2)
plt.grid(True)

# Añadir etiquetas de bits (0 o 1) en la señal binaria
for i, bit in enumerate(message):
    plt.text(i * bit_duration + bit_duration / 2, 0.5, str(bit), ha='center', va='center', color='red', fontsize=12, fontweight='bold')

# Visualización de la señal
plt.subplot(2, 1, 2)
plt.plot(t_total, signal_FSK)
plt.title("Señal modulada FSK")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.grid(True)
plt.tight_layout()
plt.show()