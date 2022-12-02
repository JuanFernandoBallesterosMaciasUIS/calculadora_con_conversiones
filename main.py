from tkinter import *
from tkinter import messagebox, ttk
import menu

#Ventana principal
ventana = Tk()
ventana.iconbitmap('icono/logo21.ico')
ventana.title("Calculadora")
#ventana.geometry("350x425")
ventana.resizable(0,0)
ventana.config(bg="#080808")

#  Obtenemos el largo y  ancho de la pantalla
wtotal = ventana.winfo_screenwidth()
htotal = ventana.winfo_screenheight()
#  Guardamos el largo y alto de la ventana
wventana = 350
hventana = 425

#  Aplicamos la siguiente formula para calcular donde debería posicionarse
pwidth = round(wtotal/2-wventana/2)
pheight = round(htotal/2-hventana/2)

#  Se lo aplicamos a la geometría de la ventana
ventana.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight))



#Entrada
e_texto = Entry(ventana, font = ("Rubik 20"), borderwidth = 4, justify= 'right',bg="#080808",fg="#ffffff")
e_texto.place(x=0, y=0,width = 350, height = 50)

#funciones



def click_boton(valor):
    global i
    e_texto.insert(i, valor)
    i += 1


def borrar():
    e_texto.delete(0, END)


def hacer_operacion():
    ecuacion = e_texto.get()
    resultado = eval(ecuacion)
    e_texto.delete(0, END)
    e_texto.insert(0, resultado)
i = 0





#Botones

boton1 = Button(ventana, text = "1", command= lambda: click_boton(1),bg="#454545", fg="#ffffff",font = ("Bahnschrift Condensed",20))
boton2 = Button(ventana, text = "2", command= lambda: click_boton(2),bg="#454545", fg="#ffffff",font = ("Bahnschrift Condensed",20))
boton3 = Button(ventana, text = "3", command= lambda: click_boton(3),bg="#454545", fg="#ffffff",font = ("Bahnschrift Condensed",20))
boton4 = Button(ventana, text = "4", command= lambda: click_boton(4),bg="#454545", fg="#ffffff",font = ("Bahnschrift Condensed",20))
boton5 = Button(ventana, text = "5", command= lambda: click_boton(5),bg="#454545", fg="#ffffff",font = ("Bahnschrift Condensed",20))
boton6 = Button(ventana, text = "6", command= lambda: click_boton(6),bg="#454545", fg="#ffffff",font = ("Bahnschrift Condensed",20))
boton7 = Button(ventana, text = "7", command= lambda: click_boton(7),bg="#454545", fg="#ffffff",font = ("Bahnschrift Condensed",20))
boton8 = Button(ventana, text = "8", command= lambda: click_boton(8),bg="#454545", fg="#ffffff",font = ("Bahnschrift Condensed",20))
boton9 = Button(ventana, text = "9", command= lambda: click_boton(9),bg="#454545", fg="#ffffff",font = ("Bahnschrift Condensed",20))
boton0 = Button(ventana, text = "0", command= lambda: click_boton(0),bg="#454545", fg="#ffffff",font = ("Bahnschrift Condensed",20))



boton_borrar = Button(ventana, text = "AC", command= lambda: borrar(),bg="#454545", fg="#b05c1b",font = ("Bahnschrift Condensed",25))
boton_parentesis1 = Button(ventana, text = "(", command= lambda: click_boton("("),bg="#454545", fg="#b05c1b",font = ("Bahnschrift Condensed",25))
boton_parentesis2 = Button(ventana, text = ")", command= lambda: click_boton(")"),bg="#454545", fg="#b05c1b",font = ("Bahnschrift Condensed",25))
boton_punto = Button(ventana, text = ".", command= lambda: click_boton("."),bg="#454545", fg="#b05c1b",font = ("Bahnschrift Condensed",25))

boton_suma = Button(ventana, text = "+", command= lambda: click_boton("+"),bg="#454545", fg="#b05c1b",font = ("Bahnschrift Condensed",25))
boton_resta = Button(ventana, text = "-", command= lambda: click_boton("-"),bg="#454545", fg="#b05c1b",font = ("Bahnschrift Condensed",25))
boton_mult = Button(ventana, text = "*", command= lambda: click_boton("*"),bg="#454545", fg="#b05c1b",font = ("Bahnschrift Condensed",25))
boton_div = Button(ventana, text = "/", command= lambda: click_boton("/"),bg="#454545", fg="#b05c1b",font = ("Bahnschrift Condensed",25))
boton_igual = Button(ventana, text = "=", command= lambda: hacer_operacion(),bg="#454545", fg="#b05c1b",font = ("Bahnschrift Condensed",25))


#Agregar botones en pantalla

#Menu
button = Button(text = "Conversiones", command = menu.menu_conversiones,bg="#4d2405", fg="#ffffff",font = ("Bahnschrift Condensed",18))
button.place(x=115, y=380,width = 120, height = 40)

#Fila 1
boton_borrar.place(x=9, y=56, width = 73, height = 56)
boton_parentesis1.place(x=97, y=56, width = 73, height = 56)
boton_parentesis2.place(x=182, y=56, width = 73, height = 56)
boton_div.place(x=267, y=56, width = 73, height = 56)

#Fila 2
boton7.place(x=9, y=121, width = 73, height = 56)
boton8.place(x=97, y=121, width = 73, height = 56)
boton9.place(x=182, y=121, width = 73, height = 56)
boton_mult.place(x=267, y=121, width = 73, height = 56)

#Fila 3
boton4.place(x=9, y=186, width = 73, height = 56)
boton5.place(x=97, y=186, width = 73, height = 56)
boton6.place(x=182, y=186, width = 73, height = 56)
boton_suma.place(x=265, y=186, width = 73, height = 56)

#Fila 4
boton1.place(x=9, y=250, width = 73, height = 56)
boton2.place(x=97, y=250, width = 73, height = 56)
boton3.place(x=182, y=250, width = 73, height = 56)
boton_resta.place(x=267, y=250, width = 73, height = 56)

#Fila 5
boton0.place(x=9, y=315, width = 73, height = 56)
boton_punto.place(x=97, y=315, width = 73, height = 56)
boton_igual.place(x=180, y=315, width = 160, height = 56)


ventana.mainloop()