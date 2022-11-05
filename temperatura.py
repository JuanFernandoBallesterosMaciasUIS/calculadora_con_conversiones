from tkinter import *

def vent_temperatura():
    menu = Tk()
    menu.title("Temperatura")
    menu.geometry("355x410")
    
    # Frame
    frame1 = Frame(menu)
    frame1.config(bg="lightsteelblue3", width = 355, height = 146)
    frame1.place(x=0, y=0)
    
    frame2 = Frame(menu)
    frame2.config(bg="snow", width = 335, height = 125)
    frame2.place(x=11, y=11)
    
    
    #Agregar botones en pantalla de longitud 
    # fila 1
    boton7 = Button(menu, text = "7", width = 9, height = 3,)
    boton7.place(x=15, y=151)
    
    boton8 = Button(menu, text = "8", width = 9, height = 3,)
    boton8.place(x=102, y=151)
    
    boton9 = Button(menu, text = "9", width = 9, height = 3,)
    boton9.place(x=187, y=151)
    
    boton_borrar = Button(menu, text = "AC", width = 8, height = 7,bg="sky blue")
    boton_borrar.place(x=272, y=151) 
    
    # fila 2
    boton4 = Button(menu, text = "4", width = 9, height = 3,)
    boton4.place(x=15, y=217)
    
    boton5 = Button(menu, text = "5", width = 9, height = 3,)
    boton5.place(x=102, y=217)
    
    boton6 = Button(menu, text = "6", width = 9, height = 3,)
    boton6.place(x=187, y=217)
    
    # fila 3
    boton1 = Button(menu, text = "1", width = 9, height = 3,)
    boton1.place(x=15, y=281)
    
    boton2 = Button(menu, text = "2", width = 9, height = 3,)
    boton2.place(x=102, y=281)
    
    boton3 = Button(menu, text = "3", width = 9, height = 3,)
    boton3.place(x=187, y=281)
    
    boton4 = Button(menu, text = "X", width = 8, height = 7,bg="sky blue")
    boton4.place(x=272, y=281) 
    
    # fila 4
    
    boton0 = Button(menu, text = "0", width = 9, height = 3,)
    boton0.place(x=102, y=345)
    
    boton1 = Button(menu, text = ".", width = 9, height = 3,)
    boton1.place(x=187, y=345)