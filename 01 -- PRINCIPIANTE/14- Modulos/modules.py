# MODULES
# Codigo externo a nuestro codigo  -> Tipo lobreria

# def sum_two_value (first_number, second_number):
# 	print(first_number + second_number)

import module

# Hay que acceder al fichero y acceder como si fuera objeto
module.sumValue(5,3,3)
module.printValue(55)


# Se accede directamente en las funciones
from module import sumValue, printValue

sumValue(5,4,3)
printValue('Hola, Python')

# Import de modulos por defecto con python
import math

print(math.pi)
print(math.pow(2, 8))

# Import directo con nombre alias
from math import pi as PI_VALUE

print(PI_VALUE)