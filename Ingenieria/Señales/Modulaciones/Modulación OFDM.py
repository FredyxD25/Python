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

# Gráfica de la constelación
plt.figure(figsize=(8, 8))
plt.scatter(received_symbols.real.flatten(), received_symbols.imag.flatten(), s=20, alpha=0.5, color="blue")

# Dibujar círculos para unir puntos
circle_radius = np.abs(received_symbols[0, :])  # Radio basado en el primer símbolo
angles = np.linspace(0, 2 * np.pi, 100)
for radius in np.unique(circle_radius):
    x_circle = radius * np.cos(angles)
    y_circle = radius * np.sin(angles)
    plt.plot(x_circle, y_circle, linestyle='--', color='red', alpha=0.5)


plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.title("Diagrama de Constelación (QPSK)")
plt.xlabel("Parte Real")
plt.ylabel("Parte Imaginaria")
plt.axis('equal')
plt.show()
