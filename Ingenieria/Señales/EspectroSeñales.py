import numpy as np
import matplotlib.pyplot as plt

np.seterr(divide='ignore', invalid='ignore')

# Configuración de la figura
fig, axs = plt.subplots(4, 2, figsize=(12, 16))

# Frecuencias para los espectros
frequencies = np.linspace(0, 3000, 1000)

# Espectro de AM
am_carrier = 1000  # Frecuencia de portadora
am_signal = np.sinc((frequencies - am_carrier) / 50) + np.sinc((frequencies + am_carrier) / 50)
axs[0, 0].plot(frequencies, am_signal)
axs[0, 0].set_title("Espectro AM")
axs[0, 0].set_xlabel("Frecuencia (kHz)")
axs[0, 0].set_ylabel("Amplitud")

# Espectro de FM
fm_carrier = 1000
fm_signal = np.sinc((frequencies - fm_carrier) / 200) + np.sinc((frequencies + fm_carrier) / 200)
axs[0, 1].plot(frequencies, fm_signal)
axs[0, 1].set_title("Espectro FM")
axs[0, 1].set_xlabel("Frecuencia (MHz)")
axs[0, 1].set_ylabel("Amplitud")

# Espectro de 3G (WCDMA)
wcdma_bandwidth = 5  # MHz
wcdma_signal = np.exp(-0.5 * ((frequencies - 1000) / (wcdma_bandwidth * 200)) ** 2)
axs[1, 0].plot(frequencies, wcdma_signal)
axs[1, 0].set_title("Espectro 3G (WCDMA)")
axs[1, 0].set_xlabel("Frecuencia (MHz)")
axs[1, 0].set_ylabel("Amplitud")

# Espectro de 4G (OFDM)
subcarriers = 12
ofdm_signal = np.sinc((frequencies - 1000) / 10) * np.abs(np.sin(np.pi * subcarriers * frequencies / 1000) / np.sin(np.pi * frequencies / 1000))
axs[1, 1].plot(frequencies, ofdm_signal)
axs[1, 1].set_title("Espectro 4G (OFDM)")
axs[1, 1].set_xlabel("Frecuencia (MHz)")
axs[1, 1].set_ylabel("Amplitud")

# Espectro de Televisión Analógica
tv_analog_signal = np.sinc((frequencies - 500) / 100) + np.sinc((frequencies - 600) / 50)
axs[2, 0].plot(frequencies, tv_analog_signal)
axs[2, 0].set_title("Espectro TV Analógica")
axs[2, 0].set_xlabel("Frecuencia (MHz)")
axs[2, 0].set_ylabel("Amplitud")

# Espectro de Televisión Digital (DVB-T)
ofdm_tv_signal = np.sinc((frequencies - 500) / 50) * np.abs(np.sin(np.pi * subcarriers * frequencies / 500) / np.sin(np.pi * frequencies / 500))
axs[2, 1].plot(frequencies, ofdm_tv_signal)
axs[2, 1].set_title("Espectro TV Digital (DVB-T)")
axs[2, 1].set_xlabel("Frecuencia (MHz)")
axs[2, 1].set_ylabel("Amplitud")

# Espectro de Telefonía Fija (PCM)
pcm_signal = np.abs(np.sin(np.pi * frequencies / 500))
axs[3, 0].plot(frequencies, pcm_signal)
axs[3, 0].set_title("Espectro Telefonía Fija (PCM)")
axs[3, 0].set_xlabel("Frecuencia (kHz)")
axs[3, 0].set_ylabel("Amplitud")

# Quitar gráfico vacío
fig.delaxes(axs[3, 1])

plt.tight_layout()
plt.show()
