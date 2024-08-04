# TIPOS DE ERROR


# SyntaxError  --> error de sintaxis en pythin
# print "¡Hola comunidad!"  #--> SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
print("¡Hola comunidad!")


# NameError  --> no definido la variable
# print(language)  #--> NameError: name 'language' is not defined3
language = 'Spanish'
print(language)


# IndexError
my_list = ["Python", "Swift", "Kotlin", "Dart", "JavaScript"]
print(my_list[0])
# print(my_list[5]) #--> IndexError: list index out of range


# ModuleNotFoundError
# import maths #--> ModuleNotFoundError: No module named 'maths'
import math


# AttributeError 
# print(math.PI) #--> AttributeError: module 'math' has no attribute 'PI'. Did you mean: 'pi'? 
print(math.pi)


# KeyError
my_dict = {'Nombre': 'Brais', 'Apellido': 'Moure', 'Edad': 35, 1:'Python'}
# print(my_dict[0])  #--> KeyError: 0
# print(my_dict['Apelido']) #--> KeyError: 'Apelido'
print(my_dict['Edad']) 


# TypeError
# print(my_list['Nombre'])  #--> TypeError: list indices must be integers or slices, not str
print(my_list[0])


# ImportError
# from math import PI  #--> ImportError: cannot import name 'PI' from 'math' (unknown location). Did you mean: 'pi'?
from math import pi
print(pi)


# ValueError
# my_int = int("10e") #--> ValueError: invalid literal for int() with base 10: '10e'
my_int = int("10")
print(my_int)  


# ZeroDivisionError
print(4/2)
# print(4/0)  #--> ZeroDivisionError: division by zero