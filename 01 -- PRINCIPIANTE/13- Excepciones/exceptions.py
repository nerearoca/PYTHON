# EXCEPCIONS HANDLING
numberOne, numberTwo = 5, 1
numberTwo = '1'
error = False

try:
	print(numberOne + numberTwo)
except:  # Si se produce uma excepcion
	print('Error en el resultado')
	error = True
else:  # Si todo funciona correctamente se mostrara los 2 fresultados(el de try i el del else) OPCIONAL
	print('Se ejecuto correctamente')
	error = False
finally:  # Se ejecutara de cualquier forma OPCIONAL
	print('Se finalizo la ejecucion')

if error:
	print('Todo mal')
else:
	print('Todo correcto')

# Excepciones por tipo
try:
	print(numberOne + numberTwo)
except TypeError:
	print('Error en el TypeError')
except ValueError:
	print('Error en el ValueError')

# Captura de la informacion basica
try:
	print(numberOne + numberTwo)
except ValueError as error:  # Capturar la excepcion y donde
	print(error)
except Exception as error:  # Sea cual sea el error sera capturado
	print(error)
