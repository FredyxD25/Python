


def calcular_crc(mensaje: str, polinomio: str) -> str:
    
    # Número de ceros a agregar (grado del polinomio)
    n = len(polinomio) - 1
    
    # Extender el mensaje agregándole n ceros al final
    mensaje_extendido = mensaje + "0" * n

    # Convertir las cadenas en listas de enteros para facilitar el cálculo bit a bit
    mensaje_lista = [int(bit) for bit in mensaje_extendido]
    polinomio_lista = [int(bit) for bit in polinomio]

    # División binaria (algoritmo de división por XOR sin acarreo)
    for i in range(len(mensaje)):
        # Si el bit actual es 1, se realiza el XOR con el polinomio
        if mensaje_lista[i] == 1:
            for j in range(len(polinomio_lista)):
                mensaje_lista[i + j] ^= polinomio_lista[j]

    # El CRC es el residuo, es decir, los últimos n bits de la lista resultante
    crc = ''.join(str(bit) for bit in mensaje_lista[-n:])
    return crc

def binario_a_polinomio(binario: str) -> str:
    """
    Convierte una representación binaria de un polinomio CRC en su equivalente algebraico.

    :param binario: Cadena de bits (ej. "1101" representa x^3 + x^2 + 1).
    :return: Representación algebraica del polinomio en términos de x.
    """
    # Obtener la longitud del polinomio
    grado = len(binario) - 1
    terminos = []

    # Recorrer cada bit y construir el polinomio
    for i, bit in enumerate(binario):
        if bit == '1':  # Solo tomamos los coeficientes 1
            exponente = grado - i
            if exponente > 1:
                terminos.append(f"x^{exponente}")
            elif exponente == 1:
                terminos.append("x")
            else:
                terminos.append("1")  # Para x^0

    # Unir los términos con " + "
    return " + ".join(terminos)

def texto_a_bytes(texto: str) -> list:
    return [ord(caracter) for caracter in texto]

def decimal_a_binario(numero: int) -> str:
    if 0 <= numero <= 255:
        return format(numero, '08b')  # Convierte a binario y rellena con ceros hasta 8 bits
    else:
        raise ValueError("El número debe estar en el rango de 0 a 255.")
    
if __name__ == "__main__":
    # Ejemplo de uso:
    mensaje = "0000111101100100"  # Mensaje binario de entrada
    generador = "11000000000000101"          # Polinomio generador (por ejemplo, x^3 + x + 1)
    
    resultado_crc = calcular_crc(mensaje, generador)
    print("El CRC del mensaje es:", resultado_crc)
    
    polinomio_x = binario_a_polinomio(generador) 
    print(f"Polinomio en términos de x: {polinomio_x}")
    
    #---------------------
    # Ejemplo de uso:
    texto = "Hola, mundo!"
    
    # Convertir texto a bytes
    bytes_ascii = texto_a_bytes(texto)
    print("Texto a bytes:", bytes_ascii)
    
    for num in bytes_ascii:
        print(f"Decimal: {num} -> Binario (8 bits): {decimal_a_binario(num)}")
