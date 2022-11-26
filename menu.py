from tkinter import *
from tkinter import messagebox, ttk
import Longitud
import masa
import temperatura
import volumen

def menu_conversiones():
    
    menu = Tk()
    menu.title("Conversiones")
    menu.geometry("300x260")
    
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
    
    label = Label(menu, text="Selecciona una magnitud",font = ("Bahnschrift Condensed",15),fg="white",bg="black")
    label.grid(row = 0, column = 0, padx = 60, pady = 10)


    menu.mainloop