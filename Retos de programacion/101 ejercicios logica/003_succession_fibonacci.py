"""
Escribe un programa que imprima los 50 primeros números de la sucesión
de Fibonacci empezando en 0.
- La serie Fibonacci se compone por una sucesión de números en
  la que el siguiente siempre es la suma de los dos anteriores.
  0, 1, 1, 2, 3, 5, 8, 13...

"""

# ESTA MAL AQUI
# lista_numero = [0,1]
# def succession_fibonacci(numero_anterior, numero_actual):
# 	nuevo_numero = numero_anterior + numero_actual
# 	print(nuevo_numero)
# 	return nuevo_numero
	
# numero_actual, nuevo_numero = 0,1
# while(len(lista_numero) != 50):
	
# 	nuevo_numero = succession_fibonacci(numero_actual, nuevo_numero)
# 	lista_numero.append(nuevo_numero)

# print(lista_numero)

def fibonacci():
	  
  nPrev, nNext = 0, 1

  for index in range(0, 50):
    # print('Index:', index)
    print(nPrev)
    
    fib = nPrev + nNext
    nPrev = nNext
    nNext = fib		

fibonacci()