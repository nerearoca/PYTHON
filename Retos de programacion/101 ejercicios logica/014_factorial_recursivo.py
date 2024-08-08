"""
Escribe una función que calcule y retorne el factorial de un número dado
de forma recursiva.
"""

# Factorial es de manera recursiva calcular su numero

def calcular_factorial(numero):
	factorial = 1
	while(numero > 0):
		factorial *= numero
		numero -= 1

	return factorial

numero = int(input("Escriba el numero a calcular: "))
print(calcular_factorial(numero))