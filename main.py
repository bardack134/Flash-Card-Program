from tkinter import *


#CONSTANTES
BACKGROUND_COLOR = "#B1DDC6"

#TODO: CREANDO LA CONFIGURACION INICIAL DE NUESTRA APP
#creando ventana
window=Tk()


#parametros que definen la interfaz de nuestra ventana, como padin y color de fondo
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)


#titulo de la ventana
window.title("Flash Cards")


#creo mi canvas widget donde voy a  poner la photo del card
my_canvas=Canvas(window, bg=BACKGROUND_COLOR,  width=800,  height=526, highlightthickness=0 )


#pongo el canvas en mi ventana
my_canvas.grid(row=0, column=1, columnspan=2)


#cargo la imagen
card_front_imagen=PhotoImage(file="card_front.png")


#creo mi foto dentro del canvas
my_canvas.create_image(400, 263, image=card_front_imagen, anchor='center')
# my_canvas.create_image(0, 20, image=card_front_imagen, anchor='nw')


#labels donde iran las palabras del vocabulario
title_label=Label(my_canvas, text='Title', font=("Ariel", 40, "italic"), bg='white')
title_label.place(x=400, y=150, anchor='center')


word_label=Label(my_canvas, text='Word', bg='white', font=("Ariel", 60, "bold"))
word_label.place(x=400, y=263, anchor='center')


#para correr nuestra app
window.mainloop()