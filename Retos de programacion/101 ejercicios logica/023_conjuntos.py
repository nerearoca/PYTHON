"""
 Crea una función que reciba dos array, un booleano y retorne un array.
 - Si el booleano es verdadero buscará y retornará los elementos comunes
   de los dos array.
 - Si el booleano es falso buscará y retornará los elementos no comunes
   de los dos array.
 - No se pueden utilizar operaciones del lenguaje que
   lo resuelvan directamente.
"""

def conjuntos(array1:list, array2:list, boolea):
	set1 = set(array1)
	set2 = set(array2)	
	array = list()
	if boolea:
		for se in set1:
			try:
				list(array2).index(se, 0, len(array2))
				array.append(se)
			except ValueError:
				pass
			
		for se in set2:
			try:
				list(array1).index(se, 0, len(array1))
				array.append(se)
			except ValueError:
				pass

		return set(array)
		# set3= set1.union(set2)
		# return set3
	else:
		for se in set1:
			try:
				list(array2).index(se, 0, len(array2))
			except ValueError:
				array.append(se)

		for se in set2:
			try:
				list(array1).index(se, 0, len(array1))
			except ValueError:
				array.append(se)
			# if not array2.index(se):
			# 	array.append(se)
		return set(array)


print(conjuntos([1, 2, 3, 3, 4], [2, 2, 3, 3, 3, 4, 6], True))
print(conjuntos([1, 2, 3, 3, 4], [2, 2, 3, 3, 3, 4, 6], False))