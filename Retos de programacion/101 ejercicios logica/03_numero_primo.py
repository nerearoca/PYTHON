# Escribe un programa que se encargue de comprobar si un número 
# 	es o no primo.
# Hecho esto, imprime los números primos entre 1 y 100.

def primo(numero: int):

	is_primo = True
	multiplos = [2,3,5,7,11]
	
	for multiplo in multiplos:
		if(int(numero) % int(multiplo) == 0):
			if(int(numero) == int(multiplo)):
				is_primo = True
			else:
				is_primo = False

	if(is_primo):
		print('Su numero es primo')
	else:
		print('Su numero NO es primo')

	nPrimos = []
	for index in range(0, 100):

		is_primo = True
		multiplos = [2,3,5,7,11]

		for multiplo in multiplos:
			if(int(index) % int(multiplo) == 0):
				if(int(index) == int(multiplo)):
					is_primo = True
				else:
					is_primo = False

		if(is_primo):
			nPrimos.append(index)
	
	print(nPrimos)

new_number = input('Inserte el numero a comprovar: ')

primo(new_number)

# CORRECCION

def is_prime():

	for number in range(1, 101):

		if number >= 2:

			is_divisible = False

			for index in range(2, number):
				if number % index == 0:
					is_divisible = True
					break

			if not is_divisible:
				print(number)


is_prime()