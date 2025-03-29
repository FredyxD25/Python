import time
import json
from tkinter import *

with open(r"D:\Programacion GIT\Python\Ingenieria\Multiplataforma\29_03_2024\posiciones.json", 'r') as file:

    position_dict = json.load(file)

def mover():
    global x
    canvas.delete("all")
    
    if x < len(position_dict):
        pos = list(position_dict.values())[x]
        canvas.create_oval(pos[0], pos[1], pos[0] + 20 , pos[1] + 20 , width=2, fill="black")
        x += 1
    
    Aplicacion.after(300, mover)

if __name__ == "__main__":
    Aplicacion = Tk()
    canvas = Canvas(Aplicacion, width=400, height=300, bg="white")
    canvas.pack(expand=YES, fill=BOTH)

    
    x = 0
    
  
    mover()
    
    Aplicacion.mainloop()