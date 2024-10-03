import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import json

# Parámetros de la señal
frecuencia = 5       # Frecuencia de la señal en Hz
duracion = 1         # Duración de la señal en segundos
fs = 100             # Frecuencia de muestreo (samples/segundo)
bits_por_muestra = 5 # Resolución en bits


valor_primer_byte = '11111111'

t = np.linspace(0, duracion, int(fs * duracion), endpoint=False)

def funciones():
    # -----------------------------------------------------------
    # ----------- Generar la señal de onda sinusoidal ----------- 
    # -----------------------------------------------------------

    señal_original_sinusoidal = np.sin(2 * np.pi * frecuencia * t) 
    # Normalización para que los valores estén entre 0 y 1 (lo que facilita la cuantización), es como agregarle un offset
    señal_sinusoidal = (señal_original_sinusoidal - señal_original_sinusoidal.min()) / (señal_original_sinusoidal.max() - señal_original_sinusoidal.min()) #Se agrega un offset para la señal de muestreo

    # -----------------------------------------------------------
    # ----------- Generar la señal de onda triangular ----------- 
    # -----------------------------------------------------------

    señal_original_triangular = signal.sawtooth(2 * np.pi * frecuencia * t, width=0.5)  # Señal triangular
    # Normalización para que los valores estén entre 0 y 1 (lo que facilita la cuantización)
    señal_triangular = (señal_original_triangular - señal_original_triangular.min()) / (señal_original_triangular.max() - señal_original_triangular.min())

    # -----------------------------------------------------------
    # ----------- Generar la señal de onda cuadrada ------------- 
    # -----------------------------------------------------------

    señal_original_cuadrada = signal.square(2 * np.pi * frecuencia * t)  # Señal cuadrada
    # Normalización para que los valores estén entre 0 y 1 (lo que facilita la cuantización)
    señal_cuadrada = (señal_original_cuadrada - señal_original_cuadrada.min()) / (señal_original_cuadrada.max() - señal_original_cuadrada.min())

    # -----------------------------------------------------------
    # ----------- Generar la señal de diente de sierra ----------
    # -----------------------------------------------------------

    señal_original_diente_sierra = t * frecuencia % 1 # Señal sierra
    # Normalización para que los valores estén entre 0 y 1 (lo que facilita la cuantización)
    señal_diente_sierra = (señal_original_diente_sierra - señal_original_diente_sierra.min()) / (señal_original_diente_sierra.max() - señal_original_diente_sierra.min())

    return señal_sinusoidal,señal_original_sinusoidal, señal_triangular,señal_original_triangular, señal_cuadrada,señal_original_cuadrada, señal_diente_sierra,señal_original_diente_sierra

def decimal_a_binario(numero, bit):
    return format(int(numero), f'0{8}b') #Se muestran 8 bits

def señal_cuantizada_normalizada(señal):
    
    ADC = 2 ** bits_por_muestra  # Número de niveles de cuantización, ** es potencia, ADC = 2 ** 5 = 32
    señal_normalizada = np.round(señal * (ADC - 1)) #Se resta 1 para que sean 31 bits y evitar desbordamiento
    señal_cuantizada  = [decimal_a_binario(valor, bits_por_muestra) for valor in señal_normalizada]# Convertir los valores cuantizados a formato binario (PCM)
    return señal_cuantizada , señal_normalizada

def str_int(vector):
    # Convertir la lista de cadenas a enteros
    vector_int = [float(x) for x in vector]
    return vector_int
    
def intercalar_vectores (primer_byte,vector1, vector2, vector3, vector4):
    contador = 0
    limite_maximo = len(t)
    if primer_byte == '':
        modulacion = []
    else:
        modulacion = [primer_byte]
        
    for v1, v2, v3, v4 in zip(vector1, vector2, vector3, vector4):
        if contador < limite_maximo: # Verificar si aún no se ha alcanzado el límite
            modulacion.extend([v1, v2, v3, v4])
            contador += 4  # Incrementar el contador en 3 por cada iteración
    # Cortar la lista al límite máximo si excede
    modulacion = modulacion[:limite_maximo]  # +1 para incluir el valor inicial
    return modulacion 

def guardar_json(señal_cuantizada_sinusoidal,señal_cuantizada_triangular,señal_cuantizada_cuadrada,señal_cuantizada_diente_sierra,bytes_modulados):
    # Crear un diccionario con el vector y un título
    data = {
        "Sinusoidal": {
            "Bytes": señal_cuantizada_sinusoidal
            },
        "Triangular": {
            "Bytes": señal_cuantizada_triangular
            },
        "Cuadrada": {
            "Bytes": señal_cuantizada_cuadrada
            },
        "Sierra": {
            "Bytes": señal_cuantizada_diente_sierra
            },
        "PCM": {
            "Bytes": bytes_modulados
            }
    }

    # Especificar el nombre del archivo JSON
    nombre_archivo1 = 'modulacion_todas_señales_PCM.json'
    # Generar el archivo JSON
    with open(nombre_archivo1, 'w') as archivo_json:
        json.dump(data, archivo_json)

    # Crear un diccionario con el vector y un título
    data = {
        "PCM": {
            "Bytes": bytes_modulados
            }
    }

    # Especificar el nombre del archivo JSON
    nombre_archivo2 = 'modulacion_PCM.json'

    # Generar el archivo JSON
    with open(nombre_archivo2, 'w') as archivo_json:
        json.dump(data, archivo_json)

def grafica(señal_original_sinusoidal,señal_normalizada_sinusoidal,señal_original_triangular,señal_normalizada_triangular,señal_original_cuadrada,señal_normalizada_cuadrada,señal_original_diente_sierra,señal_normalizada_diente_sierra,señal_modulada):
    # Graficar la señal original y cuantizada

    plt.figure(figsize=(10, 8))

    #Grafica señal sinusoidal
    plt.subplot(5, 2, 1)
    plt.plot(t, señal_original_sinusoidal, color='g')
    plt.title('Señal Original (Onda Sinusoidal)')
    plt.grid(True)

    plt.subplot(5, 2, 2)
    plt.stem(t, señal_normalizada_sinusoidal, basefmt=' ',markerfmt='g' ,linefmt='g')
    plt.title(f'Señal Cuantizada con {bits_por_muestra} bits')
    plt.ylim(-2,35)
    plt.grid(True)

    #Grafica señal triangular
    plt.subplot(5, 2, 3)
    plt.plot(t, señal_original_triangular, color='m')
    plt.title('Señal Original (Onda Triangular)')
    plt.grid(True)

    plt.subplot(5, 2, 4)
    plt.stem(t, señal_normalizada_triangular, basefmt=' ',markerfmt='m' ,linefmt='m')
    plt.title(f'Señal Cuantizada con {bits_por_muestra} bits')
    plt.ylim(-2,35)
    plt.grid(True)

    #Grafica señal cuadrada
    plt.subplot(5, 2, 5)
    plt.plot(t, señal_original_cuadrada, color='r')
    plt.title('Señal Original (Onda Cuadrada)')
    plt.grid(True)

    plt.subplot(5, 2, 6)
    plt.stem(t, señal_normalizada_cuadrada, basefmt=' ',markerfmt='r' ,linefmt='r')
    plt.title(f'Señal Cuantizada con {bits_por_muestra} bits')
    plt.ylim(-2,35)
    plt.grid(True)

    #Grafica señal diente de sierra
    plt.subplot(5, 2, 7)
    plt.plot(t, señal_original_diente_sierra, color='orange')
    plt.title('Señal Original (Onda Diente Sierra)')
    plt.grid(True)

    plt.subplot(5, 2, 8)
    plt.stem(t, señal_normalizada_diente_sierra, basefmt=' ',markerfmt='orange' ,linefmt='orange')
    plt.title(f'Señal Cuantizada con {bits_por_muestra} bits')
    plt.ylim(-2,35)
    plt.grid(True)

    plt.subplot(5, 1, 5)

    colors = ['g', 'm', 'r' , 'orange'] * (len(señal_modulada) // 1)
    for i in range(len(señal_modulada)):
        plt.stem(t[i], señal_modulada[i], linefmt=colors[i // 1] , basefmt=" ")
    plt.title(f'Señal Modulada con señal sinusoidal, triangular, cuadrada y diente de sierra con {bits_por_muestra} bits')
    plt.ylim(-2,35)
    plt.grid(True)

    plt.tight_layout()
    plt.show()

def main():
    señal_sinusoidal,señal_original_sinusoidal, señal_triangular,señal_original_triangular, señal_cuadrada,señal_original_cuadrada, señal_diente_sierra,señal_original_diente_sierra = funciones()

# -----------------------------------------------------------------------
# ----------- Cuantización de la señal, discretizar la señal  ----------- 
# -----------------------------------------------------------------------

    señal_cuantizada_sinusoidal     , señal_normalizada_sinusoidal      = señal_cuantizada_normalizada(señal_sinusoidal)
    señal_cuantizada_triangular     , señal_normalizada_triangular      = señal_cuantizada_normalizada(señal_triangular)
    señal_cuantizada_cuadrada       , señal_normalizada_cuadrada        = señal_cuantizada_normalizada(señal_cuadrada)
    señal_cuantizada_diente_sierra  , señal_normalizada_diente_sierra   = señal_cuantizada_normalizada(señal_diente_sierra)

    bytes_modulados = intercalar_vectores(valor_primer_byte,señal_cuantizada_sinusoidal,señal_cuantizada_triangular,señal_cuantizada_cuadrada,señal_cuantizada_diente_sierra)
    señal_modulada = str_int(intercalar_vectores('',señal_normalizada_sinusoidal,señal_normalizada_triangular,señal_normalizada_cuadrada,señal_normalizada_diente_sierra))

    grafica(señal_original_sinusoidal,señal_normalizada_sinusoidal,señal_original_triangular,señal_normalizada_triangular,señal_original_cuadrada,señal_normalizada_cuadrada,señal_original_diente_sierra,señal_normalizada_diente_sierra,señal_modulada)

    guardar_json(señal_cuantizada_sinusoidal,señal_cuantizada_triangular,señal_cuantizada_cuadrada,señal_cuantizada_diente_sierra,bytes_modulados)

if __name__ == "__main__":
    main()