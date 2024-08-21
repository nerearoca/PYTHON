"""
 Lee el fichero "Challenge21.txt" incluido en el proyecto, calcula su
 resultado e imprímelo.
  - El .txt se corresponde con las entradas de una calculadora.
  - Cada línea tendrá un número o una operación representada por un
    símbolo (alternando ambos).
  - Soporta números enteros y decimales.
  - Soporta las operaciones suma "+", resta "-", multiplicación "*"
    y división "/".
  - El resultado se muestra al finalizar la lectura de la última
    línea (si el .txt es correcto).
  - Si el formato del .txt no es correcto, se indicará que no se han
  podido resolver las operaciones.

  NO ENTENDI NI VERGAS XD
"""

import io

file_chall = open('Challenge21.txt', 'r')
string = file_chall.read()

# def calculadora(string):
	#   total = 0
	# 5+2-1*8-15+4/2
	# print(string.find('/').find('*'))
	# return total
	# first_lin = True

	# num = 0
	# for lin in string:
	# 	print(total)

	# 	if lin.isnumeric():
	# 		if first_lin:
	# 			total = float(lin)
	# 			first_lin = False
	
	# 		num1 = float(lin)
	# 	elif lin == '-':
	# 		total = total - num1
	# 	elif lin == '*':
	# 		total = num1 * num2
	# 	elif lin == '+':
	# 		total += num
	# 	elif lin == '/':
	# 		total /= num	
  # return total		
	# return total
    
    

# print(calculadora(string.replace('\n', "")))
# print(string.replace('\n', ""))
def calculate_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Remove any trailing newlines or spaces
        lines = [line.strip() for line in lines]

        # Validate format
        if len(lines) % 2 == 0:
            raise ValueError("Formato incorrecto en el archivo.")

        # Start with the first number
        result = float(lines[0])

        # Iterate over the operations and numbers
        for i in range(1, len(lines), 2):
            operation = lines[i]
            try:
                next_number = float(lines[i + 1])
            except ValueError:
                raise ValueError("Formato incorrecto en el archivo.")

            if operation == "+":
                result += next_number
            elif operation == "-":
                result -= next_number
            elif operation == "*":
                result *= next_number
            elif operation == "/":
                result /= next_number
            else:
                raise ValueError("Operación desconocida.")

        print(f"Resultado: {result}")
    except (FileNotFoundError, ValueError) as e:
        print("No se han podido resolver las operaciones:", e)

# Supongamos que el archivo se llama "Challenge21.txt"
calculate_from_file("Challenge21.txt")

