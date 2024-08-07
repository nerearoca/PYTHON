"""

Crea una función que reciba dos cadenas como parámetro (str1, str2)
e imprima otras dos cadenas como salida (out1, out2).
- out1 contendrá todos los caracteres presentes en la str1 pero NO
  estén presentes en str2.
- out2 contendrá todos los caracteres presentes en la str2 pero NO
  estén presentes en str1.
"""

cadena1, cadena2 = "Hola", "Adeu"

def reemplazar_letras(cadena1, cadena2):
	# print(cadena1, cadena2)
	# lista = cadena2.split('')
	cadena1, cadena2 = set(cadena1.lower()), set(cadena2.lower())
	caracteres_presentes = ''.join(sorted(cadena1 - cadena2))

	# index = 0
	# caracteres_presentes = ""

	# for letra in cadena1:	
	# 	if letra != cadena2[index]:
	# 		caracteres_presentes = letra
	# 	index += 1

	return caracteres_presentes

def reemplazar(cadena1, cadena2):
	out1 = reemplazar_letras(cadena1, cadena2)
	out2 = reemplazar_letras(cadena2, cadena1)

	return out1, out2

print(reemplazar(cadena1, cadena2))