import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la señal
A = 1  # Amplitud
f_c = 1  # Frecuencia de la portadora (Hz)
T = 1  # Duración de cada bit (segundos)
fs = 100  # Frecuencia de muestreo (Hz)

# Secuencia de bits
bits = np.array([1, 1, 0, 1])

# Tiempo total
t_bpsk = np.arange(0, len(bits)*T, 1/fs)

# Generar la señal BPSK usando la ecuación de fase
bpsk_signal = np.zeros(len(t_bpsk))
for i in range(len(bits)):
    if bits[i] == 1:
        # Bit 1: Fase 0 (sin desfase)
        bpsk_signal[i*fs:(i+1)*fs] = A * np.cos(2 * np.pi * f_c * t_bpsk[i*fs:(i+1)*fs])
    else:
        # Bit 0: Fase 180 grados (desfase de pi)
        bpsk_signal[i*fs:(i+1)*fs] = A * np.cos(2 * np.pi * f_c * t_bpsk[i*fs:(i+1)*fs] + np.pi)

# Graficar la señal
plt.figure(figsize=(12, 6))

# Gráfico de la secuencia de bits
plt.subplot(2, 1, 1)
plt.step(np.arange(0, len(bits)), bits, where='mid')
plt.title('Secuencia de bits: 1101')
plt.xlabel('Tiempo (símbolos)')
plt.ylabel('Bit')

# Gráfico de la señal BPSK
plt.subplot(2, 1, 2)
plt.plot(t_bpsk, bpsk_signal)
plt.title('Señal modulada BPSK (1101)')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')

plt.tight_layout()
plt.show()
