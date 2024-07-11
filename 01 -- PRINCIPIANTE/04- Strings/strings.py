# STRINGS

my_string = "My string";
my_other_string = 'My other string';

print(len(my_string));
print(len(my_other_string));

# Concatenar string
print(my_string + my_other_string);
print(my_string + ' ' + my_other_string);

my_new_line_string = 'Este es un string \ncon salto de linea';
print(my_new_line_string);

my_new_tabulated_string = 'Este es un string \tcon tabulacion';
print(my_new_tabulated_string);

my_new_scaped_string = '\\Este es un string \ncon escapado';
print(my_new_scaped_string);

# Formateo 
name, surname, age = 'Brais', 'Moure', 30;
print("Mi nombre es {} {} y mi edad es {}" .format(name, surname, age));  # --> Formateo directo
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age)); # --> Formateo no directo, --> Comprueba que las variabels sean del tipo correcto, sino con variables, busca el 1º y 2º string y luego el 1º digito numerico

# Mala praxis
print("Mi nombre es " + name + " " + surname  + " y mi edad es " + str(age)); # --> NO USAR, LE CUESTA EN ESTE LENGUAJE --> y age tiene que ser con str(age)

print(f"Mi nombre es {name} {surname} y mi edad es {age}"); # Inferencia de datos --> Mejso manera mas visual si queremos que esten mas ordenados de manera mas segura, pero no hay la comprovacon de tipo


# DESEMPAQUETADO DE CARACTERES
language = 'python';
# a, b = language;   --> Esto da error
a, b, c, d, e, f = language;
print('a: ' + a);
print('b: ' + b);
print('c: ' + c);
print('d: ' + d);
print('e: ' + e);
print('f: ' + f);


# DIVISION
language_slice = language[1:3];  # Pilla de 1 i 3
print('language[1:3]: ' + language_slice);

language_slice = language[1:];  # Pilla todo de 1-x
print('language[1:]: ' + language_slice);

language_slice = language[-2];  # Pilla de detras posicion 2  (-2)
print('language[-2]: ' + language_slice);

language_slice = language[1:2:4];  #Solo recoge 2 --> evira caracteres
print('language[1:2:4]: ' + language_slice);

language_slice = language[0:6:4];  #Solo recoge 0 i 4 --> evira caracteres
print('language[0:6:4]: ' + language_slice);   # PQ FUNCIONA ESTO ??

# REVERSE
reversed_language = language[::-1];
print('language[::-1]: ' + reversed_language);

reversed_language = language[::-2];
print('language[::-2]: ' + reversed_language);

reversed_language = language[::1];
print('language[::1]: ' + reversed_language);

# Metodos o funciones
print('language.capitalize(): ', language.capitalize())  # pondra la 1ra letra en mayusculas
print('language.upper(): ', language.upper())  # Todo eb nmayuscula
print('language.count(): ', language.count('t'))  # Contara el numero de t's
print('language.isnumeric(): ', language.isnumeric())   # Comprovara si el string es un numero
print('"1".isnumeric(): ', '1'.isnumeric())  
print('language.lower(): ', language.lower())  # A munuscula
print('language.upper().isupper(): ', language.upper().isupper())  # Pondra a mayuscula y comprovara si es mayusculas
print('language.startswith("py"): ', language.startswith('py'))   
print('language.startswith("Py"): ', language.startswith('Py')) 