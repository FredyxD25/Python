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
plt.figure(figsize=(20, 10))

# Coordenadas de los fasores (QPSK)
fasores = [1 + 1j, -1 + 1j, -1 - 1j, 1 - 1j]


# Parámetros de la señal
fs = 100  # Frecuencia de muestreo
t1 = np.arange(0, 4, 1/fs)  # Tiempo de 0 a 1 segundo
t2 = np.arange(4, 8, 1/fs)  # Tiempo de 0 a 1 segundo
t3 = np.arange(8, 12, 1/fs)  # Tiempo de 0 a 1 segundo
t4 = np.arange(12, 16, 1/fs)  # Tiempo de 0 a 1 segundo

# Frecuencias
fc = 1000  # Frecuencia de la portadora (Hz)
fm = 100   # Frecuencia de la señal mensaje (Hz)

# Señales
Q1 =  1 * np.sin(2 * np.pi * t1) + 1 * np.cos(2 * np.pi * t2) 
Q2 =  1 * np.sin(2 * np.pi * t2) - 1 * np.cos(2 * np.pi * t2) 
Q3 = -1 * np.sin(2 * np.pi * t3) + 1 * np.cos(2 * np.pi * t3) 
Q4 = -1 * np.sin(2 * np.pi * t4) - 1 * np.cos(2 * np.pi * t4) 

# Señal Mensaje
plt.subplot(1, 1, 1)
plt.plot(t1, Q1, color='blue')
plt.plot(t2, Q2, color='green')
plt.plot(t3, Q3, color='red')
plt.plot(t4, Q4, color='orange')

plt.title('Señal Mensaje')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.xlim(0,16)
plt.ylim(-3,3)
plt.grid()

plt.tight_layout()
plt.show()