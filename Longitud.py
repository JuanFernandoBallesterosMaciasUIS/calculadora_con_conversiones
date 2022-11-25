from tkinter import *
from tkinter import ttk


i = 0

def vent_longitud():
    menu = Tk()
    menu.title("Longitud")
    menu.geometry("355x410")

    def click_boton(valor):
        global i
        e_texto.insert(i, valor)
        i += 1
       
    def borrar():
        e_texto.delete(0, END)
        e_texto2.delete(0, END)
        
    # Se agrega la lista para conversion de unidades    

    def operar():
        opc1 = lista_desplegable.get()
        opc2 = lista_desplegable2.get()

  # Metro

        if opc1 == "Metro" and opc2 == "Centímetro":
            x = float(e_texto.get())
            resul = x*100
            e_texto2.delete(0, END)
            e_texto2.insert(0,string=str(resul)) 
        
        elif opc1 == "Metro" and opc2 == "Milímetro":
            x = float(e_texto.get())
            resul = x*1000
            e_texto2.delete(0, END)
            e_texto2.insert(0,string=str(resul))
        
        elif opc1 == "Metro" and opc2 == "Kilómetro":
            x = float(e_texto.get())
            resul = x*0.001
            e_texto2.delete(0, END)
            e_texto2.insert(0,string=str(resul)) 

        elif opc1 == "Metro" and opc2 == "Hectómetro":
            x = float(e_texto.get())
            resul = x*0.01
            e_texto2.delete(0, END)
            e_texto2.insert(0,string=str(resul))


# Centímetro 

        elif opc1 == "Centímetro" and opc2 == "Metro":
            x = float(e_texto.get())
            resul = x*0.01
            e_texto2.delete(0, END)
            e_texto2.insert(0,string=str(resul))

        elif opc1 == "Centímetro" and opc2 == "Milímetro":
            x = float(e_texto.get())
            resul = x*10
            e_texto2.delete(0, END)
            e_texto2.insert(0,string=str(resul))

        elif opc1 == "Centímetro" and opc2 == "Kilómetro":
            x = float(e_texto.get())
            resul = x*0.00001
            e_texto2.delete(0, END)
            e_texto2.insert(0,string=str(resul))

        elif opc1 == "Centímetro" and opc2 == "Hectómetro":
            x = float(e_texto.get())
            resul = x*0.0001
            e_texto2.delete(0, END)
            e_texto2.insert(0,string=str(resul))

#Milímetro
        elif opc1 == "Milímetro" and opc2 == "Metro":
            x = float(e_texto.get())
            resul = x*0.001
            e_texto2.delete(0, END)
            e_texto2.insert(0,string=str(resul))
        
        elif opc1 == "Milímetro" and opc2 == "Centímetro":
            x = float(e_texto.get())
            resul = x*0.1
            e_texto2.delete(0, END)
            e_texto2.insert(0,string=str(resul))

        elif opc1 == "Milímetro" and opc2 == "Kilómetro":
            x = float(e_texto.get())
            resul = x*0.000001
            e_texto2.delete(0, END)
            e_texto2.insert(0,string=str(resul))

        elif opc1 == "Milímetro" and opc2 == "Hectómetro":
            x = float(e_texto.get())
            resul = x*0.00001
            e_texto2.delete(0, END)
            e_texto2.insert(0,string=str(resul))

# Kilómetro  

        elif opc1 == "Kilómetro" and opc2 == "Metro":
            x = float(e_texto.get())
            resul = x*1000
            e_texto2.delete(0, END)
            e_texto2.insert(0,string=str(resul))

        elif opc1 == "Kilómetro" and opc2 == "Centímetro":
            x = float(e_texto.get())
            resul = x*100000
            e_texto2.delete(0, END)
            e_texto2.insert(0,string=str(resul))

        elif opc1 == "Kilómetro" and opc2 == "Milímetro":
            x = float(e_texto.get())
            resul = x*1000000
            e_texto2.delete(0, END)
            e_texto2.insert(0,string=str(resul))

        elif opc1 == "Kilómetro" and opc2 == "Hectómetro":
            x = float(e_texto.get())
            resul = x*10
            e_texto2.delete(0, END)
            e_texto2.insert(0,string=str(resul))

# Hectómetro
        
        elif opc1 == "Hectómetro" and opc2 == "Metro":
            x = float(e_texto.get())
            resul = x*100
            e_texto2.delete(0, END)
            e_texto2.insert(0,string=str(resul))

        elif opc1 == "Hectómetro" and opc2 == "Centímetro":
            x = float(e_texto.get())
            resul = x*10000
            e_texto2.delete(0, END)
            e_texto2.insert(0,string=str(resul))

        elif opc1 == "Hectómetro" and opc2 == "Milímetro":
            x = float(e_texto.get())
            resul = x*1e+6
            e_texto2.delete(0, END)
            e_texto2.insert(0,string=str(resul))
        
        elif opc1 == "Hectómetro" and opc2 == "Kilómetro":
            x = float(e_texto.get())
            resul = x*0.1
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
    opciones = ["Metro","Centímetro", "Milímetro", "Kilómetro", "Hectómetro"]
    lista_desplegable['values'] = opciones

    lista_desplegable2 = ttk.Combobox(menu, width = 12, )
    lista_desplegable2.place (x = 20, y = 75 )


    #lista de opciones
    opciones =  ["Metro","Centímetro", "Milímetro", "Kilómetro", "Hectómetro"]
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
# color de la funete, tipo de letra )
    boton_borrar = Button(menu, text = "Borrar",bg="sky blue",  width = 8, height = 7, command= lambda: borrar())
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
    
    boton4 = Button(menu, text = "Ejecutar",bg="sky blue", width = 8, height = 7,command=operar )
    boton4.place(x=272, y=281) 

# fila 4
    boton0 = Button(menu, text = "0", width = 9, height = 3,command= lambda: click_boton(0))
    boton0.place(x=102, y=345)

    boton1 = Button(menu, text = ".", width = 9, height = 3,command= lambda: click_boton("."))
    boton1.place(x=187, y=345)
    
#menu.mainloop()