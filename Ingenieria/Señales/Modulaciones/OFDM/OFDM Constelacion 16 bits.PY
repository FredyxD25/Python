import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la señal OFDM
num_subcarriers = 4  # Número de subportadoras
num_symbols = 100    # Número de símbolos OFDM
modulation_order = 16  # 16-QAM

# Generar símbolos 16-QAM para cada subportadora
qam_levels = np.array([-3, -1, 1, 3])  # Niveles para 16-QAM
symbols = (np.random.choice(qam_levels, (num_subcarriers, num_symbols)) + 
           1j * np.random.choice(qam_levels, (num_subcarriers, num_symbols)))

# Transformada Inversa de Fourier (IFFT) para generar la señal OFDM
ofdm_signal = np.fft.ifft(symbols, axis=0)

# Aplicar Transformada de Fourier (FFT) para recuperar la constelación de las subportadoras
recovered_symbols = np.fft.fft(ofdm_signal, axis=0)

# Graficar la constelación
plt.figure(figsize=(8, 8))
for i in range(num_subcarriers):
    plt.scatter(recovered_symbols[i, :].real, recovered_symbols[i, :].imag, label=f'Subportadora {i+1}', alpha=0.7)

plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
plt.title('Constelación OFDM con 4 Subportadoras (16-QAM)')
plt.xlabel('Parte Real')
plt.ylabel('Parte Imaginaria')
plt.legend()
plt.grid(alpha=0.3)
plt.show()
