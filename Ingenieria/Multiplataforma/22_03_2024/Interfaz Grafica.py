from tkinter import *
from tkinter import Tk
from tkinter import ttk
import sys
def click():
    try:
        numero=int(C_Entrada.get())
        T_Etiqueta = "Elnumero es: "+ str(numero)
        etiqueta.config(text=T_Etiqueta)
    except:
        T_Etiqueta="Introduzca un dato"
        etiqueta.config(text=T_Etiqueta)

if __name__ == "__main__":
    Aplicacion = Tk()
    Aplicacion.geometry("500x600")
    Aplicacion.title("Edición")
    T_Etiqueta = "Digite algo..."
    etiqueta = Label(Aplicacion, text=T_Etiqueta, bg='red', fg='blue')
    boton = Button(Aplicacion, text="OK", command = click, width=20, height=10, anchor= "ne")
    T_salida="."
    C_Entrada = Entry(Aplicacion,textvariable=T_salida)

    '''etiqueta.pack()
    boton.pack()
    C_Entrada.pack()'''
    
    etiqueta.place(x=70, y=140, width=100, height=30)
    boton.place(x=60, y=40, width=100, height=30)

    Aplicacion.mainloop()