import tkinter as tk
from tkinter import ttk

class CRC_GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora CRC")
        self.root.geometry("400x350")
        self.root.resizable(False, False)

        # Selección de CRC
        self.tipo_crc = tk.StringVar(value="CRC-32")
        ttk.Label(root, text="Selecciona el tipo de CRC:").pack(anchor="w", padx=10, pady=5)

        opciones = ["CRC-32", "CRC-16"]
        for opcion in opciones:
            ttk.Radiobutton(root, text=opcion, variable=self.tipo_crc, value=opcion, command=self.limpiar_polinomio).pack(anchor="w", padx=20)

        # Cuadros de entrada
        self.input_frame = ttk.Frame(root)
        self.input_frame.pack(pady=10, padx=10, fill="x")

        ttk.Label(self.input_frame, text="Mensaje en binario:").grid(row=0, column=0, sticky="w")
        self.entry_binario = ttk.Entry(self.input_frame, width=50, validate="key", validatecommand=(root.register(self.validar_binario), "%P"))
        self.entry_binario.grid(row=0, column=1, sticky="ew", padx=5)

        ttk.Label(self.input_frame, text="Mensaje en texto:").grid(row=1, column=0, sticky="w")
        self.entry_texto = ttk.Entry(self.input_frame)
        self.entry_texto.grid(row=1, column=1, sticky="ew", padx=5)

        self.entry_binario.bind("<KeyRelease>", self.desactivar_otro)
        self.entry_texto.bind("<KeyRelease>", self.desactivar_otro)

        # Entrada para el polinomio generador
        ttk.Label(self.input_frame, text="Polinomio generador (bits):").grid(row=2, column=0, sticky="w")
        self.entry_polinomio = ttk.Entry(self.input_frame, validate="key", validatecommand=(root.register(self.validar_polinomio), "%P"))
        self.entry_polinomio.grid(row=2, column=1, sticky="ew", padx=5)

        # Resultado (de solo lectura)
        ttk.Label(root, text="Resultado:").pack(anchor="w", padx=10, pady=5)
        self.resultado = tk.StringVar()
        self.entry_resultado = ttk.Entry(root, textvariable=self.resultado, state="readonly")
        self.entry_resultado.pack(padx=10, fill="x")

        # Botón para calcular
        ttk.Button(root, text="Calcular CRC", command=self.calcular_crc).pack(pady=10)
    
    def validar_polinomio(self, value):
        # Verifica si el polinomio tiene solo 0s y 1s
        if not all(char in "01" for char in value):
            return False
        
        # Limita la longitud si CRC-16 está seleccionado
        if self.tipo_crc.get() == "CRC-16":
            return len(value) <= 17  # Polinomio de 17 bits para CRC-16
        # Limita la longitud si CRC-32 está seleccionado
        if self.tipo_crc.get() == "CRC-32":
            return len(value) <= 33  # Polinomio de 33 bits para CRC-16
        
    def limpiar_polinomio(self):
        """ Borra el polinomio generador cuando se cambia el tipo de CRC. """
        self.entry_polinomio.delete(0, tk.END)
        return True  # Para otros casos, sin restricción de longitud
    
    def validar_binario(self, value):
        """ Valida que solo se ingresen 0 y 1 en el campo binario. """
        return all(char in "01" for char in value) or value == ""

    def desactivar_otro(self, event):
        """ Permite escribir solo en uno de los dos campos (binario o texto). """
        if event.widget == self.entry_binario and self.entry_binario.get():
            self.entry_texto.config(state="disabled")
        elif event.widget == self.entry_texto and self.entry_texto.get():
            self.entry_binario.config(state="disabled")
        else:
            self.entry_binario.config(state="normal")
            self.entry_texto.config(state="normal")

    def calcular_crc(self):
        """ Función placeholder para el cálculo de CRC (por ahora no implementado). """
        self.resultado.set("Cálculo pendiente...")

if __name__ == "__main__":
    root = tk.Tk()
    app = CRC_GUI(root)
    root.mainloop()

