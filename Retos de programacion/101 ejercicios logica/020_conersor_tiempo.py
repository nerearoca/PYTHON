"""
Crea una función que reciba días, horas, minutos y segundos (como enteros)
y retorne su resultado en milisegundos.
"""

def calculo_milisegundos(dias, horas, minutos, segundos):
	if dias > 0 :
		horas += 24 * dias
	elif dias < 0:
		return 'Error en los dias'
	
	if horas > 0:
		minutos += 60 * horas
	elif horas < 0:
		return 'Error en las horas'

	print(minutos)
	if minutos > 0:
		segundos += 60 * minutos
	elif minutos < 0:
		return 'Error en los minutos'
	
	calculo = segundos * 1000

	return calculo


print(calculo_milisegundos(0, 0, 0, 10))
print(calculo_milisegundos(2, 5, -45, 10))
print(calculo_milisegundos(2000000000, 5, 45, 10))