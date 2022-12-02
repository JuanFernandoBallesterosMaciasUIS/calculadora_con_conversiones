from tkinter import *
from tkinter import ttk
from tkinter import messagebox

i = 0

def vent_masa():
    menu = Tk()
    menu.iconbitmap('icono/logo21.ico')
    menu.title("Masa")
    menu.config(bg="#080808")
    #menu.geometry("355x410")
    menu.config(bg="#080808")
    menu.resizable(0,0)
    
    #  Obtenemos el largo y  ancho de la pantalla
    wtotal = menu.winfo_screenwidth()
    htotal = menu.winfo_screenheight()
    #  Guardamos el largo y alto de la ventana
    wventana = 355
    hventana = 410

    #  Aplicamos la siguiente formula para calcular donde debería posicionarse
    pwidth = round(wtotal/2-wventana/2)
    pheight = round(htotal/2-hventana/2)

    #  Se lo aplicamos a la geometría de la ventana
    menu.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight))
    

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
        
        
        if opc1 == "Kilogramos" and opc2 == "Libras":
            x = float(e_texto.get())
            resul = x*2
            e_texto2.delete(0, END)
            e_texto2.insert(0,string=str(resul))
            
        elif opc1 == "Kilogramos" and opc2 == "Gramos":
            x = float(e_texto.get())
            resul = x*1000
            e_texto2.delete(0, END)
            e_texto2.insert(0,string=str(resul))
            
        elif opc1 == "Kilogramos" and opc2 == "Miligramos":
            x = float(e_texto.get())
            resul = x*1000000
            e_texto2.delete(0, END)
            e_texto2.insert(0,string=str(resul))
            
            
        elif opc1 == "Libras" and opc2 == "Kilogramos":
            x = float(e_texto.get())
            resul = x*0.5
            e_texto2.delete(0, END)
            e_texto2.insert(0,string=str(resul))
        
        elif opc1 == "Libras" and opc2 == "Gramos":
            x = float(e_texto.get())
            resul = x*500
            e_texto2.delete(0, END)
            e_texto2.insert(0,string=str(resul))
            
        elif opc1 == "Libras" and opc2 == "Miligramos":
            x = float(e_texto.get())
            resul = x*500000
            e_texto2.delete(0, END)
            e_texto2.insert(0,string=str(resul))
            
        elif opc1 == "Gramos" and opc2 == "Kilogramos":
            x = float(e_texto.get())
            resul = x*0.001
            e_texto2.delete(0, END)
            e_texto2.insert(0,string=str(resul))
            
        elif opc1 == "Gramos" and opc2 == "Libras":
            x = float(e_texto.get())
            resul = x*(1/500)
            e_texto2.delete(0, END)
            e_texto2.insert(0,string=str(resul))
            
        elif opc1 == "Gramos" and opc2 == "Miligramos":
            x = float(e_texto.get())
            resul = x*1000
            e_texto2.delete(0, END)
            e_texto2.insert(0,string=str(resul))
            
        elif opc1 == "Miligramos" and opc2 == "Kilogramos":
            x = float(e_texto.get())
            resul = x*(1/1000000)
            e_texto2.delete(0, END)
            e_texto2.insert(0,string=str(resul))
            
        elif opc1 == "Miligramos" and opc2 == "Libras":
            x = float(e_texto.get())
            resul = x*(1/500)
            e_texto2.delete(0, END)
            e_texto2.insert(0,string=str(resul))
            
        elif opc1 == "Miligramos" and opc2 == "Gramos":
            x = float(e_texto.get())
            resul = x*(1/1000)
            e_texto2.delete(0, END)
            e_texto2.insert(0,string=str(resul))
        else:
            messagebox.showinfo("Error", "Selecciona unidades diferentes")
            
        
            
    # Frame
    frame1 = Frame(menu)
    frame1.config(bg="lightsteelblue3", width = 355, height = 146)
    frame1.place(x=0, y=0)
    frame1.config(bg="#080808")
    

    frame2 = Frame(menu)
    frame2.config(bg="lightsteelblue3", width = 335, height = 125)
    frame2.place(x=11, y=11)
    frame2.config(bg="#080808")

    # Listas desplegables
    lista_desplegable = ttk.Combobox(menu, width = 12)
    lista_desplegable.place (x = 20, y = 20 )

    #lista de opciones
    opciones = ["Kilogramos","Libras","Gramos","Miligramos"]
    lista_desplegable['values'] = opciones

    lista_desplegable2 = ttk.Combobox(menu, width = 12)
    lista_desplegable2.place (x = 20, y = 75 )


    #lista de opciones
    opciones = ["Kilogramos","Libras","Gramos","Miligramos"]
    lista_desplegable2['values'] = opciones

    #Entradas 
    e_texto = Entry(menu, font = ("Rubik 20"),justify= 'right', width = 8)
    e_texto.place(x=198, y=14)

    e_texto2 = Entry(menu, font = ("Rubik 20"),justify= 'right', width = 8)
    e_texto2.place(x=198, y=75)


    #Agregar botones en pantalla de longitud 
    # fila 1
    boton7 = Button(menu, text = "7",command= lambda: click_boton(7),bg="#454545", fg="#ffffff",font = ("Bahnschrift Condensed",20))
    boton7.place(x=15, y=151,width = 73, height = 56)
    
    boton8 = Button(menu, text = "8",command= lambda: click_boton(8),bg="#454545", fg="#ffffff",font = ("Bahnschrift Condensed",20))
    boton8.place(x=102, y=151,width = 73, height = 56)
    
    boton9 = Button(menu, text = "9",command= lambda: click_boton(9),bg="#454545", fg="#ffffff",font = ("Bahnschrift Condensed",20))
    boton9.place(x=187, y=151,width = 73, height = 56)
    
    boton_borrar = Button(menu, text = "Borrar",command= lambda: borrar(),bg="#4d2405", fg="#ffffff",font = ("Bahnschrift Condensed",18))
    boton_borrar.place(x=272, y=151,width = 73, height = 121)
    
    # fila 2
    boton4 = Button(menu, text = "4",command= lambda: click_boton(4),bg="#454545", fg="#ffffff",font = ("Bahnschrift Condensed",20))
    boton4.place(x=15, y=217,width = 73, height = 56)
    
    boton5 = Button(menu, text = "5",command= lambda: click_boton(5),bg="#454545", fg="#ffffff",font = ("Bahnschrift Condensed",20))
    boton5.place(x=102, y=217,width = 73, height = 56)
    
    boton6 = Button(menu, text = "6",command= lambda: click_boton(6),bg="#454545", fg="#ffffff",font = ("Bahnschrift Condensed",20))
    boton6.place(x=187, y=217,width = 73, height = 56)
    
    # fila 3
    boton1 = Button(menu, text = "1",command= lambda: click_boton(1),bg="#454545", fg="#ffffff",font = ("Bahnschrift Condensed",20))
    boton1.place(x=15, y=281,width = 73, height = 56)
    
    boton2 = Button(menu, text = "2",command= lambda: click_boton(2),bg="#454545", fg="#ffffff",font = ("Bahnschrift Condensed",20))
    boton2.place(x=102, y=281,width = 73, height = 56)
    
    boton3 = Button(menu, text = "3",command= lambda: click_boton(3),bg="#454545", fg="#ffffff",font = ("Bahnschrift Condensed",20))
    boton3.place(x=187, y=281,width = 73, height = 56)
    
    boton_operar = Button(menu, text = "Ejecutar",command=operar,bg="#4d2405", fg="#ffffff",font = ("Bahnschrift Condensed",18))
    boton_operar.place(x=272, y=281,width = 73, height = 120) 
    
    # fila 4
    
    boton0 = Button(menu, text = "0",command= lambda: click_boton(0),bg="#454545", fg="#ffffff",font = ("Bahnschrift Condensed",20))
    boton0.place(x=15, y=345, width = 160, height = 56)
    
    boton1 = Button(menu, text = ".",command= lambda: click_boton("."),bg="#454545", fg="#ffffff",font = ("Bahnschrift Condensed",20))
    boton1.place(x=187, y=345,width = 73,height=56)