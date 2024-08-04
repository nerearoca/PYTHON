"""
Crea una única función (importante que sólo sea una) que sea 
capaz de calcular y retornar el área de un polígono.
- La función recibirá por parámetro sólo UN polígono a la vez.
- Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
- Imprime el cálculo del área de un polígono de cada tipo.
"""

def area_poligono(poligono):
	if poligono == 'Triángulo':
		altura = input('Altura:')
		base = input('Base:')

		area = lambda altura, base: (int(altura) * int(base)) / 2
		print(area(altura, base))
		
	elif poligono == 'Cuadrado' or poligono == 'Rectángulo':
		altura = input('Altura:')
		base = input('Base:')

		area = lambda altura, base: (int(altura) * int(base))
		
		print(area(altura, base))

	else:
		print("None")

tipo_poligono = input('Tipo de poligono? 1)Triangulo 2)Cuadrado 3)Rectangulo 4)Otro')
if tipo_poligono:

	if int(tipo_poligono) == 1:
		poligono = 'Triángulo'
	elif int(tipo_poligono) == 2:
		poligono = 'Cuadrado'
	elif int(tipo_poligono) == 3:
		poligono = 'Rectángulo'
	else:
		poligono = 'Otro'

	area_poligono(poligono)