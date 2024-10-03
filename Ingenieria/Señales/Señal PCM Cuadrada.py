import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Parámetros de la señal
frecuencia = 5       # Frecuencia de la señal en Hz
duracion = 1         # Duración de la señal en segundos
fs = 100             # Frecuencia de muestreo (samples/segundo)
bits_por_muestra = 3 # Resolución en bits

# Generar la señal de onda cuadrada
t = np.linspace(0, duracion, int(fs * duracion), endpoint=False)
señal_original = signal.square(2 * np.pi * frecuencia * t)  # Señal cuadrada

# Normalización para que los valores estén entre 0 y 1 (lo que facilita la cuantización)
señal_normalizada = (señal_original - señal_original.min()) / (señal_original.max() - señal_original.min())

# Cuantización de la señal
niveles = 2 ** bits_por_muestra  # Número de niveles de cuantización
señal_cuantizada = np.round(señal_normalizada * (niveles - 1))

# Convertir los valores cuantizados a formato binario (PCM)
def decimal_a_binario(numero, bits):
    return format(int(numero), f'0{bits}b')

señal_pcm = [decimal_a_binario(valor, bits_por_muestra) for valor in señal_cuantizada]

# Graficar la señal original y cuantizada
plt.figure(figsize=(10, 6))

plt.subplot(3, 1, 1)
plt.plot(t, señal_original, label='Señal Original (Onda Cuadrada)')
plt.title('Señal Original (Onda Cuadrada)')
plt.grid(True)
plt.legend()

plt.subplot(3, 1, 2)
plt.step(t, señal_cuantizada, label='Señal Cuantizada', where='mid')
plt.title(f'Señal Cuantizada con {bits_por_muestra} bits')
plt.grid(True)
plt.legend()

# Mostrar los bits de la señal PCM para un segmento de la señal
plt.subplot(3, 1, 3)
plt.title('Señal PCM (bits)')
for i in range(len(señal_pcm[:10])):
    plt.text(i/fs, 0.5, señal_pcm[i], fontsize=10, ha='center')
plt.xlim(0, 10/fs)
plt.ylim(0, 1)
plt.grid(True)

plt.tight_layout()
plt.show()