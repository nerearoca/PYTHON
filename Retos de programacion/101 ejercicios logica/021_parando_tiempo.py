"""
Crea una función que sume 2 números y retorne su resultado pasados
unos segundos.
 - Recibirá por parámetros los 2 números a sumar y los segundos que
  debe tardar en finalizar su ejecución.
 - Si el lenguaje lo soporta, deberá retornar el resultado de forma
  asíncrona, es decir, sin detener la ejecución del programa principal.
  Se podría ejecutar varias veces al mismo tiempo.
"""


import time
# time.sleep(segundos)
def sum_seg(num1, num2, segundos):
	time.sleep(segundos)
	return num1 + num2

print(sum_seg(5,4,2))
print(sum_seg(6,4,3))
print(sum_seg(7,4,1))