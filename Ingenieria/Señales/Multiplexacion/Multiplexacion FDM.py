import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la simulación
fs = 1000  # Frecuencia de muestreo (Hz)
t = np.linspace(0, 1, fs)  # Vector de tiempo de 1 segundo

# Frecuencias de las señales individuales (en Hz)
freq1 = 5    # Señal 1
freq2 = 50   # Señal 2
freq3 = 120  # Señal 3

# Crear las señales individuales
signal1 = np.sin(2 * np.pi * freq1 * t)
signal2 = np.sin(2 * np.pi * freq2 * t)
signal3 = np.sin(2 * np.pi * freq3 * t)

# Señal FDM (combinación de las señales individuales)
fdm_signal = signal1 + signal2 + signal3

# Graficar las señales individuales y la señal FDM
plt.figure(figsize=(12, 8))

# Señal 1
plt.subplot(4, 1, 1)
plt.plot(t, signal1, label=f'Señal de {freq1} Hz')
plt.title('Señales Individuales y Señal FDM')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.legend()
plt.grid()

# Señal 2
plt.subplot(4, 1, 2)
plt.plot(t, signal2, label=f'Señal de {freq2} Hz', color='orange')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.legend()
plt.grid()

# Señal 3
plt.subplot(4, 1, 3)
plt.plot(t, signal3, label=f'Señal de {freq3} Hz', color='green')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.legend()
plt.grid()

# Señal combinada FDM
plt.subplot(4, 1, 4)
plt.plot(t, fdm_signal, label='Señal FDM (combinada)', color='purple')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
