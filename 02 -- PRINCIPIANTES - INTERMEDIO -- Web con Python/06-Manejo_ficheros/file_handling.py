# #  File Handling

# import os


# # .txt file

# # open("./my_file.txt")  #--> FileNotFoundError: [Errno 2] No such file or directory: "./my_file.txt"
# txt_file = open("06-Manejo_ficheros/my_file.txt", "w+") # desde el directorio directamente superior
# 																												# modo de lectura-escritura con r+
# 																												# modo de sobreescritura con w+
# txt_file.write("Mi nombre es Brais\nMi apellido es Moure\n35 años\nY mi lenguage favorito es Python")
# # print(txt_file.read()) # Lectura de todo el fichero
# # print(txt_file.read(10)) # Lectura de solo los primeros 10 caracteres

# # Lectua linea a linea 
# # print(txt_file.readline())    # Mi nombre es Brais
# # print(txt_file.readline())    # Mi apellido es Moure

# # Lee todas las lineas restantes 
# # print(txt_file.readlines())  # ["35 aÃ±os\n", "Y mi lenguage favorito es Python"]

# # Lectura de todo el fichero
# for line in txt_file.readlines():
# 	print(line)

# txt_file.write("\nAunque tambien me gusta Kotlin")  # Se añade al final del fichero
# print(txt_file.readline())

# txt_file.close()

# # os.remove("06-Manejo_ficheros/my_file.txt")  # Borrar el fichero


# # .json file

# import json

# json_file = open("06-Manejo_ficheros/my_file.json", "w+")
# json_test = {
# 	"name": "Brais", 
# 	"surname": "Moure", 
# 	"age": 35, 
# 	"languages":["Python", "Kotlin", "Swift"]
# }

# json.dump(json_test, json_file, indent = 2)

# json_file.close()

# with open("06-Manejo_ficheros/my_file.json") as my_other_file:
# 	for line in my_other_file.readlines():
# 		print(line)

# json_dict = json.load(open("06-Manejo_ficheros/my_file.json"))
# print(json_dict)

# print(json_dict['name'])


# # .csv file

# import csv

# csv_file = open("06-Manejo_ficheros/my_file.csv", "w+")

# # json_test = {
# 	# "name": "Brais", 
# 	# "surname": "Moure", 
# 	# "age": 35, 
# 	# "languages":["Python", "Kotlin", "Swift"]
# # }
# csv_writer = csv.writer(csv_file)
# csv_writer.writerow(['name', "surname", "age", "language"])
# csv_writer.writerow(['Brais', "Moure", 35, "Python"])
# csv_writer.writerow(['Roswell', "", 2, "COBOL"])

# csv_file.close()

# with open("06-Manejo_ficheros/my_file.csv") as my_other_file:
# 	for line in my_other_file.readlines():
# 		print(line)


# .xlsx file
# import xlrd # debe instalarse el modulo

# .xml
# import xml

# .pdf --> hay dos tipos de archivos pdf(con el texto plano este sirve, con los demas no)

import PyPDF2
pdf = open('06-Manejo_ficheros/ud7_diw_activity5.pdf', "rb")
reader = PyPDF2.PdfReader(pdf)
# page = reader._get_page(0) # Recoger una pagina
page = reader.pages[0]

informacion = page.extract_text()
print(informacion)


with open('06-Manejo_ficheros/info_pdf.txt', 'w+') as txt:
	txt.write(informacion)

pdf = open('06-Manejo_ficheros/ud7_diw_activity5.pdf', "rb")
reader = PyPDF2.PdfReader(pdf)
# print(reader.metadata)
# print(reader._get_num_pages())

# page = reader._get_page(1)
# text = page.extract_text()

# print(text)

# page = reader.pages[0]
# text = page.extract_text()
# print(text)