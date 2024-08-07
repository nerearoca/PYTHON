"""
ANAGRAMAS
Comprueba si dos cadenas
de texto son anagramas.

Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas.
 - Un Anagrama consiste en formar una palabra reordenando TODAS
   las letras de otra palabra inicial.
 - NO hace falta comprobar que ambas palabras existan.
 - Dos palabras exactamente iguales no son anagrama.
"""

def is_anagram(word_one, word_two):
	if word_one.lower() != word_two.lower() :
		return sorted(word_one.lower()) == sorted(word_two.lower())
	else:
		return False
	
	# if word_one.lower() == word_two.lower() :
	# 	return False
	# return sorted(word_one.lower()) == sorted(word_two.lower())
	

word_one = input('Escriba la primera palabra:')
word_two = input('Escriba la segunda palabra:')

result = is_anagram(word_one, word_two)

print(result)