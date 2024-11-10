import numpy as np

# Función para generar la matriz de Walsh-Hadamard para los códigos CDM
def walsh_hadamard_matrix(size):
    if size == 1:
        return np.array([[1]])
    else:
        smaller_matrix = walsh_hadamard_matrix(size // 2)
        top = np.hstack((smaller_matrix, smaller_matrix))
        bottom = np.hstack((smaller_matrix, -smaller_matrix))
        return np.vstack((top, bottom))

# Configuración inicial
num_users = 2  # Número de usuarios
message_length = 8  # Longitud del mensaje en bits

# Generación de mensajes binarios aleatorios para cada usuario
messages = np.random.choice([1, -1], (num_users, message_length))
print("Mensajes de cada usuario:")
print(messages)

# Generación de la matriz de Walsh-Hadamard de tamaño adecuado
codes = walsh_hadamard_matrix(2)  # Genera una matriz 2x2 para 2 usuarios
print("\nCódigos asignados a cada usuario:")
print(codes)

# Codificación: cada mensaje se multiplica por su código
encoded_signals = np.array([messages[i] * codes[i] for i in range(num_users)])
print("\nSeñales codificadas de cada usuario:")
print(encoded_signals)

# Multiplexación: suma todas las señales codificadas
multiplexed_signal = np.sum(encoded_signals, axis=0)
print("\nSeñal multiplexada (suma de todas las señales codificadas):")
print(multiplexed_signal)

# Decodificación: se multiplica la señal multiplexada por el código del usuario y luego se promedia
decoded_messages = []
for i in range(num_users):
    decoded_message = multiplexed_signal * codes[i]
    averaged_message = np.sign(np.sum(decoded_message.reshape((message_length, -1)), axis=1))
    decoded_messages.append(averaged_message)

print("\nMensajes decodificados para cada usuario:")
for i, decoded_message in enumerate(decoded_messages):
    print(f"Usuario {i+1}: {decoded_message}")
