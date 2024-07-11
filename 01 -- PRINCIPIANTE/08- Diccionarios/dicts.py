# Dictionaries

# Constructos
my_dict = dict()
my_other_dict = {}

# Mostrar tipos
print('type(my_dict)', type(my_dict))
print('type(my_other_dict)', type(my_other_dict))

# Estructura relacionals, estilo json, objeto
my_other_dict = {'Nombre': 'Brais', 'Apellido': 'Moure', 'Edad': 35, 1:'Python'}

my_dict = {
	'Nombre': 'Brais', 
	'Apellido': 'Moure', 
	'Edad': 35, 
	'Lenguajes': {'Python', 'Swift', 'Kotlin'},
	1: 1.77
}

print(my_other_dict)
print(my_dict)

print('len(my_other_dict):', len(my_other_dict))
print('len(my_dict):', len(my_dict))

# Acceder a sus valores 
print(my_dict['Nombre'])

# Edicion
my_dict['Nombre'] = 'Pedro'
print('my_dict:', my_dict)
print(my_dict[1])

# Añadir clave i dato al dict
my_dict['Calle'] = 'Calle MoureDev'
print('my_dict:', my_dict)

# Borrar dato del diccionario mediante la clave
del my_dict['Calle']
print('my_dict:', my_dict)

# Ver datos o comprovar si existen en el diccionario
print("'Moure' in my_dict:", 'Moure' in my_dict)
print("'Apellido' in my_dict:", 'Apellido' in my_dict)  # Busca por clave, no valor

my_dict_items = my_dict.items()
print(my_dict_items)
print(my_dict.keys())
print(my_dict.values())

my_list = ['Lenguajes', 1, 'Calle']

# Crea diccionario sin valores
my_new_dict = dict.fromkeys(my_list)
print(my_new_dict)
my_new_dict = dict.fromkeys(('Lenguajes', 1, 'Calle'))
print(my_new_dict)
my_new_dict = dict.fromkeys(my_dict)
print(my_new_dict)

# Se dan a todos las claves los mismos valores {'Brais', 'Moure'}
my_new_dict = dict.fromkeys(my_dict, 'Moure')
print(my_new_dict)

print(list(my_new_dict))
print(set(my_new_dict))
print(tuple(my_new_dict))

my_values = my_new_dict.values()
print(type(my_values))
print(list(my_values))

# Solo se puede pasar a lista
print(list(my_new_dict.values()))
# print(set(my_new_dict.values()))
# print(tuple(my_new_dict.values()))
print(dict.fromkeys(list(my_new_dict.values())).keys())
print(dict.fromkeys(list(my_values)))