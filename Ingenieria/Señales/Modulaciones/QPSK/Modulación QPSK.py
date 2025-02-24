import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la simulación
num_subcarriers = 64  # Número de subportadoras
num_symbols = 1000    # Número de símbolos OFDM
mod_order = 4         # Orden de modulación (QPSK, mod_order=4)

# Generación de datos aleatorios
np.random.seed(42)  # Para reproducibilidad
data = np.random.randint(0, mod_order, (num_subcarriers, num_symbols))

# Función para asignar símbolos según la modulación (QPSK)
def qpsk_modulation(bits):
    mapping = {
        0: 1 + 1j,
        1: -1 + 1j,
        2: -1 - 1j,
        3: 1 - 1j
    }
    return np.array([mapping[bit] for bit in bits.flatten()]).reshape(bits.shape)

# Modulación QPSK
symbols = qpsk_modulation(data)

# Transformada Inversa de Fourier (IFFT) para obtener la señal OFDM
time_signal = np.fft.ifft(symbols, axis=0)

# Canal (sin ruido para este ejemplo)
received_signal = time_signal

# Transformada de Fourier (FFT) en el receptor
received_symbols = np.fft.fft(received_signal, axis=0)

# Normalización de los datos recibidos
received_symbols /= np.sqrt(num_subcarriers)

# Gráfica de los fasores
plt.figure(figsize=(8, 8))

# Coordenadas de los fasores (QPSK)
fasores = [1 + 1j, -1 + 1j, -1 - 1j, 1 - 1j]

# Dibujar fasores hasta los puntos
for fasor in fasores:
    plt.quiver(0, 0, fasor.real, fasor.imag, angles='xy', scale_units='xy', scale=1, color='green', linewidth=0.5)
    plt.scatter(fasor.real, fasor.imag, color='blue', s=50)  # Marcar los puntos de los fasores

# Dibujar círculo unitario
circle = plt.Circle((0, 0), np.sqrt(2)*np.cos(np.pi), color='red', fill=False, linestyle='--', linewidth=1)
plt.gca().add_artist(circle)

plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.title("Fasores (QPSK)")
plt.xlabel("Parte Real")
plt.ylabel("Parte Imaginaria")
plt.axis('equal')
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)
plt.show()
