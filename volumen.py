from tkinter import *
from tkinter import ttk

i = 0

def vent_volumen():
    menu = Tk()
    menu.title("Volumen")
    menu.geometry("355x410")

    def click_boton(valor):
        global i
        e_texto.insert(i, valor)
        i += 1
       
    def borrar():
        e_texto.delete(0, END)
        e_texto2.delete(0, END)
        
    def operar():
        opc1 = lista_desplegable.get()
        opc2 = lista_desplegable2.get()
        
        if opc1 == "m³" and opc2 == "Cm³":
            x = float(e_texto.get())
            resul = x*1000000
            e_texto2.delete(0, END)
            e_texto2.insert(0,string=str(resul))
            
        elif opc1 == "m³" and opc2 == "Litros":
            x = float(e_texto.get())
            resul = x*1000
            e_texto2.delete(0, END)
            e_texto2.insert(0,string=str(resul))
        
        elif opc1 == "m³" and opc2 == "Mililitros":
            x = float(e_texto.get())
            resul = x*1000000
            e_texto2.delete(0, END)
            e_texto2.insert(0,string=str(resul))
        
        elif opc1 == "Cm³" and opc2 == "m³":
            x = float(e_texto.get())
            resul = x*(1/1000000)
            e_texto2.delete(0, END)
            e_texto2.insert(0,string=str(resul))
            
        elif opc1 == "Cm³" and opc2 == "Litros":
            x = float(e_texto.get())
            resul = x*(1/1000)
            e_texto2.delete(0, END)
            e_texto2.insert(0,string=str(resul))
            
        elif opc1 == "Cm³" and opc2 == "Mililitros":
            x = float(e_texto.get())
            resul = x*1
            e_texto2.delete(0, END)
            e_texto2.insert(0,string=str(resul))
            
        elif opc1 == "Litros" and opc2 == "m³":
            x = float(e_texto.get())
            resul = x*(1/1000)
            e_texto2.delete(0, END)
            e_texto2.insert(0,string=str(resul))
            
        elif opc1 == "Litros" and opc2 == "Cm³":
            x = float(e_texto.get())
            resul = x*1000
            e_texto2.delete(0, END)
            e_texto2.insert(0,string=str(resul))
            
        elif opc1 == "Litros" and opc2 == "Mililitros":
            x = float(e_texto.get())
            resul = x*1000
            e_texto2.delete(0, END)
            e_texto2.insert(0,string=str(resul))
            
        elif opc1 == "Mililitros" and opc2 == "m³":
            x = float(e_texto.get())
            resul = x*(1/1000000)
            e_texto2.delete(0, END)
            e_texto2.insert(0,string=str(resul))
            
        elif opc1 == "Mililitros" and opc2 == "Cm³":
            x = float(e_texto.get())
            resul = x*1
            e_texto2.delete(0, END)
            e_texto2.insert(0,string=str(resul))
            
        elif opc1 == "Mililitros" and opc2 == "Litros":
            x = float(e_texto.get())
            resul = x*(1/1000)
            e_texto2.delete(0, END)
            e_texto2.insert(0,string=str(resul))
        
        
        

# Frame
    frame1 = Frame(menu)
    frame1.config(bg="lightsteelblue3", width = 355, height = 146)
    frame1.place(x=0, y=0)

    frame2 = Frame(menu)
    frame2.config(bg="snow", width = 335, height = 125)
    frame2.place(x=11, y=11)

    # Listas desplegables
    lista_desplegable = ttk.Combobox(menu, width = 12)
    lista_desplegable.place (x = 20, y = 20 )

    #lista de opciones
    opciones = ["m³","Cm³","Litros","Mililitros"]
    lista_desplegable['values'] = opciones

    lista_desplegable2 = ttk.Combobox(menu, width = 12)
    lista_desplegable2.place (x = 20, y = 75 )


    #lista de opciones
    opciones = ["m³","Cm³","Litros","Mililitros"]
    lista_desplegable2['values'] = opciones

    #Entradas 
    e_texto = Entry(menu, font = ("Rubik 20"),justify= 'right', width = 8)
    e_texto.place(x=198, y=14)

    e_texto2 = Entry(menu, font = ("Rubik 20"),justify= 'right', width = 8)
    e_texto2.place(x=198, y=75)


    #Agregar botones en pantalla de longitud 
    # fila 1
    boton7 = Button(menu, text = "7", width = 9, height = 3,command= lambda: click_boton(7))
    boton7.place(x=15, y=151)

    boton8 = Button(menu, text = "8", width = 9, height = 3,command= lambda: click_boton(8))
    boton8.place(x=102, y=151)

    boton9 = Button(menu, text = "9", width = 9, height = 3,command= lambda: click_boton(9))
    boton9.place(x=187, y=151)

    boton_borrar = Button(menu, text = "Borrar", width = 8, height = 7,bg="sky blue",command= lambda: borrar())
    boton_borrar.place(x=272, y=151) 

    # fila 2
    boton4 = Button(menu, text = "4", width = 9, height = 3,command= lambda: click_boton(4))
    boton4.place(x=15, y=217)

    boton5 = Button(menu, text = "5", width = 9, height = 3,command= lambda: click_boton(5))
    boton5.place(x=102, y=217)

    boton6 = Button(menu, text = "6", width = 9, height = 3,command= lambda: click_boton(6))
    boton6.place(x=187, y=217)

    # fila 3
    boton1 = Button(menu, text = "1", width = 9, height = 3,command= lambda: click_boton(1))
    boton1.place(x=15, y=281)

    boton2 = Button(menu, text = "2", width = 9, height = 3,command= lambda: click_boton(2))
    boton2.place(x=102, y=281)

    boton3 = Button(menu, text = "3", width = 9, height = 3,command= lambda: click_boton(3))
    boton3.place(x=187, y=281)

    boton_borrar = Button(menu, text = "Ejecutar", width = 8, height = 7,bg="sky blue", command=operar)
    boton_borrar.place(x=272, y=281) 

    # fila 4

    boton0 = Button(menu, text = "0", width = 9, height = 3,command= lambda: click_boton(0))
    boton0.place(x=102, y=345)

    boton_punto = Button(menu, text = ".", width = 9, height = 3,command= lambda: click_boton("."))
    boton_punto.place(x=187,y=345)