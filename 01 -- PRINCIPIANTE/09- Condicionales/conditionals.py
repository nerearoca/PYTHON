# CONDICIONALES
# Mas habituales, manera de estblecer flujos de ejecucuion de nuestro codigo, si algo se va a ejecutar o no

my_condition = False

# if my_condition == True: es lo mismo
if my_condition:
	print('Se ejecuta la condicion del 1r if')

my_condition = 5 * 5 * 5
if my_condition >= 10:
	print('Se ejecuta la condicion del 2o if')

if my_condition > 10 and my_condition < 20:
	print('Es mayor que 10 y menor que 20')
elif my_condition > 50:
	print('Es mayor a 50')
else:
	print('Es menor o igual a 10')

print('La ejecucion continua')


my_string = 'Mi cadena de texto'

if my_string:
	print('Mi cadena de texto no es vacia')

my_string = ''
if not my_string:
	print('La cadena de texto esta vacia')