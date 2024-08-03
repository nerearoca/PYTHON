# LAMBDAS --> como una funcion, pero en realidad, son como funciones anonimas(sin nombre)

sum_two_values = lambda first_value, second_value: first_value + second_value
print(sum_two_values(1,5))

sum_two_values = lambda first_value, second_value: print(first_value + second_value)
sum_two_values(3,5)

multiply_values = lambda first_value, second_value: first_value * second_value - 3
print(multiply_values(2,4))

def sum_three_values(value):
	return lambda first_value, second_value: first_value + second_value + value
print(sum_three_values(4))
print('Sum_three_values: ',sum_three_values(5)(2,4))  # Moure decia que no esta soportado.... (????)