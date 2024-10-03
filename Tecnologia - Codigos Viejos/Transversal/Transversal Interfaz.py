from tkinter import*
from tkinter import ttk
import matplotlib.pyplot as plt
import matplotlib.animation as animation


from serial import*

serialPort='COM3'
baudRate=9600
seri=Serial(serialPort,baudRate)

VentanaMenu=Tk()
VentanaMenu.resizable(1,1)
VentanaMenu.geometry("850x550")
VentanaMenu.title("Menu")
VentanaMenu.config(bg="Black")
milabel=Label(VentanaMenu, text="BIENVENIDO AL PROCESO")
milabel.place(x=300, y=50)
milabel.config(font=15, bg="Black",fg='Red')
milabel=Label(VentanaMenu, text="DE DESINFECCION UV")
milabel.place(x=310, y=70)
milabel.config(font=15, bg="Black",fg='Red')
milabel=Label(VentanaMenu, text="Elija una opción")
milabel.place(x=350, y=170)
milabel.config(font=15, bg="Black",fg='White')
#imagenL=PhotoImage(file="1.png")
#lblImagen=Label(VentanaMenu,image=imagenL).place(x=100,y=100)

numeroEntrada=""
numeroEntrada1=""
numeroSer=0
Grado=0
b=0
c=0
mi=0
se=0



#------ BASE DE DATOS
def base():
    
    Ventanabase=Toplevel()
    Ventanabase.geometry("850x600")
    Ventanabase.title("BASE DE DATOS")
    Ventanabase.config(bg="Black")
    labelgrado3=Label(Ventanabase)
    labelgrado3.config(text="Sus últimos registros son:")
    labelgrado3.place(x=300, y=20)
    labelgrado3.config(font=10,bg="Black",fg='White')

    botonSalir=Button(Ventanabase, text="Salir", bg="Red", command=lambda:Ventanabase.destroy())
    botonSalir.pack()
    botonSalir.place(x=750,y=450)

    
    cuadro=Frame(Ventanabase)
    cuadro.pack()
    cuadro.config(bg="Red",width="120",height="25",bd="10")
    cuadro.place(x=280,y=100)
    cuadro=Frame(Ventanabase)
    cuadro.pack()
    cuadro.config(bg="White",width="120",height="25",bd="10")
    cuadro.place(x=280,y=130)
    cuadro=Frame(Ventanabase)
    cuadro.pack()
    cuadro.config(bg="White",width="120",height="25",bd="10")
    cuadro.place(x=280,y=160)
    cuadro=Frame(Ventanabase)
    cuadro.pack()
    cuadro.config(bg="White",width="120",height="25",bd="10")
    cuadro.place(x=280,y=190)
    cuadro=Frame(Ventanabase)
    cuadro.pack()
    cuadro.config(bg="White",width="120",height="25",bd="10")
    cuadro.place(x=280,y=220)
    cuadro=Frame(Ventanabase)
    cuadro.pack()
    cuadro.config(bg="White",width="120",height="25",bd="10")
    cuadro.place(x=280,y=250)
    cuadro=Frame(Ventanabase)
    cuadro.pack()
    cuadro.config(bg="White",width="120",height="25",bd="10")
    cuadro.place(x=280,y=280)
    cuadro=Frame(Ventanabase)
    cuadro.pack()
    cuadro.config(bg="White",width="120",height="25",bd="10")
    cuadro.place(x=280,y=310)
    cuadro=Frame(Ventanabase)
    cuadro.pack()
    cuadro.config(bg="White",width="120",height="25",bd="10")
    cuadro.place(x=280,y=340)
    cuadro=Frame(Ventanabase)
    cuadro.pack()
    cuadro.config(bg="White",width="120",height="25",bd="10")
    cuadro.place(x=280,y=370)
    cuadro=Frame(Ventanabase)
    cuadro.pack()
    cuadro.config(bg="White",width="120",height="25",bd="10")
    cuadro.place(x=280,y=400)


    cuadro=Frame(Ventanabase)
    cuadro.pack()
    cuadro.config(bg="Red",width="120",height="25",bd="10")
    cuadro.place(x=425,y=100)
    cuadro=Frame(Ventanabase)
    cuadro.pack()
    cuadro.config(bg="White",width="120",height="25",bd="10")
    cuadro.place(x=425,y=130)
    cuadro=Frame(Ventanabase)
    cuadro.pack()
    cuadro.config(bg="White",width="120",height="25",bd="10")
    cuadro.place(x=425,y=160)
    cuadro=Frame(Ventanabase)
    cuadro.pack()
    cuadro.config(bg="White",width="120",height="25",bd="10")
    cuadro.place(x=425,y=190)
    cuadro=Frame(Ventanabase)
    cuadro.pack()
    cuadro.config(bg="White",width="120",height="25",bd="10")
    cuadro.place(x=425,y=220)
    cuadro=Frame(Ventanabase)
    cuadro.pack()
    cuadro.config(bg="White",width="120",height="25",bd="10")
    cuadro.place(x=425,y=250)
    cuadro=Frame(Ventanabase)
    cuadro.pack()
    cuadro.config(bg="White",width="120",height="25",bd="10")
    cuadro.place(x=425,y=280)
    cuadro=Frame(Ventanabase)
    cuadro.pack()
    cuadro.config(bg="White",width="120",height="25",bd="10")
    cuadro.place(x=425,y=310)
    cuadro=Frame(Ventanabase)
    cuadro.pack()
    cuadro.config(bg="White",width="120",height="25",bd="10")
    cuadro.place(x=425,y=340)
    cuadro=Frame(Ventanabase)
    cuadro.pack()
    cuadro.config(bg="White",width="120",height="25",bd="10")
    cuadro.place(x=425,y=370)
    cuadro=Frame(Ventanabase)
    cuadro.pack()
    cuadro.config(bg="White",width="120",height="25",bd="10")
    cuadro.place(x=425,y=400)


    labelgrado3=Label(Ventanabase)
    labelgrado3.config(text="DATO")
    labelgrado3.place(x=310, y=100)
    labelgrado3.config(font=10,bg="Red",fg='White')

     
    labelgrado3=Label(Ventanabase)
    labelgrado3.config(text="1")
    labelgrado3.place(x=330, y=130)
    labelgrado3.config(font=10,bg="White",fg='Black')

     
    labelgrado3=Label(Ventanabase)
    labelgrado3.config(text="2")
    labelgrado3.place(x=330, y=160)
    labelgrado3.config(font=10,bg="White",fg='Black')

     
    labelgrado3=Label(Ventanabase)
    labelgrado3.config(text="3")
    labelgrado3.place(x=330, y=190)
    labelgrado3.config(font=10,bg="White",fg='Black')

     
    labelgrado3=Label(Ventanabase)
    labelgrado3.config(text="4")
    labelgrado3.place(x=330, y=220)
    labelgrado3.config(font=10,bg="White",fg='Black')

     
    labelgrado3=Label(Ventanabase)
    labelgrado3.config(text="5")
    labelgrado3.place(x=330, y=250)
    labelgrado3.config(font=10,bg="White",fg='Black')

     
    labelgrado3=Label(Ventanabase)
    labelgrado3.config(text="6")
    labelgrado3.place(x=330, y=280)
    labelgrado3.config(font=10,bg="White",fg='Black')

     
    labelgrado3=Label(Ventanabase)
    labelgrado3.config(text="7")
    labelgrado3.place(x=330, y=310)
    labelgrado3.config(font=10,bg="White",fg='Black')

     
    labelgrado3=Label(Ventanabase)
    labelgrado3.config(text="8")
    labelgrado3.place(x=330, y=340)
    labelgrado3.config(font=10,bg="White",fg='Black')

     
    labelgrado3=Label(Ventanabase)
    labelgrado3.config(text="9")
    labelgrado3.place(x=330, y=370)
    labelgrado3.config(font=10,bg="White",fg='Black')

     
    labelgrado3=Label(Ventanabase)
    labelgrado3.config(text="10")
    labelgrado3.place(x=330, y=400)
    labelgrado3.config(font=10,bg="White",fg='Black')

     
    labelgrado3=Label(Ventanabase)
    labelgrado3.config(text="TIEMPO")
    labelgrado3.place(x=430, y=100)
    labelgrado3.config(font=10,bg="Red",fg='White')

    labelgrado3=Label(Ventanabase)
    labelgrado3.config(text="1")
    labelgrado3.place(x=460, y=130)
    labelgrado3.config(font=10,bg="White",fg='Black')

     
    labelgrado3=Label(Ventanabase)
    labelgrado3.config(text="2")
    labelgrado3.place(x=460, y=160)
    labelgrado3.config(font=10,bg="White",fg='Black')

     
    labelgrado3=Label(Ventanabase)
    labelgrado3.config(text="3")
    labelgrado3.place(x=460, y=190)
    labelgrado3.config(font=10,bg="White",fg='Black')

     
    labelgrado3=Label(Ventanabase)
    labelgrado3.config(text="4")
    labelgrado3.place(x=460, y=220)
    labelgrado3.config(font=10,bg="White",fg='Black')

     
    labelgrado3=Label(Ventanabase)
    labelgrado3.config(text="5")
    labelgrado3.place(x=460, y=250)
    labelgrado3.config(font=10,bg="White",fg='Black')

     
    labelgrado3=Label(Ventanabase)
    labelgrado3.config(text="6")
    labelgrado3.place(x=460, y=280)
    labelgrado3.config(font=10,bg="White",fg='Black')

     
    labelgrado3=Label(Ventanabase)
    labelgrado3.config(text="7")
    labelgrado3.place(x=460, y=310)
    labelgrado3.config(font=10,bg="White",fg='Black')

    
    labelgrado3=Label(Ventanabase)
    labelgrado3.config(text="8")
    labelgrado3.place(x=460, y=340)
    labelgrado3.config(font=10,bg="White",fg='Black')

     
    labelgrado3=Label(Ventanabase)
    labelgrado3.config(text="9")
    labelgrado3.place(x=460, y=370)
    labelgrado3.config(font=10,bg="White",fg='Black')

     
    labelgrado3=Label(Ventanabase)
    labelgrado3.config(text="10")
    labelgrado3.place(x=460, y=400)
    labelgrado3.config(font=10,bg="White",fg='Black')

    i=0
    vector=[]   
    while True:
      while True:
          vector.insert(i,seri.readline().decode('utf-8'))
          print(vector)
          if(vector[i][1]=='\r'):
            print(vector[i][0])#Tiempo Insertado un numero
            if(i==0):
              tabla.insert("",END,text="1",values=str(values=vector[i][0]))
            elif(i==1):
              tabla.insert("",END,text="2",values=str(vector[i][1]))
            elif(i==2):
              tabla.insert("",END,text="3",values=str(vector[i][2]))
            elif(i==3):
              tabla.insert("",END,text="4",values=str(vector[i][3]))
            elif(i==4):
              tabla.insert("",END,text="5",values=str(vector[i][4]))
            elif(i==5):
              tabla.insert("",END,text="6",values=str(vector[i][5]))
            elif(i==6):
              tabla.insert("",END,text="7",values=str(vector[i][6]))
            elif(i==7):
              tabla.insert("",END,text="8",values=str(vector[i][7]))
            elif(i==8):
              tabla.insert("",END,text="9",values=str(vector[i][8]))
            elif(i==9):
              tabla.insert("",END,text="10",values=str(vector[i][9]))            
          else:
            print(vector[i][0]+vector[i][1])#Tiempo Insertado dos numeros 
            if(i==0):
              tabla.insert("",END,text="1",values=str(values=vector[i][0]))
            elif(i==1):
              tabla.insert("",END,text="2",values=str(vector[i][1]))
            elif(i==2):
              tabla.insert("",END,text="3",values=str(vector[i][2]))
            elif(i==3):
              tabla.insert("",END,text="4",values=str(vector[i][3]))
            elif(i==4):
              tabla.insert("",END,text="5",values=str(vector[i][4]))
            elif(i==5):
              tabla.insert("",END,text="6",values=str(vector[i][5]))
            elif(i==6):
              tabla.insert("",END,text="7",values=str(vector[i][6]))
            elif(i==7):
              tabla.insert("",END,text="8",values=str(vector[i][7]))
            elif(i==8):
              tabla.insert("",END,text="9",values=str(vector[i][8]))
            elif(i==9):
              tabla.insert("",END,text="10",values=str(vector[i][9])) 
          print(i+1)#Numero de ciclos
          
          i+=1
          if(i>=10):#10
              i=0
              vector.clear()
              break
         

def Vm():
    global b
    VentanaMotores=Toplevel()
     
    VentanaMotores.geometry("850x600")
    VentanaMotores.title("DESINFECCION")
    VentanaMotores.config(bg="Black")

    #------------------
    NumPantalla=StringVar()
    
    IngreseServo=Entry(VentanaMotores, textvariable=NumPantalla)
    IngreseServo.place(x=90,y=300)
    IngreseServo.config(background="black",fg="White",justify="right")

    def desin():

     
     Ventanadesin=Toplevel()
     Ventanadesin.geometry("850x600")
     Ventanadesin.title("PROCESO DESINFECCION")
     Ventanadesin.config(bg="Black")

     labelgrado3=Label(Ventanadesin)
     labelgrado3.config(text="Tiene               seg para salir del sitio")
     labelgrado3.place(x=300, y=520)
     labelgrado3.config(font=10,bg="Black",fg='White')

     
    
     tem=6
     for t in range (1,tem+1):
        labelgrado4=Label(Ventanadesin)
        labelgrado4.place(x=360, y=520)
        labelgrado4.config(font=10,bg="Black",fg='White',text=5)
        print(tem-t)
        #time.sleep(1)  

     labeldesin=Label(Ventanadesin)
     labeldesin.config(text="SU PROCESO DE DESINFECCION SE ESTA LLEVANDO A CABO")
     labeldesin.place(x=140, y=50)
     labeldesin.config(font=10,bg="Black",fg='RED')

     labeldesin=Label(Ventanadesin)
     labeldesin.config(text="Recuerde que si se detecta movimiento cerca del lugar, su proceso de desinfección se detendrá")
     labeldesin.place(x=90, y=110)
     labeldesin.config(font=10,bg="Black",fg='White')

     labeldesin=Label(Ventanadesin)
     labeldesin.config(text="DESINFECTANDO...")
     labeldesin.place(x=120, y=200)
     labeldesin.config(font=10,bg="Black",fg='White')
     labeldesin3=Label(Ventanadesin)
     labeldesin3.config(text="Quedan 20 minutos ")
     labeldesin3.place(x=120, y=240)

     labeldesin3.config(font=10,bg="Black",fg='White')
     labeldesin1=Label(Ventanadesin)
     labeldesin1.config(text="TEMPERATURA:")
     labeldesin1.place(x=500, y=200)
     labeldesin1.config(font=10,bg="Black",fg='White')
     labeldesin4=Label(Ventanadesin)
     labeldesin4.config(text="El dispositivo está a  30° ")
     labeldesin4.place(x=500, y=240)
     labeldesin4.config(font=10,bg="Black",fg='White')
 
    def NumPulsado(num):
      global b
      global numeroEntrada 
      numeroEntrada=(str(numeroEntrada+num))
      NumPantalla.set(NumPantalla.get()+num)


      b+=1
      if b==1:
        seri.write(numeroEntrada[0].encode('ascii'))
        print(numeroEntrada)
      elif b==2:
        seri.write(numeroEntrada[0].encode('ascii'))
        seri.write(numeroEntrada[1].encode('ascii'))
        print(numeroEntrada)
      elif b==3:
       # NumBorrar.set("")
        NumPantalla.set("")
        numeroEntrada=""
        b=0

    def Enter():
      global Grado
      global numeroEntrada 
      
      #NumBorrar.set("")
      Grado=int(numeroEntrada)
     # IngreseServo=Entry(VentanaMotores, textvariable=NumBorrar)
      print(Grado) 

      
      labelgrado=Label(VentanaMotores)
      labelgrado.config(text=Grado)
    
      labelgrado.place(x=130, y=400)
      labelgrado.config(font=10,bg="Black",fg='White')
      labelgrado2=Label(VentanaMotores)
      labelgrado2.config(text="Min")
      labelgrado2.place(x=150, y=400)
      labelgrado2.config(font=10,bg="Black",fg='White')

    def iniciar():


      labelgrado3=Label(VentanaMotores)
      labelgrado3.config(text="Tiene               seg para salir del sitio")
      labelgrado3.place(x=300, y=520)
      labelgrado3.config(font=10,bg="Black",fg='White')


    
      
  
  

#-----------------TECLADO SERVO
    milabel=Label(VentanaMotores, text=" LUZ UV")
    milabel.place(x=120, y=25)
    milabel.config(font=2,bg="Black",fg='White')
    milabel=Label(VentanaMotores, text=" Elija el tiempo de desinfección:")
    milabel.place(x=45, y=64)
    milabel.config(font=2,bg="Black",fg='White')

    boton1=Button(VentanaMotores, text="1",width=3,bg="Red",fg="White", command=lambda:NumPulsado("1"))
    boton1.pack()
    boton1.place(x=80,y=100)
    boton1.config(width="5", height="2",bd="1",)

    boton2=Button(VentanaMotores, text="2",width=3,bg="Red",fg="White", command=lambda:NumPulsado("2"))
    boton2.pack()
    boton2.place(x=130,y=100)
    boton2.config(width="5", height="2",bd="1")

    boton3=Button(VentanaMotores, text="3",width=3,bg="Red",fg="White", command=lambda:NumPulsado("3"))
    boton3.pack()
    boton3.place(x=180,y=100)
    boton3.config(width="5", height="2",bd="1")

    boton4=Button(VentanaMotores, text="4",width=3,bg="Red",fg="White", command=lambda:NumPulsado("4"))
    boton4.pack()
    boton4.place(x=80,y=145)
    boton4.config(width="5", height="2",bd="1")

    boton5=Button(VentanaMotores, text="5",width=3,bg="Red",fg="White",command=lambda:NumPulsado("5"))
    boton5.pack()
    boton5.place(x=130,y=145)
    boton5.config(width="5", height="2",bd="1")

    boton6=Button(VentanaMotores, text="6",width=3,bg="Red",fg="White", command=lambda:NumPulsado("6"))
    boton6.pack()
    boton6.place(x=180,y=145)
    boton6.config(width="5", height="2",bd="1")

    boton7=Button(VentanaMotores, text="7",width=3,bg="Red",fg="White", command=lambda:NumPulsado("7"))
    boton7.pack()
    boton7.place(x=80,y=190)
    boton7.config(width="5", height="2",bd="1")

    boton8=Button(VentanaMotores, text="8",width=3,bg="Red",fg="White", command=lambda:NumPulsado("8"))
    boton8.pack()
    boton8.place(x=130,y=190)
    boton8.config(width="5", height="2",bd="1")

    boton9=Button(VentanaMotores, text="9",width=3,bg="Red",fg="White", command=lambda:NumPulsado("9"))
    boton9.pack()
    boton9.place(x=180,y=190)
    boton9.config(width="5", height="2",bd="1")

    boton0=Button(VentanaMotores, text="0",width=3,bg="Red",fg="White", command=lambda:NumPulsado("0"))
    boton0.pack()
    boton0.place(x=130,y=235)
    boton0.config(width="5", height="2",bd="1")

    botonE=Button(VentanaMotores, text=">",width=3,bg="Red",fg="White",command=lambda:Enter())
    botonE.pack()
    botonE.place(x=180,y=235)
    botonE.config(width="5", height="2",bd="1")

    botonSalir=Button(VentanaMotores, text="Salir", bg="Red", command=lambda:VentanaMotores.destroy())
    botonSalir.pack()
    botonSalir.place(x=750,y=450)

    botonIniciar=Button(VentanaMotores, text="Iniciar", bg="Red", command=lambda:desin())
    botonIniciar.pack()
    botonIniciar.place(x=380,y=450)
    botonIniciar.config(width="10", height="2",bd="1")
#------ TECLADO PASO A PASO
    NumPantalla1=StringVar()
    IngresePaso=Entry(VentanaMotores,textvariable=NumPantalla1)
    IngresePaso.place(x=580,y=300)
    IngresePaso.config(background="black",fg="White",justify="right")

    def NumPulsado1(num1):
      global c
      global numeroEntrada1 
      
      NumPantalla1.set(NumPantalla1.get()+num1)
     
      numeroEntrada1=(str(numeroEntrada1+num1))
      c+=1
      if c==1:
        seri.write(numeroEntrada1[0].encode('ascii'))
        print(numeroEntrada1)
      elif c==2:
        seri.write(numeroEntrada1[0].encode('ascii'))
        seri.write(numeroEntrada1[1].encode('ascii'))
        print(numeroEntrada1)
      elif c==3:
       # NumBorrar.set("")
        NumPantalla1.set("")
        numeroEntrada1=""
        c=0

    def Enter1():
      global Grado1
      global numeroEntrada1 
      
      #NumBorrar.set("")
      Grado1=int(numeroEntrada1)
     # IngreseServo=Entry(VentanaMotores, textvariable=NumBorrar)
      print(Grado1)     
      
      labelgrado1=Label(VentanaMotores)
      labelgrado1.config(text=Grado1)
    
      labelgrado1.place(x=610, y=400)
      labelgrado1.config(font=10,bg="Black",fg='White')
      labelgrado22=Label(VentanaMotores)
      labelgrado22.config(text="°")
      labelgrado22.place(x=635, y=400)
      labelgrado22.config(font=10,bg="Black",fg='White')
      
      
      Grado1=0

    milabel=Label(VentanaMotores, text=" El tiempo de desinfección será de: ")
    milabel.config(font=2,bg="Black",fg='White')
    milabel.place(x=50, y=370)
    milabel=Label(VentanaMotores, text=" La temperatura máxima deseada es: ")
    milabel.config(font=2,bg="Black",fg='White')
    milabel.place(x=500, y=370)

    milabel=Label(VentanaMotores, text="  TEMPERATURA")
    milabel.place(x=570, y=25)
    milabel.config(font=2,bg="Black",fg='White')
    milabel=Label(VentanaMotores, text=" Elija la temperatura máxima:")
    milabel.place(x=530, y=66)
    milabel.config(font=2,bg="Black",fg='White')

    boton11=Button(VentanaMotores, text="1",width=3,bg="Red",fg="White", command=lambda:NumPulsado1("1"))
    boton11.pack()
    boton11.place(x=560,y=100)
    boton11.config(width="5", height="2",bd="1")

    boton22=Button(VentanaMotores, text="2",width=3,bg="Red",fg="White", command=lambda:NumPulsado1("2"))
    boton22.pack()
    boton22.place(x=610,y=100)
    boton22.config(width="5", height="2",bd="1")

    boton33=Button(VentanaMotores, text="3",width=3,bg="Red",fg="White", command=lambda:NumPulsado1("3"))
    boton33.pack()
    boton33.place(x=660,y=100)
    boton33.config(width="5", height="2",bd="1")

    boton44=Button(VentanaMotores, text="4",width=3,bg="Red",fg="White", command=lambda:NumPulsado1("4"))
    boton44.pack()
    boton44.place(x=560,y=145)
    boton44.config(width="5", height="2",bd="1")

    boton55=Button(VentanaMotores, text="5",width=3,bg="Red",fg="White", command=lambda:NumPulsado1("5"))
    boton55.pack()
    boton55.place(x=610,y=145)
    boton55.config(width="5", height="2",bd="1")

    boton66=Button(VentanaMotores, text="6",width=3,bg="Red",fg="White", command=lambda:NumPulsado1("6"))
    boton66.pack()
    boton66.place(x=660,y=145)
    boton66.config(width="5", height="2",bd="1")

    boton77=Button(VentanaMotores, text="7",width=3,bg="Red",fg="White", command=lambda:NumPulsado1("7"))
    boton77.pack()
    boton77.place(x=560,y=190)
    boton77.config(width="5", height="2",bd="1")

    boton88=Button(VentanaMotores, text="8",width=3,bg="Red",fg="White", command=lambda:NumPulsado1("8"))
    boton88.pack()
    boton88.place(x=610,y=190)
    boton88.config(width="5", height="2",bd="1")

    boton99=Button(VentanaMotores, text="9",width=3,bg="Red",fg="White", command=lambda:NumPulsado1("9"))
    boton99.pack()
    boton99.place(x=660,y=190)
    boton99.config(width="5", height="2",bd="1")

    boton00=Button(VentanaMotores, text="0",width=3,bg="Red",fg="White", command=lambda:NumPulsado1("0"))
    boton00.pack()
    boton00.place(x=610,y=235)
    boton00.config(width="5", height="2",bd="1")

    botonEE=Button(VentanaMotores, text=">",width=3,bg="Red",fg="White",command=lambda:Enter1())
    botonEE.pack()
    botonEE.place(x=660,y=235)
    botonEE.config(width="5", height="2",bd="1")
'''def Vt():
  figura1 =plt.figure()
  ax1 = figura1.add_subplot(1,1,1)
  xtiempo, ytemp= [], []
  ax1.set_title('Sensor de Temperatura')
  plt.label('Tiempo')
  plt.ylabel('Temperatura Lm35')  
  while True:
     if(seri.inWaiting()>0):
       def animar(i,xtiempo,ytemp ):
         datos = seri.readLine()
         datos = float(datos)
         xtiempo.append(i)
         ytemp.append(datos)

        #anim = animation.FuncAnimation(figura1, animar,fargs=(xtiempo,ytemp),interval=100 )
        #plt.show 
'''

    #VentanaSensor=Toplevel()

    #VentanaSensor.geometry("850x550")
    #VentanaSensor.title("Sensor Temperatura")
    #botonSalir1=Button(VentanaSensor, text="Salir", bg="orange", command=VentanaMenu)
    #botonSalir1.pack()
    #botonSalir1.place(x=750,y=400)


botonsensor=Button(VentanaMenu, text="BASE DE DATOS", bg="Red", fg='White',command=base) 
botonMotores=Button(VentanaMenu, text="DESINFECCION", bg="Red",fg='White', command=Vm)
botonMotores.config(width="30", height="6",bd="5")
botonsensor.config(width="30", height="6", bd="5")
botonsensor.pack()
botonsensor.place(x=100,y=300)
botonMotores.pack()  
botonMotores.place(x=500,y=300)
   
#b=ser.read()

#label2=Label(VentanaMenu)
#label2.config(text=b)
#label2.pack()

#------ VENTANA MOTORES
#------------- VENTANA TEMPERATURA


VentanaMenu.mainloop()