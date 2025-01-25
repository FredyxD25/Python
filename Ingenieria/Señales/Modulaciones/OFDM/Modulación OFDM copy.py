import numpy as np
import matplotlib.pyplot as plt

# Parámetros OFDM
num_subcarriers = 64  # Número de subportadoras
num_symbols = 10      # Número de símbolos OFDM
data_rate = 4         # Bits por símbolo (modulación QAM)
sampling_rate = 1000  # Tasa de muestreo (Hz)
cp_len = 16           # Longitud del prefijo cíclico

# Generar datos aleatorios
num_bits = num_subcarriers * num_symbols * data_rate
data_bits = np.random.randint(0, 2, num_bits)

# Mapeo de datos a símbolos QAM
qam_order = 2 ** data_rate
symbols = np.array([complex(i // np.sqrt(qam_order), i % np.sqrt(qam_order))
                     for i in range(qam_order)])
qam_symbols = symbols[np.packbits(data_bits).astype(int) % qam_order]

# Generar señales OFDM
ofdm_signal = np.zeros(num_subcarriers * num_symbols, dtype=complex)
for i in range(num_symbols):
    # Asignar los símbolos a las subportadoras
    freq_data = qam_symbols[i * num_subcarriers:(i + 1) * num_subcarriers]
    time_data = np.fft.ifft(freq_data)  # Transformada inversa de Fourier
    # Agregar prefijo cíclico
    time_data_cp = np.concatenate((time_data[-cp_len:], time_data))
    ofdm_signal[i * len(time_data_cp):(i + 1) * len(time_data_cp)] = time_data_cp

# Calcular amplitudes y ángulos de las señales
amplitudes = np.abs(ofdm_signal)
angles = np.angle(ofdm_signal)

# Visualizar resultados
plt.figure(figsize=(12, 8))

# Señal OFDM en el tiempo
plt.subplot(3, 1, 1)
plt.plot(np.real(ofdm_signal), label="Parte Real")
plt.plot(np.imag(ofdm_signal), label="Parte Imaginaria")
plt.title("Señal OFDM en el dominio del tiempo")
plt.legend()

# Amplitudes
plt.subplot(3, 1, 2)
plt.plot(amplitudes, label="Amplitud")
plt.title("Amplitudes de la señal OFDM")
plt.legend()

# Ángulos
plt.subplot(3, 1, 3)
plt.plot(angles, label="Ángulo")
plt.title("Ángulos de la señal OFDM")
plt.legend()

plt.tight_layout()
plt.show()
