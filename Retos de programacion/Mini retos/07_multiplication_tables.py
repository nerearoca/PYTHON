"""
TABLAS DE MULTIPLICAR
Imprime todas las tablas de
multiplicar de 1 al 10.
"""

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for numero in numeros:
	print(f"TABLA DEL {numero}")
	for numero_pequeño in numeros:
		# print(str(numero) + " * " + str(numero_pequeño) + " = " + str(numero * numero_pequeño))
		print(f"{numero} * {numero_pequeño} = {numero * numero_pequeño}")