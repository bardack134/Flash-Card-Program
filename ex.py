#leemos el archivo .csv y creamos un data frame
import random
from pandas import DataFrame, read_csv


vocabulary=read_csv("vocabulary.csv")


#creamos una lista de diccionarios, donce cada row es un diccionario y las claves son el nombre de las columnas
data_dictitonary=vocabulary.to_dict(orient='records')
print(data_dictitonary)

#volvemos a escoger aletoriamente una palabra del diccionario
current_row=random.choice(data_dictitonary)


#usando la clave del diccionario, obtenemos el  valor, que es nuestra palabra
japanese_word=current_row['Japanese']
hiragana_word=current_row['Hiragana']
english_word=current_row['English']
print(japanese_word)
print(hiragana_word)
print(english_word)


#eliminando valor actual de la lista de diccionarios
data_dictitonary.remove(current_row)


#creando dataframe del diccionario actualizado
words_to_learn_df=DataFrame(data=data_dictitonary)


#creando nuevo archivo .csv del nuevo dataframe
words_to_learn_df.to_csv('words_to_learn.csv', index=False)


print(data_dictitonary)