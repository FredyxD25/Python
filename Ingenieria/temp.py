import tkinter as tk
from tkinter import ttk

class CRC_GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora CRC")
        self.root.geometry("400x350")
        self.root.resizable(False, False)

        # ... (el resto de la interfaz sigue igual)

        # Resultado (campo de texto grande)
        ttk.Label(root, text="Resultado:").pack(anchor="w", padx=10, pady=5)

        # Crear un widget Text más grande para mostrar el resultado
        self.entry_resultado = tk.Text(root, height=6, width=60, font=("Arial", 12), wrap=tk.WORD, state="disabled")
        self.entry_resultado.pack(padx=30, pady=10, fill="x")

        # Botón para calcular
        ttk.Button(root, text="Calcular CRC", command=self.calcular_crc).pack(pady=10)
    
    def calcular_crc(self):
        # Aquí va tu lógica para calcular el CRC
        resultado_crc = "Resultado del CRC"  # Ejemplo de resultado
        self.mostrar_resultado(resultado_crc)

    def mostrar_resultado(self, resultado):
        # Muestra el resultado en el widget Text
        self.entry_resultado.config(state="normal")  # Cambia el estado a 'normal' para poder editarlo
        self.entry_resultado.delete(1.0, tk.END)  # Elimina el texto anterior
        self.entry_resultado.insert(tk.END, resultado)  # Inserta el nuevo resultado
        self.entry_resultado.config(state="disabled")  # Vuelve a poner el estado a 'disabled' (solo lectura)

# Crear la ventana principal y ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = CRC_GUI(root)
    root.mainloop()
