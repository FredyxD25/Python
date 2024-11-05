import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la señal
carrier_frequency = 1     # Frecuencia de la portadora
sample_frequency = 1000  # Frecuencia de muestreo
bit_duration = np.pi   # Duración de cada bit en segundos
w = 1      

# Mensaje binario a modular 
message = [1, 0, 1, 1, 1, 0, 0, 1, 0, 1]

# Generación del tiempo total de la señal
t_total = np.linspace(0, bit_duration * len(message), len(message) * sample_frequency, endpoint=False)

# Inicialización de la señal ASK y la señal binaria
signal_PSK = np.zeros(len(t_total))
binary_signal = np.zeros_like(t_total)

# Modulación BPSK
for i, bit in enumerate(message):
    if bit == 0:
        signal_PSK[i * sample_frequency:(i + 1) * sample_frequency] = np.sin(2 * w * carrier_frequency * t_total[i * sample_frequency:(i + 1) * sample_frequency] + np.pi)
    else:
        signal_PSK[i * sample_frequency:(i + 1) * sample_frequency] = np.sin(2 * w * carrier_frequency * t_total[i * sample_frequency:(i + 1) * sample_frequency])

# Visualización de la señal PSK y la señal binaria
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

# Visualización de la señal
plt.subplot(2, 1, 2)
plt.plot(t_total, signal_PSK)
plt.title("Señal modulada BPSK")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.grid(True)
plt.tight_layout()
plt.show()