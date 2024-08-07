""" 
Crea un programa que sea capaz de transformar texto natural a código
morse y viceversa.
 - Debe detectar automáticamente de qué tipo se trata y realizar
   la conversión.
 - En morse se soporta raya "—", punto ".", un espacio " " entre letras
   o símbolos y dos espacios entre palabras "  ".
 - El alfabeto morse soportado será el mostrado en
   https://es.wikipedia.org/wiki/Código_morse. 
"""



def codigo_morse(letra):
	letra_morse = " "
	if letra == 'a' or letra == 'A':
			letra_morse = ".-"
	elif letra == 'b' or letra == 'B':
			letra_morse = "-..."
	elif letra == 'c' or letra == 'C':
			letra_morse = "-.-."
	elif letra == 'd' or letra == 'D':
		letra_morse = "-.."
	elif letra == 'e' or letra == 'E':
		letra_morse = "."
	elif letra == 'f' or letra == 'F':
		letra_morse = "..-."
	elif letra == 'g' or letra == 'G':
		letra_morse = "--."
	elif letra == 'h' or letra == 'H':
		letra_morse = "...."
	elif letra == 'i' or letra == 'I':
		letra_morse = ".."
	elif letra == 'j' or letra == 'J':
		letra_morse = ".---"
	elif letra == 'k' or letra == 'K':
		letra_morse = "-.-"
	elif letra == 'l' or letra == 'L':
		letra_morse = ".-.."
	elif letra == 'm' or letra == 'M':
		letra_morse = "--"
	elif letra == 'n' or letra == 'N':
		letra_morse = "-."
	elif letra == 'o' or letra == 'O':
		letra_morse = "---"
	elif letra == 'p' or letra == 'P':
		letra_morse = ".--."
	elif letra == 'q' or letra == 'Q':
		letra_morse = "--.-"
	elif letra == 'r' or letra == 'R':
		letra_morse = ".-." 
	elif letra == 's' or letra == 'S':
		letra_morse = "..."
	elif letra == 't' or letra == 'T':
		letra_morse = "-"
	elif letra == 'u' or letra == 'U':
		letra_morse = "..-"
	elif letra == 'v' or letra == 'V':
		letra_morse = "...-"
	elif letra == 'w' or letra == 'W':
		letra_morse = ".--"
	elif letra == 'x' or letra == 'X':
		letra_morse = "-..-"
	elif letra == 'y' or letra == 'Y':
		letra_morse = "-.--"
	elif letra == 'z' or letra == 'Z':
		letra_morse = "--.."
	elif letra == '1':
		letra_morse = ".----"
	elif letra == '2':
		letra_morse = "..---"
	elif letra == '3':
		letra_morse = "...--"
	elif letra == '4':
		letra_morse = "....-"
	elif letra == '5':
		letra_morse = "....."
	elif letra == '6':
		letra_morse = "-...."
	elif letra == '7':
		letra_morse = "--..."
	elif letra == '8':
		letra_morse = "---.."
	elif letra == '9':
		letra_morse = "----." 
	elif letra == '0':
		letra_morse = "-----"
	elif letra == '.':
		letra_morse = ".-.-.-"
	elif letra == ",":
		letra_morse = "--..--"
	elif letra == '?':
		letra_morse = "..--.."
	elif letra == '"' or letra == "'":
		letra_morse = ".-..-."
	elif letra == '/':
		letra_morse = "-..-."
	return letra_morse

frase_original = "La casa de al lado es azul"

# lista = ["a", "e", "i", "o", "u"]
frase_morse = ""
for letra in frase_original:
	frase_morse = frase_morse + codigo_morse(letra)

print(frase_morse)