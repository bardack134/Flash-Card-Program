from tkinter import *
from PIL import Image, ImageTk

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


#mi foto esta demasiodo grande por lo que usare el modulo PIL(python image libray para redimencionarla)
front_image=Image.open("img1.png")


#con el comando resize podemos redimencionar nuestras imagenes
front_image_resized = front_image.resize((800, 526), Image.Resampling.LANCZOS)


#usamos nuestra 'front_image_resized' que hasido redimencionada
#Usamos ImageTk.PhotoImage para convertirlo en un formato compatible con Tkinter antes de poder usarlo
card_front_image = ImageTk.PhotoImage(front_image_resized)


#creo mi foto dentro del canvas
my_canvas.create_image(400, 263, image=card_front_image, anchor='center')
# my_canvas.create_image(0, 20, image=card_front_imagen, anchor='nw')


#labels donde iran las palabras del vocabulario
title=my_canvas.create_text(400,150, text='Title' , fill='white', font=("Ariel", 40, "italic"))



word=my_canvas.create_text(400, 253, text='Word', fill='white', font=("Ariel", 60, "bold"))



#para correr nuestra app
window.mainloop()