#  Regular expresions

# Para aprender y validar expresiones regulares: https://regex101.com

import re

my_string = "Esta es la leccion numero 7: Expresiones regulares"
my_other_string = "Esta no es la leccion numero 6: Manejo de ficheros"


# match + span
match = re.match("Esta es la leccion", my_string, re.I)
print(match)

start, end = match.span()
print(start, end)
print(my_string[start:end])

match = re.match("Esta es la leccion", my_other_string, re.I)
print(match)

if match:
	start, end = match.span()
	print(start, end)
	print(my_other_string[start:end])

# print(re.match("Esta es la leccion", my_string, re.I))
# print(re.match("Esta es la leccion", my_other_string))

# print(re.match("Expresiones regulares", my_string))  #--> Da none pq comprueba desde el inicio


# Search 

search = re.search("leccion", my_string, re.I)
print(search)
start, end = search.span()
print(start, end)


# Findall

my_string = "Esta es la leccion numero 7: Leccion llamada Expresiones regulares"

findall = re.findall("leccion", my_string, re.I)
print("Buscar todas las coincidencias --> ", findall)


# Split

my_string = "Esta es la leccion numero 7:\nLeccion llamada Expresiones regulares"
print("Dividir --> ", re.split("\n", my_string))

# sub --> sustituir

print("Sustituir --> ", re.sub('Expresiones', "expresiones", my_string))
# print("Sustituir 1  --> ", re.sub('leccion|Leccion', "LECCION", my_string))
print("Sustituir 1  --> ", re.sub('[l|L]eccion', "LECCION", my_string))

# Patterns
pattern = r"[lL]eccion" 					 			# Leccion
print(re.findall(pattern, my_string))

pattern = r"[lL]eccion|[eE]xpresiones"  # Leccion o expresiones
print(re.findall(pattern, my_string))

pattern = r"[0-9]" 		 									# Solo el numero
print(re.findall(pattern, my_string))
print(re.search(pattern, my_string))

pattern = r"\d" 			 									# Solo el numero
print(re.findall(pattern, my_string))

pattern = r"\D" 	 											# Todas las letras menos el numero
print(re.findall(pattern, my_string))

pattern = r"[l]." 											# Solo las palabra que empieza con l y su proxima letra
print(re.findall(pattern, my_string))

email = "mouredev@mouredev.com"
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z-.]+$"

print(re.match(pattern, email))
print(re.search(pattern, email))
print(re.findall(pattern, email))

email = "mouredev@mouredev"
print(re.findall(pattern, email))

email = "mouredev@mouredev."
print(re.findall(pattern, email))

email = "mouredev@mouredev.e"
print(re.findall(pattern, email))

pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z-.]+$"  # $ --> todo lo que aparece se tendra en cuenta
email = "mouredev@mouredev.com.mx"
print(re.findall(pattern, email))