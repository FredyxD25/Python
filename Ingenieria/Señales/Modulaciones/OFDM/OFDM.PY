import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la señal OFDM
N_subcarriers = 64  # Número de subportadoras
N_symbols = 100     # Número de símbolos OFDM
cp_len = 16         # Longitud del prefijo cíclico (en muestras)
#Fs = 15.36e3        # Frecuencia de muestreo (Hz)
Fs = 10
# Generar datos aleatorios (modulación QPSK)
data = np.random.choice([1+1j, 1-1j, -1+1j, -1-1j], (N_symbols, N_subcarriers))

# Realizar la IFFT (modulación OFDM)
ifft_data = np.fft.ifft(data, n=N_subcarriers, axis=1)

# Añadir prefijo cíclico
cp = ifft_data[:, -cp_len:]  # Copiar las últimas muestras
ofdm_signal = np.hstack([cp, ifft_data])  # Concatenar prefijo y símbolo OFDM

# Aplanar para obtener la señal completa
ofdm_signal = ofdm_signal.flatten()

# Eje temporal para visualización
t = np.arange(len(ofdm_signal)) / Fs

# Visualización de la señal OFDM en tiempo
plt.figure(figsize=(12, 6))
plt.plot(t[:500], ofdm_signal[:500].real, label='Parte real')
plt.plot(t[:500], ofdm_signal[:500].imag, label='Parte imaginaria', linestyle='dashed')
plt.title("Señal OFDM (Tiempo)")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.legend()


# Visualización del espectro de la señal OFDM
fft_ofdm = np.fft.fft(ofdm_signal)
freqs = np.fft.fftfreq(len(ofdm_signal), d=1/Fs)

plt.figure(figsize=(12, 6))
plt.plot(freqs[:len(freqs)//2], np.abs(fft_ofdm[:len(freqs)//2]))
plt.title("Espectro de la señal OFDM")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Amplitud")
plt.grid()
plt.show()
