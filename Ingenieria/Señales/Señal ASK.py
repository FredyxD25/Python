import numpy as np
import matplotlib.pyplot as plt

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

# Visualización de la señal ASK y la señal binaria
plt.figure(figsize=(12, 6))

# Graficar la señal binaria
plt.subplot(2, 1, 1)
plt.plot(t_total, binary_signal, drawstyle='steps-pre', color='r')
plt.title("Señal Binaria")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.ylim(-0.2, 1.2)
plt.grid(True)

# Añadir etiquetas de bits (0 o 1) en la señal binaria
for i, bit in enumerate(message):
    plt.text(i * bit_duration + bit_duration / 2, 0.5, str(bit), ha='center', va='center', color='red', fontsize=12, fontweight='bold')

# Graficar la señal ASK
plt.subplot(2, 1, 2)
plt.plot(t_total, ask_signal)
plt.title("Modulación ASK (Amplitude Shift Keying)")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.grid(True)
plt.tight_layout()
plt.show()
