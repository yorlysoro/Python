lista = list(range(0, 30, 2))

buscar = int(input("Introduzca el numero a buscar: "))

print(lista)
for i in range(len(lista)):
	if lista[i] == buscar:
		print("Encontrado en la posicion: ", i)
		break
	
else: 
	print("No encontrado")

		
	
