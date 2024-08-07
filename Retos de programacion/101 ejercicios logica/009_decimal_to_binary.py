"""
DECIMAL A BINARIO
Crea un programa se encargue de
transformar un número decimal a binario.
"""

def dec_to_bin(decimal):

	binary = ""

	while decimal > 0:

		binary = f"{decimal % 2}{binary}"
		decimal //= 2
	
	if binary:
		return binary
	else:
		return ""


dec = input('Escriba el decimal que quiera convertir en binario: ')
binario = dec_to_bin(int(dec))
print(binario)

# print(dec_to_bin(20))