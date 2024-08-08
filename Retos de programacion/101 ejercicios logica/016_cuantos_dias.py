"""
Crea una función que calcule y retorne cuántos días hay entre dos cadenas
de texto que representen fechas.
- Una cadena de texto que representa una fecha tiene el formato "dd/MM/yyyy".
- La función recibirá dos String y retornará un Int.
- La diferencia en días será absoluta (no importa el orden de las fechas).
- Si una de las dos cadenas de texto no representa una fecha correcta se
  lanzará una excepción.
"""

def cuantos_dias(date1, date2):

	separated_day1, separated_day2 = date1.split('/'), date2.split('/')
	if len(separated_day1) > 1 and  len(separated_day2) > 1:
		if int(separated_day1[0]) > 31 or int(separated_day2[0]) > 31 or int(separated_day1[1]) > 12 or int(separated_day2[1]) > 12 or int(separated_day1[2]) > 9999 or int(separated_day2[2]) > 9999:
			if ((separated_day1[1] == 1 or separated_day1[1] == 3 or separated_day1[1] == 5 or separated_day1[1] == 7 or separated_day1[1] == 8 or separated_day1[1] ==10 or separated_day1[1] == 12) and separated_day1[0] > 31) or ((separated_day2[1] == 1 or separated_day2[1] == 3 or separated_day2[1] == 5 or separated_day2[1] == 7 or separated_day2[1] == 8 or separated_day2[1] == 10 or separated_day2[1] == 12) and separated_day2[0] > 31):
				return "Fecha incorrecta"
			elif ((separated_day1[1] == 4 or separated_day1[1] == 6 or separated_day1[1] == 9 or separated_day1[1] == 11) and separated_day1[0] > 30) or ((separated_day2[1] == 4 or separated_day2[1] == 6 or separated_day2[1] == 9 or separated_day2[1] == 11) and separated_day2[0] > 30):
				return "Fecha incorrecta"
			elif (separated_day1[1] == 4 and separated_day1[0] > 29) or (separated_day2[1] == 4 and separated_day2[0] > 29):
				return "Error en la fecha"
		else:
			
			if (separated_day1[2] > separated_day2[2]) or (separated_day1[2] == separated_day2[2] and separated_day1[1] >= separated_day2[1]) or (separated_day1[2] == separated_day2[2] and separated_day1[1] == separated_day2[1] and separated_day1[0] >= separated_day2[0]):
				comparar_dias = int(separated_day1[0]) - int(separated_day2[0])
				comparar_meses = int(separated_day1[1]) - int(separated_day2[1])
				comparar_años = int(separated_day1[2]) - int(separated_day2[2])
				
			elif (separated_day1[2] < separated_day2[2]) or (separated_day1[2] == separated_day2[2] and separated_day1[1] <= separated_day2[1]) or (separated_day1[2] == separated_day2[2] and separated_day1[1] == separated_day2[1] and separated_day1[0] <= separated_day2[0]):
				comparar_dias = int(separated_day2[0]) - int(separated_day1[0])
				comparar_meses = int(separated_day2[1]) - int(separated_day1[1])
				comparar_años = int(separated_day2[2]) - int(separated_day1[2])

			if comparar_meses < 0:
				comparar_meses = 12 + (comparar_meses)

			if comparar_dias < 0:
				comparar_dias = 30 + (comparar_dias)

			# print(comparar_dias, comparar_meses, comparar_años)

			# Calcular i sumar:
			total_dias = (365 * comparar_años) + (30 * comparar_meses) + comparar_dias
			
			return f"{total_dias} dias"
	else: 
		return 'Error en alguna de las fechas'
			

print('"30/11/2003", "29/10/2004" -->',cuantos_dias("30/11/2003", "29/10/2004"))

print('"18/05/2022", "29/05/2022" -->', cuantos_dias("18/05/2022", "29/05/2022"))
print('"mouredev", "29/04/2022" -->', cuantos_dias("mouredev", "29/04/2022"))
print('"18/5/2022", "29/04/2022" --> ', cuantos_dias("18/5/2022", "29/04/2022"))