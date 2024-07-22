# LIST COMPREHENSION

my_original_list = [35, 24, 62, 52, 30, 30, 17]
my_original_list = [0, 1, 2, 3, 4, 5, 6, 7]


my_list = [i for i in my_original_list]  # Transforma una lista a otra lista
print(my_list)  # --> [0, 1, 2, 3, 4, 5, 6, 7]

my_list = [i for i in range(7)]  # Recoge 0-6  --> [0, 1, 2, 3, 4, 5, 6]
print(my_list)

my_list = [i for i in range(8)]  # Recoge 0-7  --> [0, 1, 2, 3, 4, 5, 6, 7]
print(my_list)

my_range = range(8)  #Rango 0-7  --> [0, 1, 2, 3, 4, 5, 6, 7]
print(list(my_range))

my_list = [i + 1 for i in range(8)]  # Recoge 1-8 --> [1, 2, 3, 4, 5, 6, 7, 8]
print(my_list)

my_list = [i * 2 for i in range(8)]  # Recoge 0-7 * 2  --> [0, 2, 4, 6, 8, 10, 12, 14]
print(my_list)

my_list = [i * i for i in range(8)]  # Recoge 0-7 * 0-7  --> [0, 1, 4, 9, 16, 25, 36, 49]
print(my_list)

def sum_five (number):
	return number + 5

my_list = [sum_five(i) for i in range(8)]  # Recoge de  5-12 -->  [5, 6, 7, 8, 9, 10, 11, 12]
print(my_list)

