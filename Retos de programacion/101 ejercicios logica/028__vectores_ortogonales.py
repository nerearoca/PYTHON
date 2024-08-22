"""
 Crea un programa que determine si dos vectores son ortogonales.
 - Los dos array deben tener la misma longitud.
 - Cada vector se podría representar como un array. Ejemplo: [1, -2]
"""

def esOctogonal(vector1, vector2):
	if len(vector1) == len(vector2):
		index = 0
		sumas = []
		for vec in vector1:
			sumas.append(vec * vector2[index])

			index += 1

		total = 0
		for suma in sumas:
			total += suma

		if not total:
			print('Es octogonal')
		else:
			print('NO es octogonal')
		
	else:
		print('NO es octogonal')


esOctogonal([3,4], [-4, 3])   # SI
esOctogonal([1,2], [2, 1])# NO
esOctogonal([1,-2,3], [4,2,-1]) # NO
esOctogonal([2, -3, 1], [3,2,5])# NO
esOctogonal([1,2,3], [4,-8,4])# SI