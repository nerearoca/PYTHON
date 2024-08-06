"""
CONVERSOR DE TEMPERATURAS
Crea un conversor entre
grados Celsius y Fahrenheit. 
"""

def fah_to_cel(fah):
	# Formula --> (°F - 32) x 5/9 =°C
	celsius = (fah - 32) * 5/9

	return celsius

def cel_to_fah(cel):
	# (°C x 9/5) + 32 =°F
	fahrenheit = (cel * 9/5) + 32

	return fahrenheit

 
tipo = int(input("Pasar de \n1)Fahrenheit a Celsius \n2)Celsius a Fahrenheit \n"))

if tipo == 1 or tipo == 2:
	numero = input("Introducir grados: ")

	if tipo == 1:
		print(f"{fah_to_cel(float(numero))} ºC")
	elif tipo == 2:
		
		print(f"{cel_to_fah(int(numero))} ºF")

		
		# cel_to_fah(int(numero))

else:
	print("Error, valor introducido incorrecto")