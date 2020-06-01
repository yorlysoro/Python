p = int(input('Dime el numero de filas de A: '))
q = int(input('Dime el numero de columnas de A (y filas de B): '))
r = int(input('Dime el numero de columnas de B: '))


A = []
for i in range(p):
	A.append([0] * q)
	
B = []
for i in range(q):
	B.append([0] * r)
	
print("Lectura de la matriz A")
for i in range(p):
	for j in range(q):
		A[i][j] = float(input('Dame el componente (%d, %d): ' %(i,j)))

print("Lectura de la matriz B")
for i in range(q):
	for j in range(r):
		B[i][j] = float(input('Dame el componente (%d, %d): ' %(i,j)))
		

C = []
for i in range(p):
	C.append([0] * r)

for i in range(p):
	for j in range(r):
		for k in range(q):
			C[i][j] += A[i][j] * B[k][j]
