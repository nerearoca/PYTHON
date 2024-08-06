"""
INVERSIÓN DE CADENAS
Crea una función que invierta
una cadena de texto.
"""

def invertir(cadena):
	cadena_invertida = ""
	for letra in cadena:
		cadena_invertida = letra + "" + cadena_invertida
	return cadena_invertida

cadena = input('Cadena a invertir: ')
cadena_invertida = invertir(cadena)

print(cadena_invertida)