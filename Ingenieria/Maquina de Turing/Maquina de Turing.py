from sys import argv

def cargar_cintas(archivo_cintas):
    # Función para cargar las cintas desde un archivo
    return [linea.strip() for linea in archivo_cintas]

def cargar_programa(archivo_programa):
    # Función para cargar el programa de la máquina de Turing desde un archivo
    transiciones = {}
    estados_finales = set()
    tipo_maquina = None  # Variable para almacenar el tipo de máquina
    for linea in archivo_programa:
        if linea.strip() == '':
            continue
        partes = linea.split()
        if partes[0] == 'F':
            estados_finales.add(partes[1])
        else:
            if len(partes) == 3:  # Si la línea tiene 3 partes, es un formato de AFD
                tipo_maquina = 'AFD'
                estado_actual, simbolo_actual, estado_siguiente = partes
                transiciones[(estado_actual, simbolo_actual)] = estado_siguiente
            elif len(partes) == 5:  # Si la línea tiene 5 partes, es un formato de MT
                tipo_maquina = 'MT'
                estado_actual, simbolo_actual, estado_siguiente, simbolo_salida, direccion_cabezal = partes
                transiciones[(estado_actual, simbolo_actual)] = (estado_siguiente, simbolo_salida, direccion_cabezal)
    return transiciones, estados_finales, tipo_maquina

def simular_AFD(transiciones, estado_inicial, estados_finales, cinta):
    # Función para simular un autómata finito determinista
    estado_actual = estado_inicial
    for simbolo in cinta:
        if (estado_actual, simbolo) not in transiciones:
            return False
        estado_actual = transiciones[(estado_actual, simbolo)]
    return estado_actual in estados_finales

def simular_MT(transiciones, estado_inicial, estados_finales, cinta):
    # Función para simular una máquina de Turing
    estado_actual = estado_inicial
    cinta = list(cinta)
    posicion_cabezal = 0
    while True:
        if estado_actual in estados_finales:
            return True
        if (estado_actual, cinta[posicion_cabezal]) not in transiciones:
            return False
        nuevo_estado, simbolo_escribir, direccion = transiciones[estado_actual, cinta[posicion_cabezal]]
        cinta[posicion_cabezal] = simbolo_escribir
        if direccion == 'R':
            posicion_cabezal += 1
        elif direccion == 'L':
            posicion_cabezal -= 1
        estado_actual = nuevo_estado
        if posicion_cabezal < 0:
            cinta.insert(0, '_')
            posicion_cabezal = 0
        elif posicion_cabezal >= len(cinta):
            cinta.append('_')
    return False

resultado_mensaje = {True: 'Aceptada', False: 'Rechazada'}

def main():
    if len(argv) < 2:
        print("Uso: {} tipo_programa".format(argv[0]))
        print("Donde 'tipo_programa' puede ser 'AFD' o 'MT' para Autómata Finito o Máquina de Turing respectivamente.")
        return

    tipo_maquina = argv[1]

    if tipo_maquina not in ['AFD', 'MT']:
        print("El tipo de programa debe ser 'AFD' o 'MT'.")
        return

    with open(r"C:\Users\User\Documents\UD_ING\9\Cuantica\parcial\programa.txt", 'r') as archivo_programa:
        transiciones, estados_finales, tipo_programa = cargar_programa(archivo_programa)

    with open("cintas.txt", 'r') as archivo_cintas:
        cintas = cargar_cintas(archivo_cintas)

    if tipo_programa == 'AFD':
        for cinta in cintas:
            print('La entrada', cinta, " es ", resultado_mensaje[simular_AFD(transiciones, '0', estados_finales, cinta)])
    elif tipo_programa == 'MT':
        for cinta in cintas:
            print('La entrada', cinta, " es ", resultado_mensaje[simular_MT(transiciones, '0', estados_finales, cinta)])
    else:
        print("El tipo de programa no pudo ser identificado.")

if __name__ == "__main__":
    main()