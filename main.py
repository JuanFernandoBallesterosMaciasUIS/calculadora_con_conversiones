from tkinter import *
from tkinter import messagebox, ttk
import menu

#Ventana principal
ventana = Tk()
ventana.title("Calculadora")
ventana.geometry("350x410")
ventana.resizable(0,0)



#Entrada
e_texto = Entry(ventana, font = ("Rubik 20"), borderwidth = 4,justify= 'right')
e_texto.place(x=0, y=10)


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

boton1 = Button(ventana, text = "1", width = 9, height = 3, command= lambda: click_boton(1))
boton2 = Button(ventana, text = "2", width = 9, height = 3, command= lambda: click_boton(2))
boton3 = Button(ventana, text = "3", width = 9, height = 3, command= lambda: click_boton(3))
boton4 = Button(ventana, text = "4", width = 9, height = 3, command= lambda: click_boton(4))
boton5 = Button(ventana, text = "5", width = 9, height = 3, command= lambda: click_boton(5))
boton6 = Button(ventana, text = "6", width = 9, height = 3, command= lambda: click_boton(6))
boton7 = Button(ventana, text = "7", width = 9, height = 3, command= lambda: click_boton(7))
boton8 = Button(ventana, text = "8", width = 9, height = 3, command= lambda: click_boton(8))
boton9 = Button(ventana, text = "9", width = 9, height = 3, command= lambda: click_boton(9))
boton0 = Button(ventana, text = "0", width = 21, height = 3, command= lambda: click_boton(0))



boton_borrar = Button(ventana, text = "AC", width = 9, height = 3, command= lambda: borrar())
boton_parentesis1 = Button(ventana, text = "(", width = 9, height = 3, command= lambda: click_boton("("))
boton_parentesis2 = Button(ventana, text = ")", width = 9, height = 3, command= lambda: click_boton(")"))
boton_punto = Button(ventana, text = ".", width = 9, height = 3, command= lambda: click_boton("."))

boton_suma = Button(ventana, text = "+", width = 9, height = 3, command= lambda: click_boton("+"))
boton_resta = Button(ventana, text = "-", width = 9, height = 3, command= lambda: click_boton("-"))
boton_mult = Button(ventana, text = "*", width = 9, height = 3, command= lambda: click_boton("*"))
boton_div = Button(ventana, text = "/", width = 9, height = 3, command= lambda: click_boton("/"))
boton_igual = Button(ventana, text = "=", width = 9, height = 3, command= lambda: hacer_operacion())


#Agregar botones en pantalla

#Menu
button = ttk.Button(text = "Conversiones", command = menu.menu_conversiones)
button.place(x=5, y=380)

#Fila 1
boton_borrar.place(x=9, y=56)
boton_parentesis1.place(x=97, y=56)
boton_parentesis2.place(x=182, y=56)
boton_div.place(x=267, y=56)

#Fila 2
boton7.place(x=9, y=121)
boton8.place(x=97, y=121)
boton9.place(x=182, y=121)
boton_mult.place(x=267, y=121)

#Fila 3
boton4.place(x=9, y=186)
boton5.place(x=97, y=186)
boton6.place(x=182, y=186)
boton_suma.place(x=265, y=186)

#Fila 4
boton1.place(x=9, y=250)
boton2.place(x=97, y=250)
boton3.place(x=182, y=250)
boton_resta.place(x=267, y=250)

#Fila 5
boton0.place(x=9, y=315)
boton_punto.place(x=182, y=315)
boton_igual.place(x=267, y=315)


ventana.mainloop()

