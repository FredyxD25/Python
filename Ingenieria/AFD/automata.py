import tkinter as tk
import validador

# Variables globales
num_rows = 1
num_cols = 3
conjunto_estados_finals = []
estado_inicial = None

# Inicializar entry_fields y buffer_transiciones
entry_fields = [[] for _ in range(num_rows)]
buffer_transiciones = {}

# Interfaz del formulario
def show(root):
    global num_cols, num_rows, add_row_button, enviar_button, entry_fields,estado_inicial, conjunto_estados_finals
    #,label_estado_inicial,estado_inicial
    automata = tk.Frame(root)
    automata.pack()
    
    # Labels para el texto sobre la cuadrícula
    tk.Label(automata, text="Estado").grid(row=0, column=0)
    tk.Label(automata, text="Simbolo").grid(row=0, column=1)
    tk.Label(automata, text="Objetivo").grid(row=0, column=2)

    # Crear la fila inicial de widgets Entry
    for col in range(num_cols):
        entry = tk.Entry(automata, width=10)
        entry.grid(row=1, column=col)
        entry_fields[0].append(entry)

    # Botón para enviar el formulario
    enviar_button = tk.Button(automata, text="Enviar", command=lambda: enviar_formulario(
        root, automata,estado_inicial.get(),conjunto_estados_finals.get()
        ))
    enviar_button.grid(row=4, column=3, pady=10)

    # etiqueta y boton for "Estado Inicial"
    label_estado_inicial = tk.Label(automata, text="Estado Inicial")
    label_estado_inicial.grid(row=3, column=0, pady=10)
    estado_inicial = tk.Entry(automata, width=10)
    estado_inicial.grid(row=3, column=1)

     # etiqueta y boton for "Estados Finales"
    label_estado_final = tk.Label(automata, text="Estado(s) Finale(s)")
    label_estado_final.grid(row=4, column=0, pady=10)
    conjunto_estados_finals = tk.Entry(automata, width=10)
    conjunto_estados_finals.grid(row=4, column=1)


    hint = tk.Label(automata, text="Ej: q3,q5")
    hint.grid(row=5, column=1, pady=10)

    # Botón para agregar una nueva fila
    add_row_button = tk.Button(automata, text="Nueva fila", width=10)
    add_row_button.grid(row=2, column=0, pady=10)
    add_row_button.config(command=lambda: add_new_row(
        automata, enviar_button, add_row_button,
        label_estado_inicial,estado_inicial,
        conjunto_estados_finals,label_estado_final,hint
        ))
    print("formulario mostrado")

def hide(frame):
    frame.pack_forget()

# Función para enviar el formulario y cambiar a la interfaz del buscador
def enviar_formulario(root, frame,estado_inicial,conjunto_estados_finals):
    global buffer_transiciones
    buffer_transiciones = {}
    for row in range(len(entry_fields)):
        if len(entry_fields[row]) == 3:  # Asegurar que cada fila tenga exactamente tres entradas
            estado = entry_fields[row][0].get().strip()
            simbolo = entry_fields[row][1].get().strip()
            objetivo = entry_fields[row][2].get().strip()
            if estado and simbolo and objetivo:
                buffer_transiciones[(estado, simbolo)] = objetivo
    
    # Ahora buffer_transiciones contiene los datos de transición
    print("Transiciones:", buffer_transiciones)
    print("Estado Inicial:", estado_inicial)
    print("Estado(s) Final(es):", conjunto_estados_finals)
    
    hide(frame)  # Ocultar la interfaz del formulario
    validador.show(root, estado_inicial, conjunto_estados_finals, buffer_transiciones)  # Mostrar la interfaz del validador


# Función para agregar una nueva fila
def add_new_row(automata, enviar_button, add_row_button,label_estado_inicial,estado_inicial,conjunto_estados_finals,label_estado_final,hint):
    global num_rows, entry_fields
    num_rows += 1
    entry_fields.append([])
    for col in range(num_cols):
        entry = tk.Entry(automata, width=10)
        entry.grid(row=num_rows, column=col)
        entry_fields[num_rows-1].append(entry)
    # Mover los botones a la siguiente fila
    add_row_button.grid(row=num_rows+1, column=0, pady=10)
    #
    estado_inicial.grid(row=num_rows+2, column=1, pady=10)
    label_estado_inicial.grid(row=num_rows+2, column=0, pady=10)
    ##
    label_estado_final.grid(row=num_rows+3, column=0, pady=10)
    conjunto_estados_finals.grid(row=num_rows+3, column=1, pady=10)
    ##
    enviar_button.grid(row=num_rows+3, column=3, pady=10)
    hint.grid(row=num_rows+4, column=1, pady=10)

    print("se creó una nueva fila")

# Función para reiniciar entry_fields y buffer_transiciones
def reset_variables():
    global entry_fields, buffer_transiciones, conjunto_estados_finals,estado_inicial
    entry_fields = [[] for _ in range(num_rows)]
    buffer_transiciones = {}
    conjunto_estados_finals = []
    estado_inicial = None
    print('Variables reseteadas')
