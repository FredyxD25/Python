import tkinter as tk
import automata

# Crear la ventana principal
root = tk.Tk()
root.title("Automata / Validador")

# Establecer el tamaño de la ventana principal
root.geometry("650x550")

# Mostrar el formulario inicial
automata.show(root)

# Mostrar la ventana principal
root.mainloop()