import random
from tkinter import *
from PIL import Image, ImageTk
from pandas import *


#CONSTANTES
BACKGROUND_COLOR = "#FFF8E3"

# TODO: CREAR UNA FUNCION PARA TOMAR ALEATORIAMENTE JAPANESE WORDS DEL ARCHIVO vocabulary.csv
#leemos el archivo .csv y creamos un data frame
vocabulary=read_csv("vocabulary.csv")


#creamos una lista de diccionarios, donce cada row es un diccionario y las claves son el nombre de las columnas
data_dictitonary=vocabulary.to_dict(orient='records')


#tomamos un diccionario random de nuestra lista de diccionarios
diccionay_random=random.choice(data_dictitonary)


#usando las claves del diccionario, obtenemos los valores, que son nuestras palabras
japanese_word=diccionay_random['Japanese']
hiragana_word=diccionay_random['Hiragana']
english_word=diccionay_random['English']
print(japanese_word)


def next_card():
    global diccionay_random
    
    #volvemos a escoger aletoriamente una palabra del diccionario
    diccionay_random=random.choice(data_dictitonary)
    
    
    #usando la clave del diccionario, obtenemos el  valor, que es nuestra palabra
    japanese_word=diccionay_random['Japanese']
    hiragana_word=diccionay_random['Hiragana']
    
    
    #agregando la palabra en japones a nuestra card
    my_canvas.itemconfigure(word, text=japanese_word)
    my_canvas.itemconfigure(hiragana, text=hiragana_word)


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
my_canvas.grid(row=0, column=0, columnspan=2)


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
overlay=my_canvas.create_rectangle(190,100,600, 420, fill='black',  stipple='gray50')


# labels donde iran las palabras del vocabulario
# title_label=Label(my_canvas, text='Title', fg='white', bg='#000000', font=("Ariel", 40, "italic"))
# title_label.place(x=400, y=150, anchor='center')


# word_label=Label(my_canvas, text='Word', fg='white', bg='#000000', font=("Ariel", 60, "bold"))
# word_label.place(x=400, y=263, anchor='center')

#donde iran las palabras del vocabulario, lo ponemos encima del overlay
title=my_canvas.create_text(400,150, text='Japanese' , fill='pink', font=("Ariel", 40, "italic"))
word=my_canvas.create_text(400, 253, text=japanese_word, fill='white', font=("Ariel", 60, "bold"))
hiragana=my_canvas.create_text(400, 353, text=hiragana_word, fill='white', font=("Ariel", 30, "bold"))


#Vamos a gregar botones a nuestra interfaz
check_image=PhotoImage(file='right.png')
check_button=Button(window, image=check_image, highlightthickness=0, command=next_card)
check_button.grid(row=1, column=1,  pady=15)


wrong_image=Image.open('wrong.png')
wrong_image=wrong_image.resize((75,62),  Image.Resampling.LANCZOS)
wrong_image=ImageTk.PhotoImage(file='wrong.png')
wrong_button=Button(window, image=wrong_image,  highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0,  pady=15)



#para correr nuestra app
window.mainloop()