# DATES

from datetime import datetime

def print_date(date):
	print(date.year)
	print(date.month)
	print(date.day)
	print(date.hour)
	print(date.minute)
	print(date.second)
	print(date.timestamp())

now = datetime.now()
print_date(now)

# timestamp = now.timestamp()
# print(timestamp)

# Definir fecha
year_2024 = datetime(2024, 7, 11)
print_date(year_2024)

# No tiene valores predefinidos, siempre estan a 0, por lo que hay que darles valores
from datetime import time
current_time = time(18, 55, 16)

print(current_time.hour)
print(current_time.minute)
print(current_time.second)

from datetime import date
current_date = date(2024, 12, 9)
current_date = date.today()

print(current_date.year)
print(current_date.month)
print(current_date.day)

print(current_date.weekday())  # Va de 0-6

# No se puede modificar uno a uno por propiedad, pero se tiene que crear nuevo
current_date = date(current_date.year + 1, current_date.month + 1 , current_date.day)
print(current_date.year)
print(current_date.month)

# Restar fechas
diff = year_2024 - now
print(diff)
diff = year_2024.date() - current_date
print(diff)

from datetime import timedelta

time_delta = timedelta()
start_timedelta = timedelta(200, 100, 100, weeks = 10)
end_timedelta = timedelta(300, 100, 100, weeks = 13)
print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta)
print(end_timedelta, start_timedelta)