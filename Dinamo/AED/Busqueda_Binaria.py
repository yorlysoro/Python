elementos = 15
lista = list(range(0,elementos,2))
primero = 0
ultimo = elementos
mitad = (primero + ultimo) // 2
i = 12
print(lista)
while(lista[mitad] != i ) or (primero < ultimo):
	mitad = (primero + ultimo) // 2
	if i > lista[mitad]:
		primero = mitad + 1
	else:
		ultimo = mitad - 1
if lista[mitad] == i:
	print("El valor ", i, " corresponde a ", mitad)
else:
	print("El valor ", i, "no existe")
