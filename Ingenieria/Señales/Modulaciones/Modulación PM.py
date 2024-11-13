import numpy as np
import matplotlib.pyplot as plt

# Parámetros
A_c = 10        # Amplitud de la portadora
A_m = 2         # Amplitud de la señal de mensaje
f_c = 100       # Frecuencia de la portadora (Hz)
f_m = 40        # Frecuencia de la señal de mensaje (Hz)
k_p = np.pi/3   # Constante de modulación de fase (rad)

# Tiempo
t = np.linspace(0, 1, 1000)

# Señal de mensaje
m_t = A_m * np.sin(2 * np.pi * f_m * t)

# Señal portadora
s_t = A_c * np.sin(2 * np.pi * f_c * t )

# Señal modulada
s_t_m = A_c * np.sin(2 * np.pi * f_c * t + k_p * m_t)

# Graficar
plt.figure(figsize=(12, 6))

plt.subplot(3, 1, 1)
plt.title("Señal de Mensaje")
plt.plot(t, m_t, color='blue')
plt.xlim(0,0.3)
plt.grid(True)
plt.tight_layout()

plt.subplot(3, 1, 2)
plt.title("Señal Portadora")
plt.plot(t, s_t, color='red')
plt.xlim(0,0.3)
plt.grid(True)
plt.tight_layout()

plt.subplot(3, 1, 3)
plt.title("Señal PM")
plt.plot(t, s_t_m, color='green')
plt.xlim(0,0.3)
plt.grid(True)
plt.tight_layout()

plt.tight_layout()
plt.show()
