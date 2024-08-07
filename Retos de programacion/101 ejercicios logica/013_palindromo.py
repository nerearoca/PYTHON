"""
Escribe una función que reciba un texto y retorne verdadero o
falso (Boolean) según sean o no palíndromos.

Un Palíndromo es una palabra o expresión que es igual si se lee
de izquierda a derecha que de derecha a izquierda.
 
NO se tienen en cuenta los espacios, signos de puntuación y tildes.
Ejemplo: Ana lleva al oso la avellana.
"""
import re

def es_palindromo(original_text):
	# Editar el text, lower(), y cambiar el texto y signos de comparacion
	original_text = original_text.lower()
	original_text = re.sub(re.compile(r"[.|,| |:|;|-|_|?|'|¿|¡]"), '', original_text)
	reversed_string = ""
	# Reverse string
	for char in original_text:
		reversed_string = char + reversed_string

	# Return the comparation
	if original_text == reversed_string:
		return True
	else:
		return False

# Mostrar resultado
print(es_palindromo("Ana lleva al oso la avellana?"))

