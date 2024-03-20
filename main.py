import random
from tkinter import *
from PIL import Image, ImageTk
from pandas import *


#CONSTANTES
BACKGROUND_COLOR = "#FFF8E3"

#mi foto esta demasiodo grande por lo que usare el modulo PIL(python image libray para redimencionarla)


#TODO CREAR BOTON QUE ME MUESTRA LA PARTE DE ATRAS DE LA CARD CON EL SIGNIFICADO EN INGLES
def see_card_back():
    #new background of our card
    my_canvas.itemconfigure(card_front_canvas, image=card_back_image )


    #cambio el titulo del card de japones a ingles
    my_canvas.itemconfigure(title, text="English", fill='white')
    
    
    #cambio la palabra del japones al ingles
    my_canvas.itemconfigure(word, text=english_word)
    
    
    #ya no necesito la palabra en hiragana por lo que la elimino
    my_canvas.itemconfigure(hiragana, text="")
    
    
# TODO: CREAR UNA FUNCION PARA TOMAR ALEATORIAMENTE JAPANESE WORDS DEL ARCHIVO vocabulary.csv
#leemos el archivo .csv y creamos un data frame
vocabulary=read_csv("vocabulary.csv")


#creamos una lista de diccionarios, donce cada row es un diccionario y las claves son el nombre de las columnas
data_dictitonary=vocabulary.to_dict(orient='records')


def next_card():  
    #deseo que esta variable sea global para usarla en la funcion 'see_card_back'
    global english_word
    
    #volvemos a escoger aletoriamente una palabra del diccionario
    diccionay_random=random.choice(data_dictitonary)
    
    
    #usando la clave del diccionario, obtenemos el  valor, que es nuestra palabra
    japanese_word=diccionay_random['Japanese']
    hiragana_word=diccionay_random['Hiragana']
    english_word=diccionay_random['English']
    
    
    #agregando la palabra en japones a nuestra card
    my_canvas.itemconfigure(word, text=japanese_word)
    my_canvas.itemconfigure(hiragana, text=hiragana_word)


    #cambio la imagend de fondo del canvas 
    my_canvas.itemconfigure(card_front_canvas, image=card_front_image)
    
    
    #cambio el titulo del card denuevo a japones, con el color rosado
    my_canvas.itemconfigure(title, text="Japanese", fill='pink')
    
    
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
my_canvas.grid(row=0, column=0, columnspan=3)


#mi foto esta demasiodo grande por lo que usare el modulo PIL(python image libray para redimencionarla)
front_image=Image.open("img1.png")


#con el comando resize podemos redimencionar nuestras imagenes
front_image_resized = front_image.resize((800, 526), Image.Resampling.LANCZOS)


#usamos nuestra 'front_image_resized' que hasido redimencionada
#Usamos ImageTk.PhotoImage para convertirlo en un formato compatible con Tkinter antes de poder usarlo
card_front_image = ImageTk.PhotoImage(front_image_resized)


#creo mi foto dentro del canvas
card_front_canvas=my_canvas.create_image(400, 263, image=card_front_image, anchor='center')
# my_canvas.create_image(0, 20, image=card_front_imagen, anchor='nw')


#Creamos overlay para mejorar la legibilidad del texto sobre la imagen de fondo
overlay=my_canvas.create_rectangle(190,100,600, 420, fill='black',  stipple='gray50')


#Cargo mi imagen para la parte de atras del card "back card", esto debe hacerse por fuera de la funcion para que sean variables Globales
back_image=Image.open("img2.png")
#con el comando resize podemos redimencionar nuestras imagenes
back_image_resized = back_image.resize((800, 526), Image.Resampling.LANCZOS)
#usamos nuestra 'back_image_resized' que hasido redimencionada
#Usamos ImageTk.PhotoImage para convertirlo en un formato compatible con Tkinter antes de poder usarlo
card_back_image = ImageTk.PhotoImage(back_image_resized)


#donde iran las palabras del vocabulario, lo ponemos encima del overlay
title=my_canvas.create_text(400,150, text='Japanese' , fill='pink', font=("Ariel", 40, "italic"))
word=my_canvas.create_text(400, 253, text='kanji', fill='white', font=("Ariel", 60, "bold"))
hiragana=my_canvas.create_text(400, 353, text='hiragana', fill='white', font=("Ariel", 30, "bold"))


# Cargando y redimensionando la imagen para el botón 'check', Creando  objeto PhotoImage de Tkinter  para la imagen redimensionada
check_image=Image.open('right.png')
check_image_resized=check_image.resize((75,74),  Image.Resampling.LANCZOS)
check_button_img=ImageTk.PhotoImage(check_image_resized)
check_button=Button(window, image=check_button_img, highlightthickness=0, command=next_card)
check_button.grid(row=1, column=2,  pady=15)


# Cargando y redimensionando la imagen para el botón 'wrong', Creando  objeto PhotoImage de Tkinter  para la imagen redimensionada
wrong_image=Image.open('wrong.png')
wrong_image_resized=wrong_image.resize((75,74),  Image.Resampling.LANCZOS)
wrong_button_img=ImageTk.PhotoImage(wrong_image_resized)
# Creando el botón 'wrong' con la imagen y asignando la función 'next_card' como comando
wrong_button=Button(window, image=wrong_button_img,  highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0,  pady=15)


# Cargando y redimensionando la imagen para el botón 'see_answer', Creando  objeto PhotoImage de Tkinter  para la imagen redimensionada
see_answer_img=Image.open('see.png')
see_answer_img_resized=see_answer_img.resize((42,42), Image.Resampling.LANCZOS)
see_button_img=ImageTk.PhotoImage(see_answer_img_resized)
# Creando el botón con la imagen y asignando la función 'next_card' como comando
see_answer_boton=Button(window, image=see_button_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=see_card_back)
see_answer_boton.grid(row=1, column=1, pady=15)

#llamo a la funcion para que al comenzar el programa me muestra de inmediatamente una palabra kun
next_card()


#para correr nuestra app
window.mainloop()