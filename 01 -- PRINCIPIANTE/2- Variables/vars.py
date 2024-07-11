# Trabajar con datos

# Variables por convencion se escriben en minusculas y con guion bajo
my_string_variable = 'My String Variable';
print(my_string_variable);

my_int_variable = 5;
print(my_int_variable);

my_int_to_string_variable = str(my_int_variable);  # Pasar int to string
print(my_int_to_string_variable);
print(type(my_int_to_string_variable));

my_boolean_variable = True;
print(my_boolean_variable);

# Dierentes argumentos para print
print(my_string_variable, my_int_variable);
print(type(print(my_string_variable, my_int_variable)));   # NoneType --> no es un tipo de dato(no es topo de dato es funcion de sistema)
# Juntar string predefinido con variables:
print('Este es el valor de:' , my_boolean_variable);


# ALFGUNAS FUNCIONES DEL SISTEMA :3
# TYPE --> Anteriormente --> tipo de dato

# LEN --> longitud del valor de la variable
print(len('My string'));  
print(len(my_int_to_string_variable));  


# Variables en una sola linea(se puede pero no es muy buena practica)
name, surname, alias, age = 'Bryce', 'Moure', 'MoureDev', 35;
print('Name:', name);
print('Surname:', surname);
print('Alias:', alias);
print('Age:', age);

print('Me llamo:', name, surname, ". Mi edad es:", age, '. Y mi alias es:', alias);

# INPUT: recoger datos por consola
'''
name = input('What is your first name: ');
age = input('How old are you? ');
print(name);
print(age); 
'''

# Cambiar tipo
name = 35;
age = 'Brice';

print(name, type(name));
print(age, type(age));

# Variables con tipo estatico(esto no funciona)
address: str = "Mi direccion";
print(address, type(address));
address = 15;
print(address, type(address));

# Forzar tipo en variable