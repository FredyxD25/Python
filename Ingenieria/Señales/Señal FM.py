import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la señal
fs = 10000  # Frecuencia de muestreo
t = np.arange(0, 1, 1/fs)  # Tiempo de 0 a 1 segundo

# Frecuencias
fc = 1000  # Frecuencia de la portadora (Hz)
fm = 100   # Frecuencia de la señal mensaje (Hz)
kf = 10   # Índice de modulación (sensibilidad de frecuencia)

# Señal mensaje
message = np.cos(2 * np.pi * fm * t)  # Señal mensaje

# Señal FM
fm_signal = np.cos(2 * np.pi * fc * t + kf * message)  # Modulación de frecuencia

# Graficar las señales
plt.figure(figsize=(12, 8))

# Señal Mensaje
plt.subplot(2, 1, 1)
plt.plot(t, message, color='blue')
plt.title('Señal Mensaje')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.xlim(0,0.05)
plt.grid()

# Señal FM
plt.subplot(2, 1, 2)
plt.plot(t, fm_signal, color='green')
plt.title('Señal FM (Modulada)')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.xlim(0,0.05)
plt.grid()

plt.tight_layout()
plt.show()