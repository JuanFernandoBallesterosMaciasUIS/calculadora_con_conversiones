from tkinter import *
from tkinter import messagebox, ttk
import Longitud
import masa
import temperatura
import volumen
import Tiempo

def menu_conversiones():
    
    menu = Tk()
    menu.iconbitmap('icono/logo21.ico')
    menu.title("Conversiones")
    menu.config(bg="#080808")
    #menu.geometry("300x260")
    menu.resizable(0,0)
    
    #  Obtenemos el largo y  ancho de la pantalla
    wtotal = menu.winfo_screenwidth()
    htotal = menu.winfo_screenheight()
    #  Guardamos el largo y alto de la ventana
    wventana = 300
    hventana = 300

    #  Aplicamos la siguiente formula para calcular donde debería posicionarse
    pwidth = round(wtotal/2-wventana/2)
    pheight = round(htotal/2-hventana/2)

    #  Se lo aplicamos a la geometría de la ventana
    menu.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight))
    
    menu.config(bg="black")

  
    #Menu
    button_long = Button(menu,text = "Longitud", command = Longitud.vent_longitud,font = ("Bahnschrift Condensed",15))
    button_long.place(x=100, y=50, width = 97, height = 40)
    
    button_long = Button(menu,text = "Masa", command = masa.vent_masa,font = ("Bahnschrift Condensed",15))
    button_long.place(x=100, y=100, width = 97, height = 40)
    
    button_long = Button(menu,text = "Temperatura", command = temperatura.vent_temperatura,font = ("Bahnschrift Condensed",15))
    button_long.place(x=100, y=150, width = 97, height = 40)
    
    button_long = Button(menu,text = "Volumen", command = volumen.vent_volumen,font = ("Bahnschrift Condensed",15))
    button_long.place(x=100, y=200, width = 97, height = 40)
    
    button_long = Button(menu,text = "Tiempo", command = Tiempo.vent_tiempo,font = ("Bahnschrift Condensed",15))
    button_long.place(x=100, y=250, width = 97, height = 40)
    
    label = Label(menu, text="Selecciona una magnitud",font = ("Bahnschrift Condensed",15),fg="white",bg="black")
    label.grid(row = 0, column = 0, padx = 60, pady = 10)


    menu.mainloop