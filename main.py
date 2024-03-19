from tkinter import *
from PIL import Image, ImageTk

#CONSTANTES
BACKGROUND_COLOR = "#FFF8E3"

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


#Creamos overlay para mejorar la legibilidad del texto sobre la imagen de fondo
overlay=my_canvas.create_rectangle(200,100,590, 350, fill='black', stipple='gray50')


#donde iran las palabras del vocabulario, lo ponemos encima del overlay
# title=my_canvas.create_text(400,150, text='Title' , fill='pink', font=("Ariel", 40, "italic"))



# word=my_canvas.create_text(400, 253, text='Word', fill='white', font=("Ariel", 60, "bold"))

# labels donde iran las palabras del vocabulario
title_label=Label(my_canvas, text='Title', fg='white', bg='#000000', font=("Ariel", 40, "italic"))
title_label.place(x=400, y=150, anchor='center')


word_label=Label(my_canvas, text='Word', fg='white', bg='#000000', font=("Ariel", 60, "bold"))
word_label.place(x=400, y=263, anchor='center')

#para correr nuestra app
window.mainloop()