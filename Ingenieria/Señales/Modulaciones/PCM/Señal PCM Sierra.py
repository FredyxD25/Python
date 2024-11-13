import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la señal de diente de sierra
frecuencia = 5  # Frecuencia de la señal (Hz)
amplitud = 1    # Amplitud de la señal
duracion = 1    # Duración de la señal (segundos)
frecuencia_muestreo = 1000  # Frecuencia de muestreo (Hz)

# Generar el eje de tiempo
t = np.linspace(0, duracion, duracion * frecuencia_muestreo)

# Generar la señal de diente de sierra
señal_diente_sierra = amplitud * (t * frecuencia % 1)

# Parámetros de la señal PCM
niveles_cuantizacion = 16  # Número de niveles de cuantización
bits_por_nivel = int(np.log2(niveles_cuantizacion))  # Bits necesarios para representar los niveles

# Cuantización de la señal
señal_min = np.min(señal_diente_sierra)  # Mínimo valor de la señal
señal_max = np.max(señal_diente_sierra)  # Máximo valor de la señal
delta = (señal_max - señal_min) / (niveles_cuantizacion - 1)  # Paso de cuantización

# Cuantificar la señal
señal_pcm = np.round((señal_diente_sierra - señal_min) / delta) * delta + señal_min

# Graficar la señal continua de diente de sierra y la señal PCM
plt.figure(figsize=(10, 6))

# Gráfica de la señal continua de diente de sierra
plt.subplot(2, 1, 1)
plt.plot(t, señal_diente_sierra, label='Señal Diente de Sierra Continua', color='blue')
plt.title('Señal de Diente de Sierra Continua')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.grid(True)

# Gráfica de la señal PCM (cuantificada)
plt.subplot(2, 1, 2)
plt.step(t, señal_pcm, where='mid', label='Señal PCM (Cuantificada)', color='red')
plt.title('Señal PCM de Diente de Sierra')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud Cuantificada')
plt.grid(True)

plt.tight_layout()
plt.show()