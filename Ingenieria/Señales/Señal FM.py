import numpy as np
import matplotlib.pyplot as plt

# Parámetros
fs = 10000  # Frecuencia de muestreo
f_c = 1000  # Frecuencia de la portadora (Hz)
f_m = 100   # Frecuencia de la señal moduladora (Hz)
beta = 5    # Índice de modulación (devación de frecuencia)

# Tiempo
t = np.arange(0, 1, 1/fs)

# Señal moduladora (una onda seno)
moduladora = np.sin(2 * np.pi * f_m * t)

# Señal FM
fm_signal = np.cos(2 * np.pi * f_c * t + beta * moduladora)

# Graficar
plt.figure(figsize=(12, 6))

# Señal moduladora
plt.subplot(2, 1, 1)
plt.plot(t, moduladora, color='blue')
plt.title('Señal Moduladora')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.xlim(0,0.05)

# Señal FM
plt.subplot(2, 1, 2)
plt.plot(t, fm_signal, color='green')
plt.title('Señal de Frecuencia Modulada (FM)')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.xlim(0,0.05)

plt.tight_layout()
plt.show()
