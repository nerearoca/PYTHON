"""
Crea una función que reciba un String de cualquier tipo y se encargue de
 poner en mayúscula la primera letra de cada palabra.
- No se pueden utilizar operaciones del lenguaje que
  lo resuelvan directamente.
"""

def first_may(palabra_frase):
	lista_palabras = palabra_frase.split(' ')
	indice = 0
	for palabra in lista_palabras:
		if palabra[0] == 'a':
			palabra = 'A' + palabra[1:]
		elif palabra[0] == 'b':
			palabra = 'B' + palabra[1:]
		elif palabra[0] == 'c':
			palabra = 'C' + palabra[1:]
		elif palabra[0] == 'd':
			palabra = 'D' + palabra[1:]
		elif palabra[0] == 'e':
			palabra = 'E' + palabra[1:]
		elif palabra[0] == 'f':
			palabra = 'F' + palabra[1:]
		elif palabra[0] == 'g':
			palabra = 'G' + palabra[1:]
		elif palabra[0] == 'h':
			palabra = 'H' + palabra[1:]
		elif palabra[0] == 'i':
			palabra = 'I' + palabra[1:]
		elif palabra[0] == 'j':
			palabra = 'J' + palabra[1:]
		elif palabra[0] == 'k':
			palabra = 'K' + palabra[1:]
		elif palabra[0] == 'l':
			palabra = 'L' + palabra[1:]
		elif palabra[0] == 'm':
			palabra = 'M' + palabra[1:]
		elif palabra[0] == 'n':
			palabra = 'N' + palabra[1:]
		elif palabra[0] == 'o':
			palabra = 'O' + palabra[1:]
		elif palabra[0] == 'p':
			palabra = 'P' + palabra[1:]
		elif palabra[0] == 'q':
			palabra = 'Q' + palabra[1:]
		elif palabra[0] == 'r':
			palabra = 'R' + palabra[1:]
		elif palabra[0] == 's':
			palabra = 'S' + palabra[1:]
		elif palabra[0] == 't':
			palabra = 'T' + palabra[1:]
		elif palabra[0] == 'u':
			palabra = 'U' + palabra[1:]
		elif palabra[0] == 'v':
			palabra = 'V' + palabra[1:]
		elif palabra[0] == 'w':
			palabra = 'W' + palabra[1:]
		elif palabra[0] == 'x':
			palabra = 'X' + palabra[1:]
		elif palabra[0] == 'y':
			palabra = 'Y' + palabra[1:]
		elif palabra[0] == 'z':
			palabra = 'Z' + palabra[1:]
		lista_palabras[indice] = palabra
		indice += 1

	frase = ""
	for palabra in lista_palabras:
		frase +=  palabra + " "

	return frase	

print('hola -->', first_may('hola'))
print('aloha -->', first_may('aloha'))
print('La casa de la vecina -->', first_may('La casa de la vecina'))
print('Al otro lado del rio -->', first_may('Al otro lado del rio'))
print('Al lado esta la playa -->', first_may('Al lado esta la playa'))