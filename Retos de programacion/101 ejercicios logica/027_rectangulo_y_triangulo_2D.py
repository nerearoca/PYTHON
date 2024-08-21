"""
 Crea un programa que dibuje un cuadrado o un triángulo con asteriscos "*".
 - Indicaremos el tamaño del lado y si la figura a dibujar es una u otra.
 - EXTRA: ¿Eres capaz de dibujar más figuras?
"""


def drawPolygon(altura, tipo):
	print(tipo)
	
	if altura > 1:
		if tipo == 'square':
			for alt in range(1, altura + 1):
				ancho = ""
				for anc in range(1, altura + 1):	
					ancho += '*'
				print(ancho)

		elif tipo == 'triangle':
			
			for alt in range(1, altura + 1):
				ancho = ""
				for anc in range(1, alt + 1):	
					ancho += '*'
				print(ancho)

		elif tipo == 'diamond':
			mitad = altura  / 2
			for alt in range(1, altura + 1):
				ancho = ""
				if alt < mitad:
					for anc in range(1, alt + 1):	
						ancho += '*'
				else:
					print('Hola')
				print(ancho)


# print("square")
# drawPolygon(10,"square")
# print("TRIANGLE")
# drawPolygon(15,"triangle")
drawPolygon(12,"diamond")