import numpy as np
import matplotlib.pyplot as plt
import random

# Función para generar la constelación 16-QAM
def generate_qam_constellation(mod_order):
    M = int(np.sqrt(mod_order))
    re = np.arange(-M+1, M, 2)
    im = np.arange(-M+1, M, 2)
    const = np.array([complex(r, i) for r in re for i in im])
    return const / np.sqrt((np.abs(const)**2).mean())


def constelacion():
    # Definir parámetros de la simulación
    N = 16  # Número de subportadoras reducido para claridad en gráficos
    mod_order = 16  # Orden de modulación (16-QAM)
    N_symbols = 5  # Número de símbolos por subportadora reducido para claridad
    # Generar la constelación QAM
    qam_constellation = generate_qam_constellation(mod_order)

    # Aplicar un factor de escala para aumentar la separación de los puntos
    scale_factor = 2  # Aumenta este valor para mayor separación
    qam_constellation_scaled = qam_constellation * scale_factor

    # Generar datos aleatorios
    np.random.seed(42)  # Fijar semilla para reproducibilidad
    data = np.random.choice(qam_constellation_scaled, size=(N, N_symbols))

    # Graficar constelación original con ángulos y magnitudes 
    fig, ax = plt.subplots(figsize=(8, 8),)# Aumentamos el tamaño del gráfico

    # Calcular valores geométricos y graficar
    ax.scatter(data.real.flatten(), data.imag.flatten(), color='blue', alpha=0.7)

    # Ajuste para evitar que las etiquetas se desborden
    for point in data.flatten():
        angle_deg = np.degrees(np.angle(point)) # Convertir ángulo a grados
        hypotenuse = np.abs(point)              # Hipotenusa
        real = point.real                       # Cateto real
        imag = point.imag                       # Cateto imaginario
        label = (f'h={hypotenuse:.2f}\n'
                f'θ={angle_deg:.2f}°\n'
                f'Re={real:.2f}, I={imag:.2f}i')
        
        # Desplazamos las etiquetas con un offset controlado
        if point.imag < 0:
            y_offset = -0.25
        else:
            y_offset = 0.25
        
        ax.text(point.real, point.imag + y_offset, label, fontsize=8, ha='center', va='center', color='black')

    # Configurar el gráfico
    ax.set_title("Constelación original (16-QAM) - Escalada")
    ax.set_xlabel("Parte real")
    ax.set_ylabel("Parte imaginaria")
    ax.grid(True)

    # Ajustar límites para evitar desbordes
    ax.set_xlim([np.min(data.real) - 1, np.max(data.real) + 1])
    ax.set_ylim([np.min(data.imag) - 1, np.max(data.imag) + 1])

    # Ajustar diseño
    plt.suptitle("Señales sinusoidales 16-QAM", fontsize=16)
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    

def señales():
    # Definición de los parámetros de la señal
    symbols_binary = [
        "0000", "0001", "0010", "0011",
        "0100", "0101", "0110", "0111",
        "1000", "1001", "1010", "1011",
        "1100", "1101", "1110", "1111"
    ]

    # Generar la constelación 16-QAM (amplitud y fase únicas para cada símbolo)
    real_parts = np.array([-3, -1, 1, 3])
    imag_parts = np.array([-3, -1, 1, 3])
    constellation = np.array([x + 1j * y for x in real_parts for y in imag_parts])

    # Parámetros de la gráfica
    duracion = np.pi/5
    fs = 1000  # Frecuencia de muestreo (Hz)
    f = 5      # Frecuencia de la portadora (Hz)
    t = np.linspace(0, duracion, int(fs * duracion), endpoint=False)  
    dis_titulo = 1/3
    plt.figure(figsize=(20/1.5, 10/1.5))
    plt.subplot(1, 1, 1)

    for i, (symbol, constellation_point) in enumerate(zip(symbols_binary, constellation)):

        # Amplitud y fase del símbolo
        amplitude = np.abs(constellation_point)
        phase = np.angle(constellation_point)

        # Generar la señal sinusoidal para este símbolo
        signal = amplitude * np.cos(2 * np.pi * f * t + phase)

        # Graficar la señal
        random_color = (random.random(), random.random(), random.random())
        plt.plot(t, signal, color=random_color)
        plt.text(dis_titulo,4.5,f"{symbol}", fontsize=10, color=random_color)
        plt.ylim(-5, 5)
        dis_titulo += duracion
        t+=duracion


    # Ajustar diseño
    plt.suptitle("Señales sinusoidales 16-QAM", fontsize=16)
    plt.tight_layout(rect=[0, 0, 1, 0.96])

def main():
    constelacion()
    señales()
    plt.show()
    
if __name__ == "__main__":
    main()