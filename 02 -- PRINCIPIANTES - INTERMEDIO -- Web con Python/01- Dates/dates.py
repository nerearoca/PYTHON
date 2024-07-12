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

from datetime import time
print(time)