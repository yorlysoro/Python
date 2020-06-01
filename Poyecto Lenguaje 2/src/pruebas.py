
with open("prueba.txt", "w") as prueba:
	prueba.write("Titulo\n")
	prueba.write("Otra linea")
prueba.close()

with open("prueba.txt", "r") as prueba:
	for linea in prueba:
		print(linea, end='')
prueba.close()

import re
mes = "Enero febrero"
linea = "			Nomina"
if(re.search("Enero", linea)):
	print("Se encuentra")
else:
	print("No se encuentra")
valores = None

fecha = "12 				1 			Enero"
valores = fecha.split()
print(valores)

from constantes import Meses

print(Meses)

tupla = (1,2,3)

print(tupla[0])