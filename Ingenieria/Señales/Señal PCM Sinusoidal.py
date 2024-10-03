import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la señal
frecuencia = 5       # Frecuencia de la señal en Hz
duracion = 1         # Duración de la señal en segundos
fs = 100             # Frecuencia de muestreo (samples/segundo)
bits_por_muestra = 5 # Resolución en bits

#------------ Generar la señal de onda sinusoidal

# t genera un array de tiempo desde 0.0 con un aumento de 0.01 hasta 1

t = np.linspace(0, duracion + 1/(int(fs * duracion)), int(fs * duracion), endpoint=False)  #inicio, final, Numero de muestras (no debe ser negativo), endpoint = True (se coloca cuando la ultima muestra es el STOP)

señal_original = np.sin(2 * np.pi * frecuencia * t) #Ecuacion de la señal, se puede agregar un offset para no tener que normalizar la grafica

# Normalización para que los valores estén entre 0 y 1 (lo que facilita la cuantización), es como agregarle un offset
señal_normalizada = (señal_original - señal_original.min()) / (señal_original.max() - señal_original.min()) #Se agrega un offset para la señal de muestreo

# Cuantización de la señal, discretizar la señal 
ADC = 2 ** bits_por_muestra  # Número de niveles de cuantización, ** es potencia, ADC = 2 ** 5 = 32
señal_cuantizada = np.round(señal_normalizada * (ADC - 1)) #Se resta 1 para que sean 31 bits y evitar desbordamiento

'''señal_cuantizada = array([15., 20., 25., 28., 30., 31., 30., 28., 24., 20., 15., 10.,  6.,
                            3.,  1.,  0.,  1.,  3.,  7., 12., 16., 21., 25., 29., 31., 31.,
                            30., 27., 23., 19., 14.,  9.,  5.,  2.,  0.,  0.,  1.,  4.,  8.,
                            13., 17., 22., 26., 29., 31., 31., 29., 27., 23., 18., 13.,  8.,
                            4.,  2.,  0.,  0.,  2.,  5.,  9., 14., 18., 23., 27., 30., 31.,
                            31., 29., 26., 22., 17., 12.,  8.,  4.,  1.,  0.,  0.,  2.,  6.,
                            10., 14., 19., 24., 28., 30., 31., 30., 28., 25., 21., 16., 11.,
                            7.,  3.,  1.,  0.,  1.,  3.,  6., 11., 15.])'''

# Convertir los valores cuantizados a formato binario (PCM)
def decimal_a_binario(numero, bit):
    #return format(int(numero), f'0{bit}b')
    return format(int(numero), f'0{8}b') #Se muestran 8 bits

señal_pcm = [decimal_a_binario(valor, bits_por_muestra) for valor in señal_cuantizada]

'''muestra cuantizada en binario = ['00001111', '00010100', '00011001', '00011100', '00011110', 
                                    '00011111', '00011110', '00011100', '00011000', '00010100', 
                                    '00001111', '00001010', '00000110', '00000011', '00000001', 
                                    '00000000', '00000001', '00000011', '00000111', '00001100', 
                                    '00010000', '00010101', '00011001', '00011101', '00011111', 
                                    '00011111', '00011110', '00011011', '00010111', '00010011', 
                                    '00001110', '00001001', '00000101', '00000010', '00000000', 
                                    '00000000', '00000001', '00000100', '00001000', '00001101', 
                                    '00010001', '00010110', '00011010', '00011101', '00011111', 
                                    '00011111', '00011101', '00011011', '00010111', '00010010', 
                                    '00001101', '00001000', '00000100', '00000010', '00000000', 
                                    '00000000', '00000010', '00000101', '00001001', '00001110', 
                                    '00010010', '00010111', '00011011', '00011110', '00011111', 
                                    '00011111', '00011101', '00011010', '00010110', '00010001', 
                                    '00001100', '00001000', '00000100', '00000001', '00000000', 
                                    '00000000', '00000010', '00000110', '00001010', '00001110', 
                                    '00010011', '00011000', '00011100', '00011110', '00011111', 
                                    '00011110', '00011100', '00011001', '00010101', '00010000', 
                                    '00001011', '00000111', '00000011', '00000001', '00000000', 
                                    '00000001', '00000011', '00000110', '00001011', '00001111']'''

# Graficar la señal original y cuantizada
plt.figure(figsize=(10, 6))

plt.subplot(3, 1, 1)
plt.plot(t, señal_original, label='Señal Original')
plt.title('Señal Original (Onda Sinusoidal)')
plt.grid(True)
plt.legend()

plt.subplot(3, 1, 2)
#plt.step(t, señal_cuantizada, label='Señal Cuantizada', where='mid')
plt.stem(t, señal_cuantizada, label='Señal Cuantizada')
plt.title(f'Señal Cuantizada con {bits_por_muestra} bits')
plt.grid(True)
plt.legend()

# Mostrar los bits de la señal PCM para un segmento de la señal
plt.subplot(3, 1, 3)
plt.title('Señal PCM (bits)')
for i in range(len(señal_pcm[:10])):
    plt.text(i/fs, 0.5, señal_pcm[i], fontsize=10, ha='center')
plt.xlim(0, 10/fs)
plt.ylim(0, 1)
plt.grid(True)

plt.tight_layout()
plt.show()
