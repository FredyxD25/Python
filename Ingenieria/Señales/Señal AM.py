import numpy as np
import matplotlib.pyplot as plt

# Parámetros
fs = 100  # Frecuencia de muestreo
t = np.arange(0, 0.1, fs)  # Tiempo de 0 a 1 segundo

# Frecuencia de la portadora (1000 kHz)
fc = 1000  # Frecuencia de la portadora
carrier = np.cos(2 * np.pi * fc * t)

# Frecuencia de la señal de audio (5 Hz)
fa = 1000  # Frecuencia de la señal de audio
audio_signal = 0.5 * np.sin(2 * np.pi * fa * t)  # Señal de audio normalizada

# Modulación en amplitud
am_signal = (1 + audio_signal) * carrier

# Graficar las señales
plt.figure(figsize=(12, 8))

# Onda portadora
plt.subplot(3, 1, 1)
plt.plot(t, carrier)
plt.title('Onda Portadora (10000 Hz)')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')

# Señal de audio
plt.subplot(3, 1, 2)
plt.plot(t, audio_signal)
plt.title('Señal de Audio (1000 Hz)')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')

# Señal AM
plt.subplot(3, 1, 3)
plt.plot(t, am_signal)
plt.title('Señal Modulada en Amplitud (AM)')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')

plt.tight_layout()
plt.show()
