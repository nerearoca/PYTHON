"""
 Crea una función que ordene y retorne una matriz de números.
  - La función recibirá un listado (por ejemplo [2, 4, 6, 8, 9]) y un parámetro
    adicional "Asc" o "Desc" para indicar si debe ordenarse de menor a mayor
    o de mayor a menor.
  - No se pueden utilizar funciones propias del lenguaje que lo resuelvan
    automáticamente.
"""

def ordenarLista(lista, tipo):

	listaOrdenada = lista
	maxim = len(lista)
	
	if tipo == 'ASC':				# De menor a mayor
		index = 0

		for num in range(maxim):
			for j in range(num + 1, maxim):
				if listaOrdenada[num] > listaOrdenada[j]:
					listaOrdenada[num], listaOrdenada[j] = listaOrdenada[j], listaOrdenada[num]

	elif tipo == 'DESC':	#De mayor a menor

		for num in range(maxim):
			for j in range(num + 1, maxim):
				if listaOrdenada[num] < listaOrdenada[j]:
					listaOrdenada[num], listaOrdenada[j] = listaOrdenada[j], listaOrdenada[num]


	print(listaOrdenada)

ordenarLista([5,10,15,3,4], 'ASC')
ordenarLista([5,10,15,2,3], 'DESC')