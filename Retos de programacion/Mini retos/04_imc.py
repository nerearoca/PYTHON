"""
IMC
Crea una calculadora del índice de masa corporal.
"""

def calc_imc_kg_m(peso, estatura):
	imc = float(peso) / (float(estatura) * float(estatura))
	return imc

def calc_imc_kg_ft(peso, estatura):
	peso = peso / 0.45359237
	estatura_inch =  estatura * 12
	print(estatura)
	print(estatura_inch)
	imc = (float(peso) / (float(estatura_inch) * float(estatura_inch))) * 703
	return imc

def calc_imc_lbs_ft(peso, estatura):
	estatura_inch =  estatura * 12
	print(estatura)
	print(estatura_inch)
	imc = (float(peso) / (float(estatura_inch) * float(estatura_inch))) * 703
	return imc

def calc_imc_lbs_m(peso, estatura):
	peso = peso * 0.45359237
	imc = float(peso) / (float(estatura) * float(estatura))
	return imc


# print(calc_imc_kg_m(68, 1.65))
# print(calc_imc_lbs_ft(150, 5.5))
# print(calc_imc_kg_ft(68, 6))
# print(calc_imc_lbs_m(150, 1.70))

# Valores
genero = int(input("1)Mujer 2)Hombre "))
edad = int(input("Escriba su edad: "))

tipo_altura = int(input("Altura en: 1)Metros 2)Fts "))
altura =  float(input("Escriba su altura: "))

tipo_peso = int(input("Peso en: 1)Kg 2)Lbs "))
peso =  float(input("Escriba su peso: "))

# IMC
if tipo_altura == 1 and tipo_peso == 1 :
	imc = calc_imc_kg_m(peso, altura)
elif tipo_altura == 1 and tipo_peso == 2:	
	imc = calc_imc_lbs_m(peso, altura)
elif tipo_altura == 2 and tipo_peso == 2:
	imc = calc_imc_lbs_ft(peso, altura)
elif tipo_altura == 2 and tipo_peso == 1:
	imc = calc_imc_lbs_m(peso, altura)
else: 
	print("Error en algun parametro")

if edad < 19:
	
	if edad == 5:

		if genero == 1:

			if imc <= 11.8:
				print(f"Su imc es demasiado bajo: {imc}")
			elif imc >= 11.8 and imc <= 12.6:
				print(f"Su imc es bajo: {imc}")
			elif imc >= 12.7 and imc <= 16.9:
				print(f"Su imc es bueno: {imc}")
			elif imc >= 17.0 and imc <= 19.0:
				print(f"Su imc es alto(sobrepeso): {imc}")
			elif imc >= 19.6:
				print(f"Su imc es malo(obesidad): {imc}")
			
		elif genero == 2:

			if imc <= 12.1:
				print(f"Su imc es demasiado bajo: {imc}")
			elif imc >= 12.1 and imc <= 12.9:
				print(f"Su imc es bajo: {imc}")
			elif imc >= 13.0 and imc <= 16.7:
				print(f"Su imc es bueno: {imc}")
			elif imc >= 16.8 and imc <= 18.3:
				print(f"Su imc es alto(sobrepeso): {imc}")
			elif imc >= 18.4:
				print(f"Su imc es malo(obesidad): {imc}")

		else:
			print("Error en el genero")

	elif edad == 6:
		
		if genero == 1:

			if imc <= 11.7:
				print(f"Su imc es demasiado bajo: {imc}")
			elif imc >= 11.7 and imc <= 12.6:
				print(f"Su imc es bajo: {imc}")
			elif imc >= 12.7 and imc <= 17.1:
				print(f"Su imc es bueno: {imc}")
			elif imc >= 17.2 and imc <= 19.5:
				print(f"Su imc es alto(sobrepeso): {imc}")
			elif imc >= 19.6:
				print(f"Su imc es malo(obesidad): {imc}")
			
		elif genero == 2:

			if imc <= 12.2:
				print(f"Su imc es demasiado bajo: {imc}")
			elif imc >= 12.2 and imc <= 13:
				print(f"Su imc es bajo: {imc}")
			elif imc >= 13.1 and imc <= 16.9:
				print(f"Su imc es bueno: {imc}")
			elif imc >= 17.0 and imc <= 18.7:
				print(f"Su imc es alto(sobrepeso): {imc}")
			elif imc >= 18.8:
				print(f"Su imc es malo(obesidad): {imc}")

		else:
			print("Error en el genero")

	elif edad == 7:
		
		if genero == 1:

			if imc <= 11.8:
				print(f"Su imc es demasiado bajo: {imc}")
			elif imc >= 11.8 and imc <= 12.6:
				print(f"Su imc es bajo: {imc}")
			elif imc >= 12.7 and imc <= 16.9:
				print(f"Su imc es bueno: {imc}")
			elif imc >= 17.0 and imc <= 19.0:
				print(f"Su imc es alto(sobrepeso): {imc}")
			elif imc >= 29.6:
				print(f"Su imc es malo(obesidad): {imc}")
			
		elif genero == 2:

			if imc <= 12.3:
				print(f"Su imc es demasiado bajo: {imc}")
			elif imc >= 12.3 and imc <= 13.1:
				print(f"Su imc es bajo: {imc}")
			elif imc >= 13.2 and imc <= 17.0:
				print(f"Su imc es bueno: {imc}")
			elif imc >= 17.1 and imc <= 19.3:
				print(f"Su imc es alto(sobrepeso): {imc}")
			elif imc >= 19.4:
				print(f"Su imc es malo(obesidad): {imc}")

		else:
			print("Error en el genero")

	elif edad == 8:
		
		if genero == 1:

			if imc <= 12.0:
				print(f"Su imc es demasiado bajo: {imc}")
			elif imc >= 12.0 and imc <= 12.9:
				print(f"Su imc es bajo: {imc}")
			elif imc >= 12.9 and imc <= 18.0:
				print(f"Su imc es bueno: {imc}")
			elif imc >= 18.1 and imc <= 21.0:
				print(f"Su imc es alto(sobrepeso): {imc}")
			elif imc >= 21.0:
				print(f"Su imc es malo(obesidad): {imc}")
			
		elif genero == 2:

			if imc <= 12.5:
				print(f"Su imc es demasiado bajo: {imc}")
			elif imc >= 12.5 and imc <= 13.3:
				print(f"Su imc es bajo: {imc}")
			elif imc >= 13.4 and imc <= 17.7:
				print(f"Su imc es bueno: {imc}")
			elif imc >= 17.8 and imc <= 20:
				print(f"Su imc es alto(sobrepeso): {imc}")
			elif imc >= 20.1:
				print(f"Su imc es malo(obesidad): {imc}")

		else:
			print("Error en el genero")

	elif edad == 9:
		
		if genero == 1:

			if imc <= 12.2:
				print(f"Su imc es demasiado bajo: {imc}")
			elif imc >= 12.2 and imc <= 13.2:
				print(f"Su imc es bajo: {imc}")
			elif imc >= 13.3 and imc <= 18.7:
				print(f"Su imc es bueno: {imc}")
			elif imc >= 18.8 and imc <= 22.0:
				print(f"Su imc es alto(sobrepeso): {imc}")
			elif imc >= 22.1:
				print(f"Su imc es malo(obesidad): {imc}")
			
		elif genero == 2:

			if imc <= 12.7:
				print(f"Su imc es demasiado bajo: {imc}")
			elif imc >= 12.7 and imc <= 13.5:
				print(f"Su imc es bajo: {imc}")
			elif imc >= 13.6 and imc <= 18.6:
				print(f"Su imc es bueno: {imc}")
			elif imc >= 18.3 and imc <= 20.9:
				print(f"Su imc es alto(sobrepeso): {imc}")
			elif imc >= 21.0:
				print(f"Su imc es malo(obesidad): {imc}")

		else:
			print("Error en el genero")

	elif edad == 10:
		
		if genero == 1:

			if imc <= 12.5:
				print(f"Su imc es demasiado bajo: {imc}")
			elif imc >= 12.5 and imc <= 13.6:
				print(f"Su imc es bajo: {imc}")
			elif imc >= 13.7 and imc <= 19.4:
				print(f"Su imc es bueno: {imc}")
			elif imc >= 19.4 and imc <= 23.1:
				print(f"Su imc es alto(sobrepeso): {imc}")
			elif imc >= 23.2:
				print(f"Su imc es malo(obesidad): {imc}")
			
		elif genero == 2:

			if imc <= 12.9:
				print(f"Su imc es demasiado bajo: {imc}")
			elif imc >= 12.9 and imc <= 13.8:
				print(f"Su imc es bajo: {imc}")
			elif imc >= 13.9 and imc <= 18.8:
				print(f"Su imc es bueno: {imc}")
			elif imc >= 18.9 and imc <= 21.9:
				print(f"Su imc es alto(sobrepeso): {imc}")
			elif imc >= 22.0:
				print(f"Su imc es malo(obesidad): {imc}")

		else:
			print("Error en el genero")

	elif edad == 11:
		
		if genero == 1:

			if imc <= 12.9:
				print(f"Su imc es demasiado bajo: {imc}")
			elif imc >= 12.9 and imc <= 14.0:
				print(f"Su imc es bajo: {imc}")
			elif imc >= 14.1 and imc <= 20.3:
				print(f"Su imc es bueno: {imc}")
			elif imc >= 20.4 and imc <= 24.3:
				print(f"Su imc es alto(sobrepeso): {imc}")
			elif imc >= 24.4:
				print(f"Su imc es malo(obesidad): {imc}")
			
		elif genero == 2:

			if imc <= 13.2:
				print(f"Su imc es demasiado bajo: {imc}")
			elif imc >= 13.2 and imc <= 14.1:
				print(f"Su imc es bajo: {imc}")
			elif imc >= 14.2 and imc <= 19.5:
				print(f"Su imc es bueno: {imc}")
			elif imc >= 19.6 and imc <= 23.0:
				print(f"Su imc es alto(sobrepeso): {imc}")
			elif imc >= 23.1:
				print(f"Su imc es malo(obesidad): {imc}")

		else:
			print("Error en el genero")

	elif edad == 12:
		
		if genero == 1:

			if imc <= 13.4:
				print(f"Su imc es demasiado bajo: {imc}")
			elif imc >= 13.4 and imc <= 14.6:
				print(f"Su imc es bajo: {imc}")
			elif imc >= 14.7 and imc <= 11.3:
				print(f"Su imc es bueno: {imc}")
			elif imc >= 21.4 and imc <= 25.6:
				print(f"Su imc es alto(sobrepeso): {imc}")
			elif imc >= 25.7:
				print(f"Su imc es malo(obesidad): {imc}")
			
		elif genero == 2:

			if imc <= 13.6:
				print(f"Su imc es demasiado bajo: {imc}")
			elif imc >= 13.6 and imc <= 14.6:
				print(f"Su imc es bajo: {imc}")
			elif imc >= 14.7 and imc <= 20.4:
				print(f"Su imc es bueno: {imc}")
			elif imc >= 20.5 and imc <= 24.2:
				print(f"Su imc es alto(sobrepeso): {imc}")
			elif imc >= 24.3:
				print(f"Su imc es malo(obesidad): {imc}")

		else:
			print("Error en el genero")

	elif edad == 13:
		
		if genero == 1:

			if imc <= 13.8:
				print(f"Su imc es demasiado bajo: {imc}")
			elif imc >= 13.8 and imc <= 15.1:
				print(f"Su imc es bajo: {imc}")
			elif imc >= 15.2 and imc <= 22.3:
				print(f"Su imc es bueno: {imc}")
			elif imc >= 22.4 and imc <= 26.8:
				print(f"Su imc es alto(sobrepeso): {imc}")
			elif imc >= 26.9:
				print(f"Su imc es malo(obesidad): {imc}")
			
		elif genero == 2:

			if imc <= 14.0:
				print(f"Su imc es demasiado bajo: {imc}")
			elif imc >= 14.0 and imc <= 15.1:
				print(f"Su imc es bajo: {imc}")
			elif imc >= 15.2 and imc <= 21.3:
				print(f"Su imc es bueno: {imc}")
			elif imc >= 21.4 and imc <= 25.3:
				print(f"Su imc es alto(sobrepeso): {imc}")
			elif imc >= 25.4:
				print(f"Su imc es malo(obesidad): {imc}")

		else:
			print("Error en el genero")

	elif edad == 14:
		
		if genero == 1:

			if imc <= 14.2:
				print(f"Su imc es demasiado bajo: {imc}")
			elif imc >= 14.2 and imc <= 15.6:
				print(f"Su imc es bajo: {imc}")
			elif imc >= 15.7 and imc <= 23.2:
				print(f"Su imc es bueno: {imc}")
			elif imc >= 23.2 and imc <= 27.8:
				print(f"Su imc es alto(sobrepeso): {imc}")
			elif imc >= 27.9:
				print(f"Su imc es malo(obesidad): {imc}")
			
		elif genero == 2:

			if imc <= 14.5:
				print(f"Su imc es demasiado bajo: {imc}")
			elif imc >= 14.5 and imc <= 15.6:
				print(f"Su imc es bajo: {imc}")
			elif imc >= 15.7 and imc <= 22.2:
				print(f"Su imc es bueno: {imc}")
			elif imc >= 22.3 and imc <= 26.5:
				print(f"Su imc es alto(sobrepeso): {imc}")
			elif imc >= 26.6:
				print(f"Su imc es malo(obesidad): {imc}")

		else:
			print("Error en el genero")

	elif edad == 15:
		
		if genero == 1:

			if imc <= 14.5:
				print(f"Su imc es demasiado bajo: {imc}")
			elif imc >= 14.5 and imc <= 15.9:
				print(f"Su imc es bajo: {imc}")
			elif imc >= 16.0 and imc <= 23.8:
				print(f"Su imc es bueno: {imc}")
			elif imc >= 23.9 and imc <= 28.6:
				print(f"Su imc es alto(sobrepeso): {imc}")
			elif imc >= 28.7:
				print(f"Su imc es malo(obesidad): {imc}")
			
		elif genero == 2:

			if imc <= 14.9:
				print(f"Su imc es demasiado bajo: {imc}")
			elif imc >= 14.9 and imc <= 16.2:
				print(f"Su imc es bajo: {imc}")
			elif imc >= 16.3 and imc <= 23.1:
				print(f"Su imc es bueno: {imc}")
			elif imc >= 23.2 and imc <= 27.4:
				print(f"Su imc es alto(sobrepeso): {imc}")
			elif imc >= 27.5:
				print(f"Su imc es malo(obesidad): {imc}")

		else:
			print("Error en el genero")

	elif edad == 16:
		
		if genero == 1:

			if imc <= 14.7:
				print(f"Su imc es demasiado bajo: {imc}")
			elif imc >= 14.8 and imc <= 16.2:
				print(f"Su imc es bajo: {imc}")
			elif imc >= 16.3 and imc <= 24.3:
				print(f"Su imc es bueno: {imc}")
			elif imc >= 24.4 and imc <= 29.1:
				print(f"Su imc es alto(sobrepeso): {imc}")
			elif imc >= 29.2:
				print(f"Su imc es malo(obesidad): {imc}")
			
		elif genero == 2:

			if imc <= 15.3:
				print(f"Su imc es demasiado bajo: {imc}")
			elif imc >= 15.3 and imc <= 16.3:
				print(f"Su imc es bajo: {imc}")
			elif imc >= 16.4 and imc <= 23.9:
				print(f"Su imc es bueno: {imc}")
			elif imc >= 24.0 and imc <= 28.3:
				print(f"Su imc es alto(sobrepeso): {imc}")
			elif imc >= 28.4:
				print(f"Su imc es malo(obesidad): {imc}")

		else:
			print("Error en el genero")

	elif edad == 17:
		
		if genero == 1:

			if imc <= 14.7:
				print(f"Su imc es demasiado bajo: {imc}")
			elif imc >= 14.7 and imc <= 16.3:
				print(f"Su imc es bajo: {imc}")
			elif imc >= 16.4 and imc <= 24.6:
				print(f"Su imc es bueno: {imc}")
			elif imc >= 24.7 and imc <= 29.4:
				print(f"Su imc es alto(sobrepeso): {imc}")
			elif imc >= 29.5:
				print(f"Su imc es malo(obesidad): {imc}")
			
		elif genero == 2:

			if imc <= 15.6:
				print(f"Su imc es demasiado bajo: {imc}")
			elif imc >= 15.6 and imc <= 17.0:
				print(f"Su imc es bajo: {imc}")
			elif imc >= 17.1 and imc <= 24.6:
				print(f"Su imc es bueno: {imc}")
			elif imc >= 24.7 and imc <= 29.0:
				print(f"Su imc es alto(sobrepeso): {imc}")
			elif imc >= 29.1:
				print(f"Su imc es malo(obesidad): {imc}")

		else:
			print("Error en el genero")

	elif edad == 18:
		
		if genero == 1:

			if imc <= 14.7:
				print(f"Su imc es demasiado bajo: {imc}")
			elif imc >= 14.7 and imc <= 16.3:
				print(f"Su imc es bajo: {imc}")
			elif imc >= 16.4 and imc <= 24.8:
				print(f"Su imc es bueno: {imc}")
			elif imc >= 24.9 and imc <= 29.5:
				print(f"Su imc es alto(sobrepeso): {imc}")
			elif imc >= 29.6:
				print(f"Su imc es malo(obesidad): {imc}")
			
		elif genero == 2:

			if imc <= 15.7:
				print(f"Su imc es demasiado bajo: {imc}")
			elif imc >= 15.7 and imc <= 17.2:
				print(f"Su imc es bajo: {imc}")
			elif imc >= 17.3 and imc <= 24.9:
				print(f"Su imc es bueno: {imc}")
			elif imc >= 25.0 and imc <= 29.2:
				print(f"Su imc es alto(sobrepeso): {imc}")
			elif imc >= 29.3:
				print(f"Su imc es malo(obesidad): {imc}")

		else:
			print("Error en el genero")

else:
	if edad >= 19 and edad <= 24:

		if genero == 1:

			if imc >= 18.9 and imc <= 22.1:
				print(f"Su imc es optimo: {imc}")
			elif imc <= 25:
				print(f"Su imc es bueno: {imc}")
			elif imc >= 29.6:
				print(f"Su imc es malo(obesidad): {imc}")
			else:
				print(f"Su imc es bajo: {imc}")
			
		elif genero == 2:

			if imc >= 10.8 and imc <= 14.9:
				print(f"Su imc es optimo: {imc}")
			elif imc <= 19:
				print(f"Su imc es bueno: {imc}")
			elif imc >= 23.3:
				print(f"Su imc es malo(obesidad): {imc}")
			else:
				print(f"Su imc es bajo: {imc}")

		else:
			print("Error en el genero")

	elif edad >= 25 and edad <= 29:
		
		if genero == 1:

			if imc >= 18.9 and imc <= 22:
				print(f"Su imc es optimo: {imc}")
			elif imc <= 25.4:
				print(f"Su imc es bueno: {imc}")
			elif imc >= 29.8:
				print(f"Su imc es malo(obesidad): {imc}")
			else:
				print(f"Su imc es bajo: {imc}")

		elif genero == 2:
			if imc >= 12.8 and imc <= 16.5:
				print(f"Su imc es optimo: {imc}")
			elif imc <= 20.3:
				print(f"Su imc es bueno: {imc}")
			elif imc >= 24.4:
				print(f"Su imc es malo(obesidad): {imc}")
			else:
				print(f"Su imc es bajo: {imc}")

		else:
			print("Error en el genero")

	elif edad >= 30 and edad <= 34:
		
		if genero == 1:

			if imc >= 19.7 and imc <= 22.7:
				print(f"Su imc es optimo: {imc}")
			elif imc <= 26.4:
				print(f"Su imc es bueno: {imc}")
			elif imc >= 30.5:
				print(f"Su imc es malo(obesidad): {imc}")
			else:
				print(f"Su imc es bajo: {imc}")
			
		elif genero == 2:

			if imc >= 14.5 and imc <= 18:
				print(f"Su imc es optimo: {imc}")
			elif imc <= 21.5:
				print(f"Su imc es bueno: {imc}")
			elif imc >= 25.2:
				print(f"Su imc es malo(obesidad): {imc}")
			else:
				print(f"Su imc es bajo: {imc}")

		else:
			print("Error en el genero")

	elif edad >= 35 and edad <= 39:
		
		if genero == 1:

			if imc >= 21 and imc <= 24:
				print(f"Su imc es optimo: {imc}")
			elif imc <= 27.7:
				print(f"Su imc es bueno: {imc}")
			elif imc >= 31.5:
				print(f"Su imc es malo(obesidad): {imc}")
			else:
				print(f"Su imc es bajo: {imc}")

		elif genero == 2:

			if imc >= 16.1 and imc <= 19.4:
				print(f"Su imc es optimo: {imc}")
			elif imc <= 22.6:
				print(f"Su imc es bueno: {imc}")
			elif imc >= 26.1:
				print(f"Su imc es malo(obesidad): {imc}")
			else:
				print(f"Su imc es bajo: {imc}")

		else:
			print("Error en el genero")

	elif edad >= 40 and edad <= 44:
		
		if genero == 1:

			if imc >= 22.6 and imc <= 25.6:
				print(f"Su imc es optimo: {imc}")
			elif imc <= 29.3:
				print(f"Su imc es bueno: {imc}")
			elif imc >= 32.8:
				print(f"Su imc es malo(obesidad): {imc}")
			else:
				print(f"Su imc es bajo: {imc}")

		elif genero == 2:

			if imc >= 17.5 and imc <= 20.5:
				print(f"Su imc es optimo: {imc}")
			elif imc <= 23.6:
				print(f"Su imc es bueno: {imc}")
			elif imc >= 26.9:
				print(f"Su imc es malo(obesidad): {imc}")
			else:
				print(f"Su imc es bajo: {imc}")

		else:
			print("Error en el genero")
			
	elif edad >= 45 and edad <= 49:
		
		if genero == 1:

			if imc >= 24.3 and imc <= 27.3:
				print(f"Su imc es optimo: {imc}")
			elif imc <= 30.9:
				print(f"Su imc es bueno: {imc}")
			elif imc >= 34.1:
				print(f"Su imc es malo(obesidad): {imc}")
			else:
				print(f"Su imc es bajo: {imc}")

		elif genero == 2:

			if imc >= 18.6 and imc <= 21.5:
				print(f"Su imc es optimo: {imc}")
			elif imc <= 24.5:
				print(f"Su imc es bueno: {imc}")
			elif imc >= 27.6:
				print(f"Su imc es malo(obesidad): {imc}")
			else:
				print(f"Su imc es bajo: {imc}")

		else:
			print("Error en el genero")

	elif edad >= 50 and edad <= 54:
		
		if genero == 1:

			if imc >= 26.6 and imc <= 29.7:
				print(f"Su imc es optimo: {imc}")
			elif imc <= 33.1:
				print(f"Su imc es bueno: {imc}")
			elif imc >= 36.2:
				print(f"Su imc es malo(obesidad): {imc}")
			else:
				print(f"Su imc es bajo: {imc}")

		elif genero == 2:

			if imc >= 19.8 and imc <= 22.7:
				print(f"Su imc es optimo: {imc}")
			elif imc <= 25.6:
				print(f"Su imc es bueno: {imc}")
			elif imc >= 28.7:
				print(f"Su imc es malo(obesidad): {imc}")
			else:
				print(f"Su imc es bajo: {imc}")

		else:
			print("Error en el genero")

	elif edad >= 55 and edad <= 59:
		if genero == 1:

			if imc >= 27.4 and imc <= 30.7:
				print(f"Su imc es optimo: {imc}")
			elif imc <= 34:
				print(f"Su imc es bueno: {imc}")
			elif imc >= 37.3:
				print(f"Su imc es malo(obesidad): {imc}")
			else:
				print(f"Su imc es bajo: {imc}")

		elif genero == 2:

			if imc >= 20.2 and imc <= 23.2:
				print(f"Su imc es optimo: {imc}")
			elif imc <= 26.2:
				print(f"Su imc es bueno: {imc}")
			elif imc >= 29.3:
				print(f"Su imc es malo(obesidad): {imc}")
			else:
				print(f"Su imc es bajo: {imc}")

		else:
			print("Error en el genero")

	elif edad >= 60:
		
		if genero == 1:

			if imc >= 27.6 and imc <= 31:
				print(f"Su imc es optimo: {imc}")
			elif imc <= 34.4:
				print(f"Su imc es bueno: {imc}")
			elif imc >= 38:
				print(f"Su imc es malo(obesidad): {imc}")
			else:
				print(f"Su imc es bajo: {imc}")

		elif genero == 2:

			if imc >= 20.3 and imc <= 23.5:
				print(f"Su imc es optimo: {imc}")
			elif imc <= 26.7:
				print(f"Su imc es bueno: {imc}")
			elif imc >= 29.8:
				print(f"Su imc es malo(obesidad): {imc}")
			else:
				print(f"Su imc es bajo: {imc}")

		else:
			print("Error en el genero")

	else: 
		print("Error en la edad")