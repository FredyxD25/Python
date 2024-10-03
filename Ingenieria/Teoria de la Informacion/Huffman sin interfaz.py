import heapq
from collections import Counter
import math
import json

# Paso 1: Calcular la probabilidad de cada letra
def calcular_probabilidades(frase):
    # Eliminar espacios y convertir a minúsculas
    frase = frase.replace(" ", "").lower()
    
    # Contar la frecuencia de cada letra
    frecuencias = Counter(frase)
    total_letras = sum(frecuencias.values())
    
    # Calcular la probabilidad de cada letra
    probabilidades = {letra: frecuencia / total_letras for letra, frecuencia in frecuencias.items()}
    return probabilidades

# Paso 2: Aplicar la codificación de Huffman
class Nodo:
    def __init__(self, simbolo, probabilidad):
        self.simbolo = simbolo
        self.probabilidad = probabilidad
        self.izquierda = None
        self.derecha = None
    
    def __lt__(self, otro):
        return self.probabilidad < otro.probabilidad #Compara dos objetos, self objeto actual < otro objeto a comparar
    
    # Sobrescribir el método __repr__ para visualizar correctamente
    def __repr__(self):
        return f"Nodo(simbolo={self.simbolo}, probabilidad={self.probabilidad})"

# Paso 3: Calcular la entropia
def calcular_entropia(probabilidades):
    entropia = sum(p * math.log2(1/p) for p in probabilidades.values() if p > 0)
    return entropia

# Paso 4: Calcular el largo medio
def calcular_largo_medio(probabilidades, longitudes_codigos):
    i = 0
    largo_medio = 0
    v_codigos = []
    letras_codigos =[]
    v_probabilidades = []
    letras_probabilidades =[]
    
    for letras, codigo in longitudes_codigos.items():
        letras_codigos.append(letras)
        v_codigos.append(len(codigo))
        print(letras_codigos)
        print(v_codigos)
        
    for letras, pro in probabilidades.items():
        letras_probabilidades.append(letras)
        v_probabilidades.append(pro)
        print(letras_probabilidades)
        print(v_probabilidades)
    
    v_codigos_letras = intercalar_vectores (letras_codigos, v_codigos)
    v_probabilidades_letras = intercalar_vectores (letras_probabilidades, v_probabilidades)
    print ("vector intercalado 1 :", v_codigos_letras)
    print ("vector intercalado 2 :", v_probabilidades_letras)
    
    # Identificadores comunes
    identificadores = list(v_codigos_letras.keys())

    # Construir el nuevo vector alineado
    resultado = []
    for identificador in identificadores:
        #resultado.append(identificador) #letra comun
        resultado.append(v_codigos_letras.get(identificador, None))  # Valor del primer vector
        resultado.append(v_probabilidades_letras.get(identificador, None))  # Valor del segundo vector
    
    print ("vector intercalado :", resultado)
    
    while(i < len(resultado)):
        largo_medio = resultado[i]*resultado[i+1] + largo_medio
        i += 2
    i = 0    
    return largo_medio

# Paso 5: Calcular la eficiencia
def calcular_eficiencia(entropia, largo_medio):
    if largo_medio > 0:
        eficiencia = (entropia / largo_medio) *100  #eficiencia en porcentaje
    else:
        eficiencia = 0
    return eficiencia

def crear_arbol_huffman(probabilidades):
    # Crear una cola de prioridad con objetos
    cola_prioridad = [Nodo(simbolo, probabilidad*100) for simbolo, probabilidad in probabilidades.items()] #Se hace el diccionario con las letras y la probabilidad
    print("\n Cola antes de heapify:", cola_prioridad)
    heapq.heapify(cola_prioridad) #Organizar de menor a mayor con el constructor __lt__(self, otro):
    print("Cola después de heapify:", cola_prioridad,"\n")
    
    # Crear el árbol de Huffman
    while len(cola_prioridad) > 1:
        cuenta = 0
        # Extraer los dos objetos con menor probabilidad nodo
        nodo_izquierdo = heapq.heappop(cola_prioridad)
        nodo_derecho = heapq.heappop(cola_prioridad)
        
        suma_nodo_izquierdo_derecho = nodo_izquierdo.probabilidad + nodo_derecho.probabilidad

        try:
            while (cuenta < len(cola_prioridad)):
                if cola_prioridad[0].probabilidad != suma_nodo_izquierdo_derecho:
                    break
                elif cola_prioridad[cuenta].probabilidad == suma_nodo_izquierdo_derecho:
                    suma_nodo_izquierdo_derecho -= 0.1
                cuenta += 1
        except IndexError:
            suma_nodo_izquierdo_derecho -= 0.1
            
        print("nodo izquierdo",nodo_izquierdo)
        print("nodo derecho",nodo_derecho)
        
        # Crear un nuevo objeto con la suma de sus probabilidades, sin simbolo
        nuevo_nodo = Nodo(None,suma_nodo_izquierdo_derecho )
        print("suma ultimas dos probabilidades",nuevo_nodo,"\n")
        nuevo_nodo.izquierda = nodo_izquierdo
        nuevo_nodo.derecha = nodo_derecho

        # Insertar el nuevo objeto en la cola de prioridad   
        heapq.heappush(cola_prioridad, nuevo_nodo) 
        heapq.heapify(cola_prioridad) 
        
        print("Cola después de heapify:", cola_prioridad,"\n")
        
    # El último objeto es la raíz del árbol
    return cola_prioridad[0]

def asignar_codigos_huffman(nodo, codigo_actual="", codigos={}):
    print("codigo huffman",nodo)
    if nodo.simbolo is not None:
        # Si es una hoja, asignar el código actual
        codigos[nodo.simbolo] = codigo_actual
        print(codigo_actual,codigos)
    else:
        # Recorrer el árbol de forma recursiva
        asignar_codigos_huffman(nodo.derecha, codigo_actual + "0", codigos)
        asignar_codigos_huffman(nodo.izquierda, codigo_actual + "1", codigos)
        
    return codigos

# Función principal que integra todo
def codificacion_huffman(frase):
    # Paso 1: Calcular probabilidades
    probabilidades = calcular_probabilidades(frase)
    
    # Paso 2: Crear el árbol de Huffman
    arbol_huffman = crear_arbol_huffman(probabilidades)
    
    # Paso 3: Asignar códigos de Huffman
    codigos_huffman = asignar_codigos_huffman(arbol_huffman, codigos={})
    
    # Codificar la frase
    frase_codificada = ''.join([codigos_huffman[letra] for letra in frase.replace(" ", "").lower()])
    
    return codigos_huffman, frase_codificada

def intercalar_vectores (vector1, vector2):
    contador = 0
    modulacion = []
    for v1, v2 in zip(vector1, vector2):
        modulacion.extend([v1, v2])
        contador += 2  # Incrementar el contador en 2 por cada iteración 
    #Transformar vector en diccionario
    diccionario = {modulacion[i]: modulacion[i+1] for i in range(0, len(modulacion), 2)}
    contador = 0
    return diccionario 

def guardar_json(frase,probabilidades,codigos_huffman,entropia,largo_medio,eficiencia,frase_codificada):
    v_letras_1 = []
    v_letras_2 = []
    v_probabilidades = []
    v_codigos_huffman = []
    
    for letra, prob in probabilidades.items():
        v_letras_1.append(letra)
        v_probabilidades.append(prob)
        
    for letra, codigo in codigos_huffman.items():
        v_letras_2.append(letra)
        v_codigos_huffman.append(codigo)
    # Guardar informacion en un json
    data = {
        "Mensaje": frase,
        #"Probabilidades": intercalar_vectores(v_letras_1,v_probabilidades),
        #"Entropia": entropia,
        #"Largo medio": largo_medio,
        #"Eficiencia": eficiencia,
        "Codigo Huffman": intercalar_vectores(v_letras_2,v_codigos_huffman),
        "Mensaje Codificado": frase_codificada
        }

    # Generar el archivo JSON
    with open('Huffman.json', 'w') as archivo_json:
        json.dump(data, archivo_json)

def main():
    
    #frase = ("AAAAABCDDE")
    frase = input("Introduce una frase: ")
    #frase = ("mi_mama_me_mima")
    ''' m   1
        _   01
        A   000
        I   0010
        E   0011
    '''
    
    "https://es.planetcalc.com/2481/?probability=%5B%7B%22name%22%3A%22A%22%2C%22value%22%3A40%2C%22pkID%22%3A%2228632%22%2C%22save_label%22%3A%22%22%2C%22cancel_label%22%3A%22%22%7D%2C%7B%22name%22%3A%22I%22%2C%22value%22%3A13.333%2C%22pkID%22%3A%2228633%22%2C%22save_label%22%3A%22%22%2C%22cancel_label%22%3A%22%22%7D%2C%7B%22name%22%3A%22_%22%2C%22value%22%3A20%2C%22pkID%22%3A%2228634%22%2C%22save_label%22%3A%22%22%2C%22cancel_label%22%3A%22%22%7D%2C%7B%22name%22%3A%22A%22%2C%22value%22%3A20%2C%22pkID%22%3A%2228635%22%2C%22save_label%22%3A%22%22%2C%22cancel_label%22%3A%22%22%7D%2C%7B%22name%22%3A%22E%22%2C%22value%22%3A6.6666%2C%22pkID%22%3A%2228636%22%2C%22save_label%22%3A%22%22%2C%22cancel_label%22%3A%22%22%7D%5D&inverted=1"
    
    # Calcular probabilidades
    probabilidades = calcular_probabilidades(frase)
    # Codigo Huffman
    codigos_huffman, frase_codificada = codificacion_huffman(frase)
    # Calcular entropía
    entropia = calcular_entropia(probabilidades)
    
    # Calcular largo medio
    largo_medio = calcular_largo_medio(probabilidades,codigos_huffman)
        
    # Calcular eficiencia
    eficiencia = calcular_eficiencia(entropia,largo_medio)

    guardar_json(frase,probabilidades,codigos_huffman,entropia,largo_medio,eficiencia,frase_codificada)
    
    print("\nProbabilidades de cada letra: ")
    for letra, prob in probabilidades.items():
        print(f"{letra}: {prob:.4f}")

    print("\nCódigos de Huffman para cada letra: ")
    for letra, codigo in codigos_huffman.items():
        print(f"{letra}: {codigo}")

    print("\nFrase codificada usando Huffman: ")
    print(frase_codificada)
    
    print("\nEntropia: ")
    print(f"{entropia:.4f}")
    
    print("\nLargo medio: ")
    print(f"{largo_medio:.4f}")
    
    print("\nEficiencia: ")
    print(f"{eficiencia:.2f}%\n")
    
if __name__ == "__main__":
    while(True):main()