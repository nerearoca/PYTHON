# FUNCIONES

def my_function (): 
	print('Esto es una función')

my_function ()

def sum_two_value (first_number, second_number):
	print(first_number + second_number)

sum_two_value(5, 7)
sum_two_value(54754, 71231)
sum_two_value("5", "7")
sum_two_value(1.4, 5.2)

def sum_two_values_with_return (first_number, second_number):
	my_sum = first_number + second_number
	return my_sum

my_result = sum_two_values_with_return(5, 7)
print(my_result)
# my_result = sum_two_value(5, 7)
# print(my_result)  Se puede guardar pero retorna None

def print_name (name, surname):
	print(f"{name} {surname}")

print_name('Brais', 'Moure')
print_name('Moure', 'Brais')
print_name(surname='Moure', name='Brais')  # Se puede reordenar los parametros, si se llaman por el nombre de la variable

# Parametros por defecto
def print_name_with_default (name, surname, alias = 'Sin alias'):
	print(f"{name} {surname} {alias}")

print_name_with_default('Brais', 'Moure', 'MoureDev')
print_name_with_default('Brais', 'Moure')

# Se pueden pasar tantos parametros como se quiera
def print_text(*text):
	# Como lista infinita, se puede recorer como tal
	for element in text:
		print(element)
	
print_text('Hola', 'Python', 'MoureDev')
print_text('Hola')

def print_upper_text(*texts):
	# Como lista infinita, se puede recorer como tal
	for text in texts:
		print(text.upper())
	
print_upper_text('Hola', 'Python', 'MoureDev')
print_upper_text('Hola')