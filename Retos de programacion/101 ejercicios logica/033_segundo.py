""" 
Dado un listado de números, encuentra el SEGUNDO más grande
"""

def segundoMayor(listadoNumeros):
	listado = sorted(listadoNumeros)

	print(listado[-2])

segundoMayor([5,4,3,6,8])