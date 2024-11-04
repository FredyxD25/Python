import matplotlib.pyplot as plt
import numpy as np

# Función para codificación Manchester
def manchester_encoding(data):
    signal = []
    for bit in data:
        if bit == '1':
            signal.extend([1, 0])  # 1: ↓
        else:
            signal.extend([0, 1])  # 0: ↑
    return signal

# Datos de entrada
data1 = '100100000111110000000011'
data2 = '101111001100000000011'

# Codificación Manchester
encoded1 = manchester_encoding(data1)
encoded2 = manchester_encoding(data2)

# Crear el eje temporal
time1 = np.arange(0, len(encoded1), 1)
time2 = np.arange(0, len(encoded2), 1)

# Crear la gráfica
plt.figure(figsize=(12, 8))

# Gráfica para el primer código
plt.subplot(2, 1, 1)
plt.step(time1, encoded1, where='post', label='Código 1', color='blue')
plt.title('Codificación Manchester del Código 1')
plt.xlabel('Intervalos de Tiempo')
plt.ylabel('Nivel de Señal')
plt.ylim(-0.2, 1.2)
plt.grid(True)
plt.xticks(range(len(data1) + 1))
plt.yticks([0, 1])
plt.axhline(0, color='black', lw=0.5)
plt.axhline(1, color='black', lw=0.5)

# Gráfica para el segundo código
plt.subplot(2, 1, 2)
plt.step(time2, encoded2, where='post', label='Código 2', color='orange')
plt.title('Codificación Manchester del Código 2')
plt.xlabel('Intervalos de Tiempo')
plt.ylabel('Nivel de Señal')
plt.ylim(-0.2, 1.2)
plt.grid(True)
plt.xticks(range(len(data2) + 1))
plt.yticks([0, 1])
plt.axhline(0, color='black', lw=0.5)
plt.axhline(1, color='black', lw=0.5)

plt.tight_layout()
plt.show()
