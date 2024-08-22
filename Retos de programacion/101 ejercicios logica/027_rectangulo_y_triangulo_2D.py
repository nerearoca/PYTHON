"""
 Crea un programa que dibuje un cuadrado o un triángulo con asteriscos "*".
 - Indicaremos el tamaño del lado y si la figura a dibujar es una u otra.
 - EXTRA: ¿Eres capaz de dibujar más figuras?
"""


def drawPolygon(altura, tipo):
	espacio = 0
	
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
				anchoo = altura - alt
				for anc in range(1, anchoo + 1):
					ancho += " "
				for anc in range(0, alt * 2 - 1):
					ancho += '*'		
				print(ancho)

		elif tipo == 'diamond':	
			# print(int(altura / 2))

			for alt in range(1, altura + 1):	
				if alt <= int(altura / 2) + 1:
					ancho = ""
					anchoo = int(altura / 2) + 1 - alt
					for anc in range(1, anchoo + 1):
						ancho += " "
					for anc in range(0, alt * 2 - 1):
						ancho += '*'		
					print(ancho)
				else:
					ancho = ""
					anchoo = altura - alt + 1
					# print(anchoo)

					espacio += 1
					for anc in range(0, espacio):
						ancho += ' '		
					for anc in range(0, anchoo * 2 - 1):
						ancho += "*"
					# for anc in range(0, alt * 2 - 1):
						
						# ancho += ' '		
					# if anchoo < 1:
					# 	for anc in range(1, anchoo - 1):
					# 		ancho += " "
					# else:
					# 	for anc in range(1, anchoo * 2 + 1):
					# 		ancho += " "
					# for anc in range(0, anchoo * 2 - 1):
					# 	ancho += '*'	

					# for anc in range(0, alt * 2 - 1):		
					# 	ancho += '*'		
					print(ancho)



print("SQUARE: 4")
drawPolygon(4,"square")
print("\nTRIANGLE: 5")
drawPolygon(5,"triangle")
print("\nDIAMOND: 7")
drawPolygon(5,"diamond")