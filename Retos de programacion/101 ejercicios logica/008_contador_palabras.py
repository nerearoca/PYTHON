"""
  Crea un programa que cuente cuantas veces se repite cada palabra
 y que muestre el recuento final de todas ellas.
 - Los signos de puntuación no forman parte de la palabra.
 - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
 - No se pueden utilizar funciones propias del lenguaje que
   lo resuelvan automáticamente.
"""

import re

def contador_palabras(frase_proporcinada):

	separacion_palabras = frase_proporcinada.split(" ")

	# print(separacion_palabras)


	# Buscar caracteres especiales y quitarlos
	pattern = "[.|:|,|;|-|_]"
	index = 0

	for palabra in separacion_palabras:
		separacion_palabras[index] = palabra.lower()
		find = re.findall(pattern, palabra)

		if find:
			sig = find[0]
			palabra = palabra.replace(sig, "")
			separacion_palabras[index] = palabra.lower()
			
		index += 1	
		

	# Pasar a unicas
	palabras_unicas = set(separacion_palabras)

	diccionario = dict()

	# Converir a diccionario
	for palabra in palabras_unicas:
		diccionario[palabra] = 0

	# Contar numero de repetidas
	for palabra in separacion_palabras:
		diccionario[palabra] += 1
	
	return diccionario, palabras_unicas

frase = 'La casa roja esta al lado de la casa amarilla. Asi mismo la amarilla esta al lado de la casa roja'
diccionario_palabras, palabras_unicas = contador_palabras(frase)
 
# RESULTADO
print(frase)
for palabra in palabras_unicas:
	print(f"{palabra} => {diccionario_palabras[palabra]}" )