from tkinter import *
from tkinter import ttk
from tkinter import messagebox

i = 0

def vent_tiempo():
    menu2 = Tk()
    menu2.iconbitmap('icono/logo21.ico')
    
    menu2.title("Tiempo")
    #menu2.geometry("355x410")
    menu2.config(bg="#080808")
    menu2.resizable(0,0)

    #  Obtenemos el largo y  ancho de la pantalla
    wtotal = menu2.winfo_screenwidth()
    htotal = menu2.winfo_screenheight()
    #  Guardamos el largo y alto de la ventana
    wventana = 355
    hventana = 410

    #  Aplicamos la siguiente formula para calcular donde debería posicionarse
    pwidth = round(wtotal/2-wventana/2)
    pheight = round(htotal/2-hventana/2)

    #  Se lo aplicamos a la geometría de la ventana
    menu2.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight))
  
    def click_boton(valor):
        global i
        e_texto.insert(i, valor)
        i += 1
       
    def borrar():
        e_texto.delete(0, END)
        e_texto2.delete(0, END)
        
# Se agrega la lista para conversion de tiempo   

    def operar():
        opc1 = lista_desplegable.get()
        opc2 = lista_desplegable2.get()

  # Segundos 

        if opc1 == "Segundos" and opc2 == "Minutos":
            x = float(e_texto.get())
            resul = x/60
            e_texto2.delete(0, END)
            e_texto2.insert(0,string=str(resul)) 
        
        elif opc1 == "Segundos" and opc2 == "Horas":
            x = float(e_texto.get())
            resul = x/3600
            e_texto2.delete(0, END)
            e_texto2.insert(0,string=str(resul))
        
        elif opc1 == "Segundos" and opc2 == "Días":
            x = float(e_texto.get())
            resul = x/86400
            e_texto2.delete(0, END)
            e_texto2.insert(0,string=str(resul)) 

        elif opc1 == "Segundos" and opc2 == "Semanas":
            x = float(e_texto.get())
            resul = x/604800
            e_texto2.delete(0, END)
            e_texto2.insert(0,string=str(resul))

# Minutos  

        elif opc1 == "Minutos" and opc2 == "Segundos":
            x = float(e_texto.get())
            resul = x*60
            e_texto2.delete(0, END)
            e_texto2.insert(0,string=str(resul))

        elif opc1 == "Minutos" and opc2 == "Horas":
            x = float(e_texto.get())
            resul = x/60
            e_texto2.delete(0, END)
            e_texto2.insert(0,string=str(resul))

        elif opc1 == "Minutos" and opc2 == "Días":
            x = float(e_texto.get())
            resul = x/1440
            e_texto2.delete(0, END)
            e_texto2.insert(0,string=str(resul))

        elif opc1 == "Minutos" and opc2 == "Semanas":
            x = float(e_texto.get())
            resul = x/10080
            e_texto2.delete(0, END)
            e_texto2.insert(0,string=str(resul))

# Horas 

        elif opc1 == "Horas" and opc2 == "Segundos":
            x = float(e_texto.get())
            resul = x*3600
            e_texto2.delete(0, END)
            e_texto2.insert(0,string=str(resul))

        elif opc1 == "Horas" and opc2 == "Minutos":
            x = float(e_texto.get())
            resul = x*60
            e_texto2.delete(0, END)
            e_texto2.insert(0,string=str(resul))

        elif opc1 == "Horas" and opc2 == "Días":
            x = float(e_texto.get())
            resul = x/24
            e_texto2.delete(0, END)
            e_texto2.insert(0,string=str(resul))

        elif opc1 == "Horas" and opc2 == "Semanas":
            x = float(e_texto.get())
            resul = x/168
            e_texto2.delete(0, END)
            e_texto2.insert(0,string=str(resul))

# Días 

        elif opc1 == "Días" and opc2 == "Segundos":
            x = float(e_texto.get())
            resul = x*86400
            e_texto2.delete(0, END)
            e_texto2.insert(0,string=str(resul))

        elif opc1 == "Días" and opc2 == "Minutos":
            x = float(e_texto.get())
            resul = x*1440
            e_texto2.delete(0, END)
            e_texto2.insert(0,string=str(resul))

        elif opc1 == "Días" and opc2 == "Horas":
            x = float(e_texto.get())
            resul = x*24
            e_texto2.delete(0, END)
            e_texto2.insert(0,string=str(resul))

        elif opc1 == "Días" and opc2 == "Semanas":
            x = float(e_texto.get())
            resul = x/7
            e_texto2.delete(0, END)
            e_texto2.insert(0,string=str(resul))

# Semanas

        elif opc1 == "Semanas" and opc2 == "Segundos":
            x = float(e_texto.get())
            resul = x*604800
            e_texto2.delete(0, END)
            e_texto2.insert(0,string=str(resul))

        elif opc1 == "Semanas" and opc2 == "Minutos":
            x = float(e_texto.get())
            resul = x*10080
            e_texto2.delete(0, END)
            e_texto2.insert(0,string=str(resul))

        elif opc1 == "Semanas" and opc2 == "Horas":
            x = float(e_texto.get())
            resul = x*168
            e_texto2.delete(0, END)
            e_texto2.insert(0,string=str(resul))

        elif opc1 == "Semanas" and opc2 == "Días":
            x = float(e_texto.get())
            resul = x*7
            e_texto2.delete(0, END)
            e_texto2.insert(0,string=str(resul))
        else:
            messagebox.showinfo("Error", "Selecciona unidades diferentes")

# Frame
    frame1 = Frame(menu2)
    frame1.config(bg="lightsteelblue3", width = 355, height = 146)
    frame1.place(x=0, y=0)
    frame1.config(bg="#080808")
    

    frame2 = Frame(menu2)
    frame2.config(bg="lightsteelblue3", width = 335, height = 125)
    frame2.place(x=11, y=11)
    frame2.config(bg="#080808")
    

     # Listas desplegables
    lista_desplegable = ttk.Combobox(menu2, width = 12)
    lista_desplegable.place (x = 20, y = 20 )

    #lista de opciones
    opciones = ["Segundos","Minutos", "Horas", "Días", "Semanas"]
    lista_desplegable['values'] = opciones

    lista_desplegable2 = ttk.Combobox(menu2, width = 12, )
    lista_desplegable2.place (x = 20, y = 75 )


    #lista de opciones
    opciones =  ["Segundos","Minutos", "Horas", "Días", "Semanas"]
    lista_desplegable2['values'] = opciones

    #Entradas 
    e_texto = Entry(menu2, font = ("Rubik 20"),justify= 'right', width = 8)
    e_texto.place(x=198, y=14)

    e_texto2 = Entry(menu2, font = ("Rubik 20"),justify= 'right', width = 8)
    e_texto2.place(x=198, y=75)


 #Agregar botones en pantalla de tiempo 
 # fila 1
    boton7 = Button(menu2, text = "7",command= lambda: click_boton(7),bg="#454545", fg="#ffffff",font = ("Bahnschrift Condensed",20))
    boton7.place(x=15, y=151,width = 73, height = 56)
    
    boton8 = Button(menu2, text = "8",command= lambda: click_boton(8),bg="#454545", fg="#ffffff",font = ("Bahnschrift Condensed",20))
    boton8.place(x=102, y=151,width = 73, height = 56)
    
    boton9 = Button(menu2, text = "9",command= lambda: click_boton(9),bg="#454545", fg="#ffffff",font = ("Bahnschrift Condensed",20))
    boton9.place(x=187, y=151,width = 73, height = 56)
    
    boton_borrar = Button(menu2, text = "Borrar",command= lambda: borrar(),bg="#4d2405", fg="#ffffff",font = ("Bahnschrift Condensed",18))
    boton_borrar.place(x=272, y=151,width = 73, height = 121) 
    
    # fila 2
    boton4 = Button(menu2, text = "4",command= lambda: click_boton(4),bg="#454545", fg="#ffffff",font = ("Bahnschrift Condensed",20))
    boton4.place(x=15, y=217,width = 73, height = 56)
    
    boton5 = Button(menu2, text = "5",command= lambda: click_boton(5),bg="#454545", fg="#ffffff",font = ("Bahnschrift Condensed",20))
    boton5.place(x=102, y=217,width = 73, height = 56)
    
    boton6 = Button(menu2, text = "6",command= lambda: click_boton(6),bg="#454545", fg="#ffffff",font = ("Bahnschrift Condensed",20))
    boton6.place(x=187, y=217,width = 73, height = 56)
    
    # fila 3
    boton1 = Button(menu2, text = "1",command= lambda: click_boton(1),bg="#454545", fg="#ffffff",font = ("Bahnschrift Condensed",20))
    boton1.place(x=15, y=281,width = 73, height = 56)
    
    boton2 = Button(menu2, text = "2",command= lambda: click_boton(2),bg="#454545", fg="#ffffff",font = ("Bahnschrift Condensed",20))
    boton2.place(x=102, y=281,width = 73, height = 56)
    
    boton3 = Button(menu2, text = "3",command= lambda: click_boton(3),bg="#454545", fg="#ffffff",font = ("Bahnschrift Condensed",20))
    boton3.place(x=187, y=281,width = 73, height = 56)
    
    boton_operar = Button(menu2, text = "Ejecutar",command=operar,bg="#4d2405", fg="#ffffff",font = ("Bahnschrift Condensed",18))
    boton_operar.place(x=272, y=281,width = 73, height = 120) 
    
    # fila 4
    
    boton0 = Button(menu2, text = "0",command= lambda: click_boton(0),bg="#454545", fg="#ffffff",font = ("Bahnschrift Condensed",20))
    boton0.place(x=15, y=345, width = 160, height = 56)
    
    boton1 = Button(menu2, text = ".",command= lambda: click_boton("."),bg="#454545", fg="#ffffff",font = ("Bahnschrift Condensed",20))
    boton1.place(x=187, y=345,width = 73,height=56)