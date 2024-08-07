"""
 Crea un programa que comprueba si los paréntesis, llaves y corchetes
 de una expresión están equilibrados.
 - Equilibrado significa que estos delimitadores se abren y cieran
   en orden y de forma correcta.
 - Paréntesis, llaves y corchetes son igual de prioritarios.
   No hay uno más importante que otro.
 - Expresión balanceada: { [ a * ( c + d ) ] - 5 }
 - Expresión no balanceada: { a * ( c + d ) ] - 5 }
"""

import re

# Funcion para comprovar
def exprexion_equilibrada(expresion):

	# Variables inicializadas
	contador_abiertas, contador_cerradas = 0,0
	expresiones = ""

	for letra in expresion:
		if letra == '(' or letra == '[' or letra == '{' :
			contador_abiertas += 1
			expresiones += letra
		elif letra == ')' or letra == ']' or letra == '}':
			contador_cerradas += 1
			expresiones += letra

	# Reemplazar
	while len(re.findall(re.compile(r'\(\)'), expresiones)) or len(re.findall(re.compile(r'\[\]'), expresiones)) or len(re.findall(re.compile(r'\{\}'), expresiones)):
		if re.findall(re.compile(r'\(\)'), expresiones):
			expresiones = re.sub(re.compile(r'\(\)'), '', expresiones)
		if re.findall(re.compile(r'\[\]'), expresiones):
			expresiones = re.sub(re.compile(r'\[\]'), '', expresiones)
		if re.findall(re.compile(r'\{\}'), expresiones):
			expresiones = re.sub(re.compile(r'\{\}'), '', expresiones)

	if len(expresiones):
		return 'La expresion no es equilibrada'
	else:
		return 'La expresion es equilibrada'

print(exprexion_equilibrada("{ a * ( c + d ) ] - 5 }"))
print(exprexion_equilibrada("{ [ a * ( c + d ) ] - 5 }}"))
print(exprexion_equilibrada("{a + b [c] * (2x2)}}}}"))
print(exprexion_equilibrada("{ [ a * ( c + d ) ] - 5 }"))
print(exprexion_equilibrada("{ a * ( c + d ) ] - 5 }"))
print(exprexion_equilibrada("{a^4 + (((ax4)}"))
print(exprexion_equilibrada("{ ] a * ( c + d ) + ( 2 - 3 )[ - 5 }"))
print(exprexion_equilibrada("{{{{{{(}}}}}}"))
print(exprexion_equilibrada("(a"))
