import tkinter as tk
import automata
#Librerias a importar
import networkx as nx               # grafo
import matplotlib.pyplot as plt     #grafo bonito
from PIL import Image, ImageTk      #
import math                         #raiz cuadrada

##
# Interfaz del buscador
def show(root, estado_inicial, conjunto_estados_finales, transiciones):
    farm_validador = tk.Frame(root)
    farm_validador.pack()
    
    tk.Label(farm_validador, text="Ingrese palabra:").grid(row=350, column=0, pady=8)
    palabra = tk.Entry(farm_validador)
    palabra.grid(row=350, column=1, pady=5)

    resultado_label = tk.Label(farm_validador, text="")
    resultado_label.grid(row=351, column =1, pady=5)

    boton_buscar = tk.Button(farm_validador, text="Verificar", command=lambda: revisar_palabra(
        resultado_label,transiciones, palabra.get(), estado_inicial, conjunto_estados_finales))
    boton_buscar.grid(row=353,columnspan=2,pady=8)

    # Botón para volver al formulario
    boton_volver = tk.Button(farm_validador, text="Nuevo Automata",
                              command=lambda: volver_al_formulario(root, farm_validador))
    boton_volver.grid(row=354, columnspan=2)
    
    plot_graph(transiciones,farm_validador,conjunto_estados_finales)

        # Botón para volver al graficar
    boton_graficar = tk.Button(farm_validador, text="Recargar Automata",
                              command=lambda: plot_graph(transiciones,farm_validador,conjunto_estados_finales)
                              )
    boton_graficar.grid(row=353,columnspan=1 ,pady=8)

# Función para volver al formulario
def volver_al_formulario(root, farm_validador):
    print("Presiono Volver al automata")
    farm_validador.pack_forget()
    automata.reset_variables()  # Resetea variables
    automata.show(root)
    

def revisar_palabra(resultado_label,transiciones, palabra, estado_inicial, conjunto_estados_finales):
    resultado = evaluar_palabra(transiciones, palabra, estado_inicial, conjunto_estados_finales)
    if resultado:
        resultado_label.config(text=f"La palabra: {palabra} es aceptada por el automata!")
    else:
        resultado_label.config(text=f"La palabra: {palabra} NO! es aceptada por el automata!")

def evaluar_palabra(transiciones, palabra, estado_inicial, conjunto_estados_finals):
    estado_actual = estado_inicial
    
    for simbolo in palabra:
        transicion = (estado_actual, simbolo)
        if transicion not in transiciones:
            return False  # No hay transición definida para el estado actual y el símbolo
        estado_actual = transiciones[transicion]
    return estado_actual in conjunto_estados_finals

def plot_graph(transiciones,farm_validador,conjunto_estados_finales):

    # Clear the previous graph if it exists
    plt.clf()

    # Create an empty directed graph
    G = nx.DiGraph()

    # Create dictionaries to store merged labels for self-loops
    self_loop_labels = {}
    
    # Create dictionaries to store labels for bidirectional edges
    bidirectional_labels = {}

    # Add edges and labels from the dictionary
    for (q, p), r in transiciones.items():
        if G.has_edge(q, r):
            # If an edge between q and r already exists, append the label
            # with a comma
            if (q, r) in self_loop_labels:
                self_loop_labels[(q, r)].append(p)
            else:
                self_loop_labels[(q, r)] = [G[q][r]['label'], p]
        else:
            # Check for bidirectional edges
            if (r, q) in transiciones:
                if (r, q) in bidirectional_labels:
                    bidirectional_labels[(r, q)].append(p)
                else:
                    bidirectional_labels[(r, q)] = [p]
                if (q, r) in bidirectional_labels:
                    bidirectional_labels[(q, r)].append(p)
                else:
                    bidirectional_labels[(q, r)] = [p]
            else:
                # Otherwise, add a new edge
                G.add_edge(q, r, label=p)

    # Draw the graph
    pos = nx.spring_layout(G)
    node_colors = ['lightcoral' if label in conjunto_estados_finales else 'skyblue' for label in G.nodes()]

    # Draw edges
    nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=1500, font_size=12, font_weight='bold', arrows=True)

    # Add edge labels
    edge_labels = {(q, r): data['label'] for q, r, data in G.edges(data=True)}
    for (q, r), label in edge_labels.items():
        # Calculate the position of the arrowhead
        x1, y1 = pos[q]
        x2, y2 = pos[r]
        dx = x2 - x1
        dy = y2 - y1
        length = math.sqrt(dx**2 + dy**2)
        if length != 0:  # To handle the case where arrows point to the same node
            label_pos = (x1 + dx/length * 0.7, y1 + dy/length * 0.7)  # Adjust the factor as needed
        else:
            # Offset the label position slightly from the node's position
            label_pos = (x1 + 0.1, y1 + 0.1)
        plt.text(label_pos[0], label_pos[1], label, fontsize=12, fontweight='bold')

    # Add labels for self-loops
    for edge, labels in self_loop_labels.items():
        q, r = edge
        label = ', '.join(labels)
        # Adjust label position for self-loops
        x, y = pos[q]
        plt.text(x + 0.05, y + 0.05, label, fontsize=12, fontweight='bold')

    # Add labels for bidirectional edges
    for edge, labels in bidirectional_labels.items():
        q, r = edge
        label = ', '.join(labels)
        # Adjust label position based on the relative positions of nodes q and r
        label_position = (pos[q][0] + pos[r][0]) / 2, (pos[q][1] + pos[r][1]) / 2
        plt.text(label_position[0], label_position[1], label, fontsize=12, fontweight='bold', ha='center', va='center')

    # Save the plot as an image
    plt.savefig("graph.png")

    # Open the saved image using PIL
    img = Image.open("graph.png")

    # Resize the image if necessary
    img = img.resize((550, 300))

    # Convert the image to a format that tkinter can display
    img_tk = ImageTk.PhotoImage(img)

    # Display the image in a tkinter Label widget
    image_label = tk.Label(farm_validador, image=img_tk)
    image_label.image = img_tk  # Keep a reference to avoid garbage collection

    # Place the image label using the grid layout manager
    image_label.grid(row=0, column=1)  # You can adjust row and column values as needed
