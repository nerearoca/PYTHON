# CLASES

# class MyEmptyPerson:
# 	pass # Evita el error siendo null, si el objeto no tiene nada dentro


# print(MyEmptyPerson)
# print(MyEmptyPerson())

class Person:
	def __init__ (self, name, surname, alias = 'Sin alias'):
		self.__name = name
		self.__surname = surname

		self.full_name = f"{name} {surname} ({alias})"
	
	def get_name (self):
		return self.__name

	def walk (self):
		# pass
		print(f"{self.full_name} esta caminando")




# Hace lo mismo pero es diferente 
my_person = Person('Brais', 'Moure')
print(f"{my_person.name} {my_person.surname}")
my_person.walk()

my_person_two = Person(name='Brais', surname = 'Moure')
print(my_person_two.full_name)
my_person_two.walk()

my_other_person = Person('Nerea', 'Roca', 'Junior')
my_other_person.walk()

my_other_person.full_name = 'Héctor de Leon (El Loco de los Perros)'
my_other_person.walk()
print(my_other_person.full_name)
# print(my_other_person.__name)  # No se uede acceder ni  modificar
print(my_other_person.get_name())