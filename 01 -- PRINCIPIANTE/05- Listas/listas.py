# LISTAS --> un array

my_list = list()
my_other_list = []

print(len(my_list)) 

# Añadir info
my_list = [35, 24, 62, 52, 30, 30, 17]
print('my_list: ', my_list)
print('len(my_list): ', len(my_list))

my_other_list = [35, 1.77, 'Brais', 'Moure']
print('my_other_list: ', my_other_list)
print('len(my_other_list): ', len(my_other_list))  # Longuitud de la lista
print('type(my_other_list): ', type(my_other_list))  # Tipo de variable --> <class 'list'>

print('my_other_list[0]: ', my_other_list[0])
print('my_other_list[1]: ', my_other_list[1])
print('my_other_list[-1]: ', my_other_list[-1])  # Es facil que pueda dar error
# print('my_other_list[-5]: ', my_other_list[-5])   # Error pq no esta en el rango
# print('my_other_list[4]]: ', my_other_list[4])   # Error pq no esta en el rango

print('my_other_list[len(my_other_list)-1] ', my_other_list[len(my_other_list)-1])  
print('my_list.count(30):', my_list.count(30))  # Devuelve el numero de veces que se repite el valor(30)

# Desenpaquetar en variables una lista
age, height, name, surname = my_other_list
print('Age:', age)
print('Name: ' + name)

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print('Age:', age)
print('Name: ' + name)

print(my_list + my_other_list)  # Union de listas

# Añadir datos
my_other_list.append('MoureDev')  # --> Añade al final
my_other_list.insert(1, 'Rojo')   # --> Se añade en la posicion indicada
print('My other list inserted:', my_other_list)

my_other_list[1] = 'Azul'
print('My other list edited:', my_other_list)

# Borrar datos
my_other_list.remove('Azul')   # Borra el 1r valor indique que sea igual al indicado
my_list.remove(30) 

print(my_other_list.pop())    # Borra el ultimo valor de la lista pero lo devuelve
print(my_other_list.pop(2))   # Borra del indice especificado

my_pop_element = my_list.pop(2)
print(my_pop_element)

# Eliminar por indice
print('My list:', my_list)
del my_list[2]
print('My list deleted:', my_list)

# Copiar lista
my_new_list = my_list.copy()

# Borrar toda la lista(resetearla a vacio)
my_list.clear()  
print('My list cleared: ',my_list)
print('My new list: ',my_new_list)

# Girar la lista, se tiene que llamar antes de mostrar por pantalla, sino no se muestra
my_new_list.reverse()
print('My new list reversed: ', my_new_list)

# Ordenacion de menor a menor o de orden alfabetico de la lista
my_new_list.sort()
print('My new list sorted: ', my_new_list)

# Sublistas
print('My new list sorted pero con sub [1:2]: ', my_new_list[1:2])
print('My new list sorted pero con sub [1:3]: ', my_new_list[1:3])

# CAMBIAR TIPO
my_list = 'Hola Python'
print(my_list, type(my_list))