
elemento = 5
lista = [1,4,5,1,3,8]

pertenece = False
for i in lista:
	if elemento == i:
		pertenece = True
		break
	
if pertenece:
	print("Pertenece")
else:
	print("No pertenece")