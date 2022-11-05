from tkinter import *
from tkinter import messagebox, ttk
import Longitud
import masa
import temperatura
import volumen

def menu_conversiones():
    menu = Tk()
    menu.title("Conversiones")
    menu.geometry("250x200")
    
    
    #Menu
    button_long = ttk.Button(menu,text = "Longitud", command = Longitud.vent_longitud)
    button_long.place(x=5, y=30)
    
    button_long = ttk.Button(menu,text = "Masa", command = masa.vent_masa)
    button_long.place(x=5, y=60)
    
    button_long = ttk.Button(menu,text = "Temperatura", command = temperatura.vent_temperatura)
    button_long.place(x=5, y=90)
    
    button_long = ttk.Button(menu,text = "Volumen", command = volumen.vent_volumen)
    button_long.place(x=5, y=120)
    
    label = Label(menu, text="Selecciona un boton")
    label.grid(row = 0, column = 0, padx = 10, pady = 10)
    
    menu.mainloop