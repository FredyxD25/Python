from tkinter import*

ventanaServo=Tk()

ventanaServo.title("Servo Motor") 
ventanaServo.geometry("160x140")

anguloSer=0
numeroPantalla=StringVar()
numeroBorrar=StringVar()

cuadroTemp=Frame(ventanaServo,width=640,height=480) 
pantalla=Entry(cuadroTemp,width=22)
    
pantalla.place(x=10,y=10)

cuadroTemp.pack()

def numeroPulsado(num):
    numeroPantalla.set(numeroPantalla.get()+num)
    pantalla=Entry(cuadroTemp,textvariable=numeroPantalla,width=22)

    pantalla.place(x=10,y=10)

    cuadroTemp.pack()

def borrar():
    numeroBorrar.set("                 ")
    numeroPantalla.set("")
    pantalla=Entry(cuadroTemp,textvariable=numeroBorrar,width=22)

    pantalla.place(x=10,y=10)

    cuadroTemp.pack()    
def servo(num):
    ventanaServo.destroy()

#-----------------Botones--------------------------
numero1=Button(ventanaServo,text="1",command=lambda:numeroPulsado("1"),width=5)
numero1.place(x=10,y=35)

numero2=Button(ventanaServo,text="2",command=lambda:numeroPulsado("2"),width=5)
numero2.place(x=55,y=35)

numero3=Button(ventanaServo,text="3",command=lambda:numeroPulsado("3"),width=5)
numero3.place(x=100,y=35)
    
#-------------------------------------------------------
numero4=Button(ventanaServo,text="4",command=lambda:numeroPulsado("4"),width=5)
numero4.place(x=10,y=60)

numero5=Button(ventanaServo,text="5",command=lambda:numeroPulsado("5"),width=5)
numero5.place(x=55,y=60)

numero6=Button(ventanaServo,text="6",command=lambda:numeroPulsado("6"),width=5)
numero6.place(x=100,y=60)    
#-------------------------------------------------------
numero7=Button(ventanaServo,text="7",command=lambda:numeroPulsado("7"),width=5)
numero7.place(x=10,y=85)

numero8=Button(ventanaServo,text="8",command=lambda:numeroPulsado("8"),width=5)
numero8.place(x=55,y=85)

numero9=Button(ventanaServo,text="9",command=lambda:numeroPulsado("9"),width=5)
numero9.place(x=100,y=85)    
 #-------------------------------------------------------
numero4=Button(ventanaServo,text="<--",command=borrar,width=5)
numero4.place(x=10,y=110)

numero5=Button(ventanaServo,text="0",command=lambda:numeroPulsado("0"),width=5)
numero5.place(x=55,y=110)

numero6=Button(ventanaServo,text="=",command=lambda:servo(numeroPantalla),width=5)
numero6.place(x=100,y=110)

ventanaServo.mainloop()    

