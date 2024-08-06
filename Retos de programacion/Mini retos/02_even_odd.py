"""
PAR O IMPAR
Crea un programa que compruebe si
un número entero es par o impar.
"""

def par_impar(numero):
	if numero % 2:
		return "El numero no es par"
	else:
		return "El numero es par"

dec = input('Escriba un numero para ver si es par o no: ')
binario = par_impar(int(dec))
print(binario)