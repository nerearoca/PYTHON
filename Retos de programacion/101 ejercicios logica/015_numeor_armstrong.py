"""
Escribe una función que calcule si un número dado es un número de Armstrong
(o también llamado narcisista).
Si no conoces qué es un número de Armstrong, debes buscar información
al respecto. 
"""


def numero_armstrong(numero):

	numero_final = 0
	for num in numero:
		numero_final += (int(num) * int(num) * int(num))

	if int(numero) == numero_final:
		return True
	else:
		return False
print(numero_armstrong("360"))
