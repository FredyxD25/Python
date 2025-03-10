import numpy as np
import matplotlib.pyplot as plt
import random

# Definición de los parámetros de la señal
symbols_binary = [
    "0000", "0001", "0010", "0011",
    "0100", "0101", "0110", "0111",
    "1000", "1001", "1010", "1011",
    "1100", "1101", "1110", "1111"
]

# Generar la constelación 16-QAM (amplitud y fase únicas para cada símbolo)
real_parts = np.array([-3, -1, 1, 3])
imag_parts = np.array([-3, -1, 1, 3])
constellation = np.array([x + 1j * y for x in real_parts for y in imag_parts])

# Parámetros de la gráfica
duracion = np.pi/2
fs = 1000  # Frecuencia de muestreo (Hz)
f = 5      # Frecuencia de la portadora (Hz)
t = np.linspace(0, duracion, int(fs * duracion), endpoint=False)  

# Crear las subgráficas
fig, axs = plt.subplots(4, 4, figsize=(10, 8))
fig.subplots_adjust(hspace=0.5, wspace=0.5)

for i, (symbol, constellation_point) in enumerate(zip(symbols_binary, constellation)):
    row = i // 4
    col = i % 4

    # Amplitud y fase del símbolo
    amplitude = np.abs(constellation_point)
    phase = np.angle(constellation_point)

    # Generar la señal sinusoidal para este símbolo
    signal = amplitude * np.cos(2 * np.pi * f * t + phase)

    # Graficar la señal
    random_color = (random.random(), random.random(), random.random())
    axs[row, col].plot(t, signal, color=random_color)
    axs[row, col].set_title(f"{symbol}", fontsize=10, color=random_color)
    axs[row, col].set_xlim(0, duracion)
    axs[row, col].set_ylim(-5, 5)
    axs[row, col].set_xticks([0, duracion], ['0', '$\pi/2$'])

# Ajustar diseño
plt.suptitle("Señales sinusoidales 16-QAM", fontsize=16)
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()