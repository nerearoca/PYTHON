"""
Crea una función que evalúe si un/a atleta ha superado correctamente una
 carrera de obstáculos.
	- La función recibirá dos parámetros:
		- Un array que sólo puede contener String con las palabras
			"run" o "jump"
		- Un String que represente la pista y sólo puede contener "_" (suelo)
				o "|" (valla)
	- La función imprimirá cómo ha finalizado la carrera:
		- Si el/a atleta hace "run" en "_" (suelo) y "jump" en "|" (valla)
				será correcto y no variará el símbolo de esa parte de la pista.
		- Si hace "jump" en "_" (suelo), se variará la pista por "x".
		- Si hace "run" en "|" (valla), se variará la pista por "/".
	- La función retornará un Boolean que indique si ha superado la carrera.
 Para ello tiene que realizar la opción correcta en cada tramo de la pista.
"""

def carrera_superada(estados, pista):
	# print(estados)
	index = 0
	contador = 0


	for pist in pista:
		if(len(estados) >= len(pista)):
			if(pist == '_' and estados[index] == 'run'):
				contador += 1
			elif (pist == '|' and estados[index] == 'run'):
				pista[index] == '/'
			elif (pist == '|' and estados[index] == 'jump'):
				contador += 1
			elif (pist == '_' and estados[index] == 'jump'):
				pista[index] == 'x'
		index += 1

	# print(contador)
	if(contador == len(pista)):
		return True
	else:
		return False
	# print(pista)
	# return 'Ha ganado'

"""
println(checkRace(listOf(AthleteState.RUN, 'jump', AthleteState.RUN, 'jump', AthleteState.RUN, 'jump', AthleteState.RUN), "_|_|_"))
println(checkRace(listOf('jump', 'jump', 'jump', 'jump', 'jump'), "|||||"))
println(checkRace(listOf('jump', 'jump', 'jump', 'jump', 'jump'), "||?||"))
}
"""
print("['run', 'jump', 'run', 'jump', 'run'], '_|_|_' -->", carrera_superada(['run', 'jump', 'run', 'jump', 'run'], '_|_|_'))
print("['run', 'run', 'jump', 'jump', 'run'], '_|_|_' -->", carrera_superada(['run', 'run', 'jump', 'jump', 'run'], '_|_|_'))
print("['run', 'run', 'run', 'jump', 'run'], '_|_|_' -->", carrera_superada(['run', 'run', 'run', 'jump', 'run'], '_|_|_'))
print("['run', 'run', 'jump', 'jump', 'run'], '_|_|_|_' -->", carrera_superada(['run', 'run', 'jump', 'jump', 'run'], '_|_|_|_'))
print("['run', 'jump', 'run', 'jump'], '_|_|_' -->", carrera_superada(['run', 'jump', 'run', 'jump'], '_|_|_'))
print("['run', 'jump', 'run', 'jump', 'run', 'jump', 'run'], '_|_|_' -->", carrera_superada(['run', 'jump', 'run', 'jump', 'run', 'jump', 'run'], '_|_|_'))
print("['jump', 'jump', 'jump', 'jump', 'jump'],'|||||'", carrera_superada(['jump', 'jump', 'jump', 'jump', 'jump'],'|||||'))
print("['jump', 'jump', 'jump', 'jump', 'jump'], '||?||'", carrera_superada(['jump', 'jump', 'jump', 'jump', 'jump'], '||?||') )

