"""
Quiero contar del 1 al 100 de uno en uno (imprimiendo cada uno).
¿De cuántas maneras eres capaz de hacerlo?
Crea el código para cada una de ellas.
"""

def manera1():
	numero = 1

	while(numero <= 100):
		print(numero)
		numero += 1

def manera2():
	for numero in range(1, 101):
		print(numero)

def manera3(numero):
	if numero <= 100:
		print(numero)
		numero += 1
		manera3(numero)

# manera1()  	# WHILE
# manera2()		# FOR
# manera3(0)	# IF