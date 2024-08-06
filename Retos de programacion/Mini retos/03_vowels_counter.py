"""
CONTADOR DE VOCALES
Crea un programa que cuente cuantas
vocales tiene una cadena de texto.
"""

import re

pattern = "[a|e|i|o|u|A|E|I|O|U]"

cadena = input('Introduzca el texto a comprovar: ')

vocales = re.findall(pattern, cadena)

print(len(vocales))