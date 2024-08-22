"""
Crea un función, que dado un año, indique el elemento 
y animal correspondiente en el ciclo sexagenario del zodíaco chino.
  - Info: https://www.travelchinaguide.com/intro/astrology/60year-cycle.htm
  - El ciclo sexagenario se corresponde con la combinación de los elementos
    madera, fuego, tierra, metal, agua y los animales rata, buey, tigre,
    conejo, dragón, serpiente, caballo, oveja, mono, gallo, perro, cerdo
    (en este orden).
  - Cada elemento se repite dos años seguidos.
  - El último ciclo sexagenario comenzó en 1984 (Madera Rata).
"""

def animal_zodiac(año):
	animales = ["Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Sheep", "Monkey", "Rooster", "Dog", "Pig"]

	number = (año - 4) % len(animales)
	return (animales[number])


def wu_ching(año):
	signo = ["Wood", "Wood", "Fire", "Fire", "Earth", "Earth", "Metal", "Metal", "Water", "Water"]

	number = (año - 4) % len(signo)
	return (signo[number])


def calcular_signo_y_elemento(year):
	print(f"The element for the year {year} is {wu_ching(year)}, and the animal is {animal_zodiac(year)}")

calcular_signo_y_elemento(2024)
calcular_signo_y_elemento(2025)

