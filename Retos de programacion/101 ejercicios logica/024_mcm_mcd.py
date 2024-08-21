"""
 Crea dos funciones, una que calcule el máximo común divisor (MCD) y otra
 que calcule el mínimo común múltiplo (mcm) de dos números enteros.
 - No se pueden utilizar operaciones del lenguaje que
  lo resuelvan directamente.
"""

def recursive_mcm(num):
	# Inicializar la lista y el numero en int(no en float)
	array_num1 = list()
	num1 = int(num)  # Sirve para poderlo editar

	# Comprovar por los primos mas comunes
	while not num1 % 2 :
		array_num1.append(2)
		num1 /= 2

	while not num1 % 3 :
		array_num1.append(3)
		num1 /= 3
	
	while not num1 % 5 :
		array_num1.append(5)
		num1 /= 5
	
	while not num1 % 7 :
		array_num1.append(7)
		num1 /= 7

	while not num1 % 11 :
		array_num1.append(11)
		num1 /= 11
	
	while not num1 % 13 :
		array_num1.append(13)
		num1 /= 13

	return array_num1


def mcd(numero1, numero2):

	# Recogemos los arrays
	array1 = recursive_mcm(numero1)
	array2 = recursive_mcm(numero2)
	array = list()

	# Comprovar si existen y guarlalos
	for se in set(array1):
		try:
			list(array2).index(se, 0, len(array2))
			array.append(se)
		except ValueError:
			pass

	for se in set(array2):
		try:
			list(array1).index(se, 0, len(array1))
			array.append(se)
		except ValueError:
			pass

	# Calcular el total desde el array
	total = 1
	for num in array:
		total *= num

	return f"MCD({numero1}, {numero2}) es {total}"

def mcm(numero1, numero2):

	# Recogemos los multiplos
	array1 = recursive_mcm(numero1)
	array2 = recursive_mcm(numero2)

	# Pasar el array original a set(para numeros unicos)
	array1_set_original = set(array1)
	array2_set_original = set(array2)

	# Array para le numero de repeticiones de un numero
	array1_repeticiones = list()
	array2_repeticiones = list()
	
	# Inicializar total
	total = 1

	# Para el set de repeticiones
	for se in set(array1):
		array1_repeticiones.append(array1.count(se))

	for se in set(array2):
		array2_repeticiones.append(array2.count(se))


	# Juntar los arrays
	array_juntos = array1_set_original.union(array2_set_original)

	# Recorrer el array para comprovar numero de repeticiones y si existe y calcular
	for num in array_juntos:

		# Comprovar el indice dentro del "set(convertido a lista)"
		try:
			index_array1 = list(array1_set_original).index(num)
		except ValueError:
			index_array1 = None
		
		try:
			index_array2 = list(array2_set_original).index(num)
		except ValueError:
			index_array2 = None
			
		# Comrovar de que lado esta y mostrar el mayor por indice de repeticiones
		if index_array2 == None or index_array1 == None:
			if index_array2 == None and (index_array1 == 0 or index_array1):
				num_rep = array1_repeticiones[index_array1]
			elif index_array1 == None and (index_array2 == 0 or index_array2):
				num_rep = array2_repeticiones[index_array2]

		else:
			if array2_repeticiones[index_array2] > array1_repeticiones[index_array1]:
				num_rep = array2_repeticiones[index_array2]
			else: 
				num_rep = array1_repeticiones[index_array1]
		
		# Calcular el total (** == ^)
		total *= num ** num_rep

	return f"MCM({numero1}, {numero2}) es {total}"


# print(mcd(56, 180))
# print(mcm(56, 180))
print(mcd(56, 180))
print(mcm(56, 180))