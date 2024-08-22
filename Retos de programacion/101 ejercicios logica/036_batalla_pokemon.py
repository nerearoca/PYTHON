"""
Crea un programa que calcule el daño de un ataque durante
una batalla Pokémon.
  - La fórmula será la siguiente: daño = 50 * (ataque / defensa) * efectividad
  - Efectividad: x2 (súper efectivo), x1 (neutral), x0.5 (no es muy efectivo)
  - Sólo hay 4 tipos de Pokémon: Agua, Fuego, Planta y Eléctrico 
    (buscar su efectividad)
  - El programa recibe los siguientes parámetros:
   	- Tipo del Pokémon atacante.
   	- Tipo del Pokémon defensor.
   	- Ataque: Entre 1 y 100.
   	- Defensa: Entre 1 y 100.
"""

def efectividad_ataque(tipo_atacante, tipo_defensor):
	if tipo_atacante == "Agua":
		if tipo_defensor == 'Agua':
			return 0.5
		elif tipo_defensor == 'Fuego':
			return 2
		elif tipo_defensor == 'Planta':
			return 0.5
		elif tipo_defensor == 'Electrico':
			return 1
	elif tipo_atacante == 'Fuego':
		if tipo_defensor == 'Agua':
			return 0.5
		elif tipo_defensor == 'Fuego':
			return 0.5
		elif tipo_defensor == 'Planta':
			return 2
		elif tipo_defensor == 'Electrico':
			return 1
	elif tipo_atacante == 'Planta':
		if tipo_defensor == 'Agua':
			return 2
		elif tipo_defensor == 'Fuego':
			return 0.5
		elif tipo_defensor == 'Planta':
			return 0.5
		elif tipo_defensor == 'Electrico':
			return 1
	elif tipo_atacante == 'Electrico':
		if tipo_defensor == 'Agua':
			return 2
		elif tipo_defensor == 'Fuego':
			return 1
		elif tipo_defensor == 'Planta':
			return 0.5
		elif tipo_defensor == 'Electrico':
			return 0.5

def batalla_pokemon(tipo_atacante, tipo_defensor,ataque, defensa):
	ataque_pos, defensa_pos = False, False
	if ataque > 0 and ataque < 100:
		ataque_pos = True
	else:
		return "El ataque no esta en el rango"
	
	if defensa > 0 and defensa < 100:
		defensa_pos = True
	else:
		return "La defensa no esta en el rango"
	
	if defensa_pos and ataque_pos:
		efectividad = efectividad_ataque(tipo_atacante, tipo_defensor)
		daño = 50 * (ataque / defensa) * efectividad
		return round(daño, 2)

print(batalla_pokemon("Agua", "Fuego", 50, 30))
print(batalla_pokemon("Agua", "Fuego", 101, -10))
print(batalla_pokemon("Fuego", "Agua", 50, 30))
print(batalla_pokemon("Fuego", "Fuego", 50, 30))
print(batalla_pokemon("Planta", "Electrico", 30, 50))