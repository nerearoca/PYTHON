"""
 Crea un programa que calcule quien gana más partidas al piedra,
 papel, tijera.
  - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
  - La función recibe un listado que contiene pares, representando cada jugada.
  - El par puede contener combinaciones de "R" (piedra), "P" (papel)
    o "S" (tijera).
  - Ejemplo. Entrada: [("R","S"), ("S","R"), ("P","S")]. Resultado: "Player 2".
"""

def rock_paper_sissors(array):
	player1 = 0
	player2 = 0
	for partida in array:
		if partida[0] == "R" and partida[1] == 'P':
			player2 += 1
		elif partida[1] == "R" and partida[0] == 'P':
			player1 += 1
		elif partida[0] == "R" and partida[1] == 'S':
			player1 += 1
		elif partida[1] == "R" and partida[0] == 'S':
			player2 += 1
		elif partida[0] == 'P' and partida[1] == 'S':
			player2 += 1
		elif partida[1] == 'P' and partida[0] == 'S':
			player1 += 1
		else:
			pass
	if player1 == player2:
		return "Tie"
	elif player1 < player2:
		return "Player 2"
	else:
		return "Player 1"


print('rock_paper_sissors([("R", "R")]):',rock_paper_sissors([("R", "R")]))
print('rock_paper_sissors([("R", "S")]):',rock_paper_sissors([("R", "S")]))
print('rock_paper_sissors([("P", "S")]):',rock_paper_sissors([("P", "S")]))
print('rock_paper_sissors([("R", "R"), ("S", "S"), ("P", "P")]):',rock_paper_sissors([("R", "R"), ("S", "S"), ("P", "P")]))
print('rock_paper_sissors([("R", "S"), ("S", "P"), ("S", "R")]):',rock_paper_sissors([("R", "S"), ("S", "P"), ("S", "R")]))
print('rock_paper_sissors([("R", "P"), ("S", "R"), ("P", "S")]):',rock_paper_sissors([("R", "P"), ("S", "R"), ("P", "S")]))