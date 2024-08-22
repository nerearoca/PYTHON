""" 
 Crea una función que imprima los 30 próximos años bisiestos
  siguientes a uno dado.
  - Utiliza el menor número de líneas para resolver el ejercicio.
"""
from datetime import datetime


def añosbisiestos():
	# este_año = datetime.now().year
	este_año = 2025
	año_bisiesto = 0
	if not (este_año % 4 and (este_año % 100 or not este_año % 400)):
		año_bisiesto = este_año
		
	else:
		for plus in range(1, 4):
			año_bis = este_año + plus
			if not (año_bis % 4 and (año_bis % 100 or not año_bis % 400)):
				año_bisiesto = este_año + plus

	for año in range(año_bisiesto, año_bisiesto + 4*30, 4):				
		print(año)

añosbisiestos()	
