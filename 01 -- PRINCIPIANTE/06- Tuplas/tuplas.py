# TUPLAS
# !!!!! Las tuplas son en constantes, no se pueden editar ni cambiar ni añadir

# Definicion
my_tuple = tuple()
my_other_tuple = ()

# Definicion de datos a la tupla
my_tuple = (35, 1.77, 'Brais', 'Moure')
my_other_tuple = (35, 24, 62, 52, 30, 30, 17)
print(my_tuple)
print(type(my_tuple))

# Mostrar datos
print('My_tuple[0]', my_tuple[0])
print('My_tuple[-1]', my_tuple[-1])
# print('my_other_list[4]: ', my_other_list[4])   # Error pq no esta en el rango
# print('my_other_list[-6]]: ', my_other_list[-6])   # Error pq no esta en el rango

print('My_tuple count("Brais"):', my_tuple.count('Brais'))
print('My_tuple index("Moure"):', my_tuple.index('Moure'))
print('My_tuple index("Brais"):', my_tuple.index('Brais'))

# my_tuple[1] = 1.80;
# print(my_tuple)

print('Sumar las tuplas:', my_tuple + my_other_tuple)
my_sum_tuple = my_tuple + my_other_tuple
print('Sumar las tuplas en una variable:', my_sum_tuple)

# Acceder a sus sub
print('My_sum tupe[3:6]: ', my_sum_tuple[3:6])

# Pasar tupla a lista
my_tuple = list(my_tuple) 
print('type(my_tuple): ', type(my_tuple))
print('My_tuple:', my_tuple)

my_tuple[3] = 'MoureDev'
my_tuple.insert(1, 'Azul')
print('My_tuple editada:', my_tuple)

# Pasar lista a tupla
my_tuple = tuple(my_tuple)
print('type(my_tuple): ', type(my_tuple))
print('My_tuple:', my_tuple)

# Borrar la tupla(la variable, no el contenido)

# del my_tuple[3]   TypeError: 'tuple' object doesn't support item deletion
del my_tuple
# print(my_tuple)  NameError: name 'my_tuple' is not defined