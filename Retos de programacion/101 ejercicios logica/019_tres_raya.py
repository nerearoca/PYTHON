"""
/*
 Crea una función que analice una matriz 3x3 cOmpuesta pOr "X" y "O"
 y retOrne lO siguiente:
 - "X" si han ganadO las "X"
 - "O" si han ganadO lOs "O"
 - "Empate" si ha habidO un empate
 - "NulO" si la prOpOrción de "X", de "O", O de la matriz nO es cOrrecta.
   O si han ganadO lOs 2.
NOta: La matriz puede nO estar tOtalmente cubierta.
Se pOdría representar cOn un vacíO "", pOr ejemplO.

"""

def tres_raya(tablero):
	ganaX, ganaO = False, False


	for tab1 in tablero:
		# Horizontales

		print(tab1)
		if tab1[0] =='X' and tab1[1] =='X' and tab1[2] =='X':
			ganaX = True
		elif tab1[0] =='O' and tab1[1] =='O' and tab1[2] =='O':
			ganaO = True
		
	tab1 = tablero[0]
	tab2 = tablero[1]
	tab3 = tablero[2]

	# Verticales
	if (tab1[0] == 'X' and tab2[0] == 'X' and tab3[0] == 'X') or  (tab1[1] == 'X' and tab2[1] == 'X' and tab3[1] == 'X') or (tab1[2] == 'X' and tab2[2] == 'X' and tab3[2] == 'X'):
		ganaX = True
	elif (tab1[0] == 'O' and tab2[0] == 'O' and tab3[0] == 'O') or  (tab1[1] == 'O' and tab2[1] == 'O' and tab3[1] == 'O') or (tab1[2] == 'O' and tab2[2] == 'O' and tab3[2] == 'O'):
		ganaO = True
	
	# diagonales
	if (tab1[0] == 'X' and tab2[1] == 'X' and tab3[2] == 'X') or (tab3[0] == 'X' and tab2[1] == 'X' and tab1[2] == 'X') :
		ganaX = True
	elif (tab1[0] == 'O' and tab2[1] == 'O' and tab3[2] == 'O') or (tab3[0] == 'O' and tab2[1] == 'O' and tab1[2] == 'O'):
		ganaO = True
	
	# RETURNS
	if ganaX and ganaO:
		return 'EMPATE'
	elif ganaO:
		return 'O'
	elif ganaX:
		return 'X'
	else: 
		return 'NULO'

print(tres_raya([["X", "O", "X"],
									["O", "X", "O"],
									["O", "O", "X"]]))

print(tres_raya([["", "O", "X"],
								["", "X", "O"],
								["", "O", "X"]]))

print(tres_raya([["O", "O", "O"],
								["O", "X", "X"],
								["O", "X", "X"]]))

print(tres_raya([["X", "O", "X"],
								["X", "X", "O"],
								["X", "X", "X"]]))

print(tres_raya([["X", "O", "X"],
								["X", "O", "O"],
								["X", "O", "X"]]))