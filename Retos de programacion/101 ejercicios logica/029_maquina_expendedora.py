"""
Simula el funcionamiento de una máquina expendedora creando una operación
que reciba dinero (array de monedas) y un número que indique la selección
del producto.
  - El programa retornará el nombre del producto y un array con el dinero
    de vuelta (con el menor número de monedas).
  - Si el dinero es insuficiente o el número de producto no existe,
    deberá indicarse con un mensaje y retornar todas las monedas.
  - Si no hay dinero de vuelta, el array se retornará vacío.
  - Para que resulte más simple, trabajaremos en céntimos con monedas
    de 5, 10, 50, 100 y 200.
  - Debemos controlar que las monedas enviadas estén dentro de las soportadas.
"""

def productosMaquinaExpendedora(producto):

	productos = {
		1: ["Coca-Cola", 350],
		2: ["Fanta Limon", 250],
		3: ["Fanta Naranja", 250],
		4: ["Nestea", 125],
		5: ["Cerveza Estrella Damm", 400],
		6: ["Mars", 250],
		7: ["Pipas", 125],
		8: ["Cheetos", 150]
	}

	if producto <= len(productos):
		return productos[producto]
	else:
		return "El producto seleccionado no existe"
	

def maquinaExpendedora(arrayMonedas, numPoroducto):
	if len(productosMaquinaExpendedora(numPoroducto)) == 2:
		product, price = productosMaquinaExpendedora(numPoroducto)
		calculoMonedas = 0
		for moneda in arrayMonedas:
			calculoMonedas += moneda
		
		# Lo que devuelve
		if calculoMonedas < price:
			print('Faltan monedas')
		elif calculoMonedas == price:
			print(f'Su producto es {product}, su precio es {price}')
		else:
			precio = calculoMonedas - price
			retorno = list()

			# Calcular el retorno
			while precio > 0:
				# 5, 10, 50, 100 y 200.
				if precio >= 200:
					retorno.append(200)
					precio -= 200
				elif precio >= 100:
					retorno.append(100)
					precio -= 100
				elif precio >= 50:
					retorno.append(50)
					precio -= 50
				elif precio >= 20:
					retorno.append(20)
					precio -= 20
				elif precio >= 10:
					retorno.append(10)
					precio -= 10
				elif precio >= 5:
					retorno.append(5)
					precio -= 5

			# print(retorno)
			# print(precio)
			print(f'Su producto es {product}, su precio es {price}, su vuelta es {retorno}')
		# print(calculoMonedas)
	else:
		print(productosMaquinaExpendedora(numPoroducto),arrayMonedas)


maquinaExpendedora([5,20,100, 200], 4) 
maquinaExpendedora([5,20,100, 200], 10) 
maquinaExpendedora([5,20,100, 200, 100, 20, 10], 7) 