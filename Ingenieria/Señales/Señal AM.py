import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la señal
fs = 10000  # Frecuencia de muestreo
t = np.arange(0, 1, 1/fs)  # Tiempo de 0 a 1 segundo

# Frecuencias
fc = 1000  # Frecuencia de la portadora (Hz)
fm = 100   # Frecuencia de la señal mensaje (Hz)

# Señales
carrier = np.cos(2 * np.pi * fc * t)  # Señal portadora
message = 0.5 * np.cos(2 * np.pi * fm * t)  # Señal mensaje (amplitud 0.5)

# Señal AM
am_signal = (1 + message) * carrier  # Modulación AM

# Graficar las señales
plt.figure(figsize=(12, 8))

# Señal Mensaje
plt.subplot(3, 1, 1)
plt.plot(t, message, color='blue')
plt.title('Señal Mensaje')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.xlim(0,0.05)
plt.grid()

# Señal Portadora
plt.subplot(3, 1, 2)
plt.plot(t, carrier, color='red')
plt.title('Señal Portadora')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.xlim(0,0.05)
plt.grid()

# Señal AM
plt.subplot(3, 1, 3)
plt.plot(t, am_signal, color='green')
plt.title('Señal AM (Modulada)')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.xlim(0,0.05)
plt.grid()

plt.tight_layout()
plt.show()