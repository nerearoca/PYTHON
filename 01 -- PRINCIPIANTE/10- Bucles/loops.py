# LOOPS

#  WHILE --> Mientras sea true, se ejecuta

my_condition = 0

while my_condition < 10:
	print(my_condition)
	my_condition += 2
else:  # Es opcional
	print('La condicion es mayor o igual que 10')

print('La ejecución continua')

while my_condition < 20:
	my_condition += 1 
	if(my_condition == 15): 
		print('Se detiene la ejecucion')
		break

	print(my_condition)

print('La ejecución continua')

# FOR

my_list = [35, 24, 63, 52, 30, 30, 17]

for element in my_list:
	print(element)

my_set = {35, 1.77, 'Brais', 'Moure'}  # Al dar los valores se cambia a set

for element in my_set:
	print(element)

my_tuple = (35, 1.77, 'Brais', 'Moure')

for element in my_tuple:
	print(element)

my_dict = {
	'Nombre': 'Brais', 
	'Apellido': 'Moure', 
	'Edad': 35, 
	'Lenguajes': {'Python', 'Swift', 'Kotlin'},
	1: 1.77
}

for element in my_dict:
	print(element)
	if(element == 'Edad'):
		continue  # Es como un break, deteniendo la ejecucuin en ese punto y contuniando con el proximo valor
	elif element == 1:
		print('Element vale 1')
	print('Se ejecuta')
else:
	print('El bucle for para diccionario ha finalizado')


