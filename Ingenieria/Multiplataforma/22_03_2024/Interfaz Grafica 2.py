from tkinter import *
from tkinter import Tk
from tkinter import ttk
import sys

def seleccion(event):
    seleccion = combo.get()
    T_salida.set(str(seleccion))
    print(spin.get())

if __name__ == "__main__":
    Aplicacion = Tk()
    Aplicacion.geometry("500x600")
    Aplicacion.title("Características")
    etiqueta = Label(Aplicacion, text="Lista", bg='red', fg='blue')
    combo = ttk.Combobox(Aplicacion, state="reandonly",values=["Op1","Op2","Op3","Op4"])
    combo.set("Op3")
    combo.bind("<<ComboboxSelected>>", seleccion)
    spin = ttk.Spinbox(Aplicacion, from_=0, to = 10, increment = 1)
    T_salida=StringVar(Aplicacion)
    Entrada = Entry(Aplicacion,textvariable=T_salida)

    spin.pack()
    etiqueta.pack()
    combo.pack()
    Entrada.pack()

    Aplicacion.mainloop()