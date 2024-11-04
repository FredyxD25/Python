import numpy as np
import matplotlib.pyplot as plt

# Parámetros
A_c = 100         # Amplitud de la portadora
f_c = 5         # Frecuencia de la portadora (Hz)
A_m = 10        # Amplitud de la señal de mensaje
f_m = 10         # Frecuencia de la señal de mensaje (Hz)
k_p = np.pi/2   # Constante de modulación de fase (rad)

# Tiempo
t = np.linspace(0, 1, 1000)

# Señal de mensaje
m_t = A_m * np.cos(2 * np.pi * f_m * t)

# Señal portadora
s_t = A_c * np.cos(2 * np.pi * f_c * t + k_p * m_t)

# Graficar
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.title("Señal de Mensaje")
plt.plot(t, m_t, color='blue')
plt.xlim(0,0.5)
plt.grid()

plt.subplot(2, 1, 2)
plt.title("Señal PM")
plt.plot(t, s_t, color='green')
plt.xlim(0,0.5)
plt.grid()

plt.tight_layout()
plt.show()
