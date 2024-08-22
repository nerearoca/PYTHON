"""
Crea una función que reciba un texto y muestre cada palabra en una línea,
formando un marco rectangular de asteriscos.
  - ¿Qué te parece el reto? Se vería así:
    **********
    * ¿Qué   *
    * te     *
    * parece *
    * el     *
    * reto?  *
    ********** 
"""

def marcoPalabras(palabras):
	lista_palabras = palabras.split(" ")
	print(lista_palabras)

	# Calcular la palabbra mas larga
	maximoPalabra = ""
	for palabra in lista_palabras:	
		if len(palabra) > len(maximoPalabra):
			maximoPalabra = palabra


	# Mostrar por pantalla con el marco
	marcoPalabras = ""
	for arterisco in range(0,len(maximoPalabra) + 4): 
		marcoPalabras += "*"   # El marco de arriba
	marcoPalabras += "\n"
	
	for palabra in lista_palabras: 
		marco = f"* {palabra}"  # El inicio con la palabra y el primer *
		
		while len(marco) < len(maximoPalabra) + 3: # Rellenar espacios
			marco += " "
		marco += "*\n"  #Añadir el ultimo * y un salto de linea

		# Pasar a string principal
		marcoPalabras += marco

	# Ultima linea con *(marco de abajo)
	for arterisco in range(0,len(maximoPalabra) + 4): 
		marcoPalabras += "*"
	print(marcoPalabras)



marcoPalabras('¿Qué te parece el reto?')