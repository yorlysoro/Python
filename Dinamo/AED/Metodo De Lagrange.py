k = float(input("Punto que desea interpolar: "))
prod = 1.0
suma = 0.0
nmax = 20
x = list(i * 1.0 for i in range(1, nmax))
funcion = list(i * 1.0 for i in range(1, nmax))
for i in range(1, nmax):
	for j in range(1, nmax):
		if i != j:
			prod = prod *((k - x[j-1])/(x[i-1] - x[j-1]))
		suma = suma + prod * funcion[i-1]
print("El valor de la funcion en el punto ", k," es ", suma)
