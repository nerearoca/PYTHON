"""
Crea un programa que invierta el orden de una cadena de texto
	sin usar funciones propias del lenguaje que lo hagan de forma 
	automática.
- Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""

nueva_palabra = input('Inserte una cadena de texto: ')

def cadena_inversa(palabra):

	cadena_invertida= []
	for letra in palabra:
		cadena_invertida.insert(0, letra)

	palabra_invertida = ""
	for letra in cadena_invertida:
		palabra_invertida += letra

	print(palabra_invertida)

cadena_inversa(nueva_palabra)

# CORRECCION

def reverse(text):
	text_len = len(text)
	reversed_text = ""

	for index in range(0, text_len):
		reversed_text += text[text_len - index - 1]

	return reversed_text

print(reverse('Hola mundo'))