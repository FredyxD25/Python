import numpy as np
import matplotlib.pyplot as plt

# Función para generar la matriz de Walsh-Hadamard con dimensiones personalizadas
def walsh_hadamard_matrix(rows, cols):
    # Encuentra la dimensión más cercana como potencia de 2 para una matriz cuadrada
    n = max(rows, cols)
    # Asegúrate de que sea potencia de 2
    n = 1 << (n - 1).bit_length()
    
    # Genera la matriz de Walsh-Hadamard completa de tamaño n x n
    H = np.array([[1]])
    while H.shape[0] < n:
        H = np.vstack((np.hstack((H, H)), np.hstack((H, H - 1))))
    
    # Selecciona solo las filas y columnas necesarias
    return H[:rows, :cols]

# Configuración inicial
num_users = 2  # Número de usuarios
message_length = 8  # Longitud del mensaje en bits

# Generación de mensajes binarios aleatorios para cada usuario
messages = np.random.choice([1, 0], (num_users, message_length))
print("Mensajes de cada usuario:")
print(messages)

# Generación de la matriz de Walsh-Hadamard de tamaño personalizado (2x8)
codes = walsh_hadamard_matrix(2, message_length)
print("\nCódigos asignados a cada usuario (2x8):")
print(codes)

'''# Expansión de los códigos para que coincidan con la longitud del mensaje
codes_expanded = np.repeat(codes[:, np.newaxis], message_length, axis=1)
print("\nCódigos expandidos para cada usuario:")
print(codes_expanded)'''

# Codificación: cada mensaje se multiplica por su código expandido
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

# Gráficos de las señales
plt.figure(figsize=(12, 8))

# Mensajes originales
for i in range(num_users):
    plt.subplot(3, num_users, i + 1)
    plt.stem(range(message_length), messages[i])
    plt.title(f"Mensaje original Usuario {i+1}")
    plt.ylim(-1.5, 1.5)

# Señales codificadas
for i in range(num_users):
    plt.subplot(3, num_users, num_users + i + 1)
    plt.stem(range(message_length), encoded_signals[i])
    plt.title(f"Señal codificada Usuario {i+1}")
    plt.ylim(-1.5, 1.5)

# Señal multiplexada
plt.subplot(3, 1, 3)
plt.stem(range(message_length), multiplexed_signal)
plt.title("Señal Multiplexada")
plt.ylim(-num_users - 0.5, num_users + 0.5)

plt.tight_layout()
plt.show()