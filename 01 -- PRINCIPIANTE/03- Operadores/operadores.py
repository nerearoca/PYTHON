# OPERADORES ARITMETRICOS:

# Habitulaes
print('3 + 4:', 3+4);
print('3 - 4:', 3-4);
print('3 * 4:', 3*4);
print('3 / 4:', 3/4); 
print('10 % 4:', 10%4);  # El resto
print('10 % 3:', 10%3);
print('10 % 2:', 10%2);

# Operaciones no habituales en otros lenguages de programacion(pero habituales en python)
print('10 // 3:', 10//3);   # Aprox. a numero entero (resultado de la operacion en int y no float)  --> FLOOR DIVISION
print('10 ** 3:', 10**3);   # Calcular exponente  --> 10 ^ 3


print('Hola'+'Python');  # Las junta en un solo string sin espacio
# print('Hola'-'Python');  --> Da error, mo funciona, tampoco /
# print('Hola'+5); --> No se pueden concatenar en texto un int + string

print("2 ** 3 + 3 - 7 / 1 // 4:", 2 ** 3 + 3 - 7 / 1 // 4);  # Se pueden combinar todos los tipos de operadores entre numeros

# Se repite el numero de veeces que le digas en la multiplicacion
print('Hola ' * 5);
print('Hola ' * int(2 ** 3 + 3 - 7 / 1 // 4));

myfloat = 2.5 * 2;
print("Hola " * int(myfloat));



# OPERADORES COMPARATIVOS:

# Habituales:
# Numeros
print('3 > 4:',3 > 4);
print('3 < 4:',3 < 4);
print('3 >= 4:',3 >= 4);
print('3 <= 4:',3 <= 4);
print('3 == 4:',3 == 4);
print('3 != 4:',3 != 4);
print('3 > 4 == 2:',3 > 4 == 2);  # Se pueden juntar pero dificil de usar(atipico)

# Strings
print('Hola > Python:', 'Hola' > 'Python');
print('Hola < Python:', 'Hola' < 'Python');
print('Hola >= Python:', 'Hola' >= 'Python');
print('Hola <= Python:', 'Hola' <= 'Python');
print('Hola == Python:', 'Hola' == 'Python');
print('Hola != Python:', 'Hola' != 'Python');

print('Hola <= Hola:', 'Hola' <= 'Hola');
print('Hola == Hola:', 'Hola' == 'Hola');

print('Hola >= Bola:', 'Hola' >= 'Bola');
print('Hola == Bola:', 'Hola' == 'Bola');

print('Hola >= Zola:', 'Hola' >= 'Zola');  # Compruebacion de ordenacion alfabetica

print('aaa >= aaa:', 'aaa' >= 'aaa'); 
print('aaa >= AAA:', 'aaa' >= 'AAA');		# Ordenacion alfabetica de ascii
print('AAA >= aaa:', 'AAA' >= 'aaa');  
print('aaa >= aba:', 'aaa' >= 'aba'); 
print('len(aaa) >= len(aba):', len('aaa') >= len('aba')); 




# OPERADORES LOGICOS: Se escriben and o or en lugar de && ||

# Habituales
print('3 > 4 and "Hola" > "Python":', 3 > 4 and "Hola" > "Python");
print('3 > 4 or "Hola" > "Python":', 3 > 4 or "Hola" > "Python");

print('3 < 4 and "Hola" < "Python":', 3 < 4 and "Hola" < "Python");
print('3 < 4 or "Hola" > "Python":', 3 < 4 or "Hola" > "Python");

print('3 < 4 or ("Hola" > "Python" and 4 == 4):', 3 < 4 or ("Hola" > "Python" and 4 == 4));

print('3 > 4:', 3 > 4);
print('not(3 > 4):', not(3 > 4));