# SETS
## De base un arrays 



# Definicion 
my_set = set()
my_other_set = {}  #Misma sintaxis que los diccionarios

print('type(my_set)', type(my_set))
print('type(my_other_set)', type(my_other_set))  # Inicialemnte es un dict

# Rellenar los sets
my_other_set = {35, 1.77, 'Brais', 'Moure'}  # Al dar los valores se cambia a set
print('type(my_other_set)', type(my_other_set))

print('len(my_other_set)', len(my_other_set))

# Comprovar si hay elementos y añadirlos
my_other_set.add('MoureDev')

# Set no es una estructura ordenada, por eso no se puede acceder a un elemento por indice
# print(my_other_set[0])  TypeError: 'set' object is not subscriptable
print('My_other set edited: ', my_other_set)

# No se repiten en los sets, no admite repetidos
my_other_set.add('MoureDev')
print('My_other set edited 2: ', my_other_set)

# Ver datos o comprovar si existen en el set
print("'Moure' in my_other_set:", 'Moure' in my_other_set)
print("'Mouri' in my_other_set:", 'Mouri' in my_other_set)

# Borrar en set
my_other_set.remove('Moure')
print('my_other_set con Moure eliminado:', my_other_set)

# Borrar de la variable los datos, no la variable
my_other_set.clear()
print(my_other_set)
print(len(my_other_set))

del my_other_set
# print(my_other_set)  NameError: name 'my_other_set' is not defined


# Hacer las transformaciones es peligroso pq no se sabe en que posicion hay cada cosa
my_set = {35, 1.77, 'Brais', 'Moure'}
my_list = list(my_set)

print(my_list[0], my_set)

my_other_set = {'Kotlin', 'Swift', 'Python'}

# Unir sets
my_new_set = my_set.union(my_other_set)
print(my_new_set)

# Unions, no se aaden repetidos, y el nuevo union no se añade en la variable, pq esta en el print
print(my_new_set.union(my_new_set).union(my_set).union({'JavaScript', 'C#'}))

print(my_new_set.difference(my_set))