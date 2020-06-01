lista = [2,26,4,3,1]

for i in range(1, len(lista)):
	print("Pasada ", i)
	for j in range(0,len(lista)-i):
		print("Comparacion de los elemento en posicion %d y %d" %(j, j+1))
	if lista[j] > lista[j+1]:
		elemento = lista[j]
		lista[j] = lista[j+1]
		lista[j+1] = elemento
		print("Se intercambian")
	print("Esta actual de la lista", lista)
	
print (lista)
