"""
  Dado un array de enteros ordenado y sin repetidos,
  crea una función que calcule y retorne todos los que faltan entre
  el mayor y el menor.
  - Lanza un error si el array de entrada no es correcto.

"""

def diferencia_mayor_menor(array):
	if len(set(array)) == len(array):
		if sorted(array) == array or sorted(array, reverse=True) == array:
			
			# Devolver diferencia
			if array[0] < array[len(array) - 1]:
				return array[len(array) - 1] - array[0]
			else:
				return array[0]  -  array[len(array) - 1]
	
	# Errores
		else:
			return "El array de entrada no esta ordenado"
	else:
		return "El array tiene repeticiones"



print(diferencia_mayor_menor([1, 3, 5]))
print(diferencia_mayor_menor([5, 3, 1]))
print(diferencia_mayor_menor([5, 1]))
print(diferencia_mayor_menor([-5, 1]))
print(diferencia_mayor_menor([1, 3, 3, 5]))
print(diferencia_mayor_menor([5, 7, 1]))
print(diferencia_mayor_menor([10, 7, 7, 1]))