
m = int(input('Dime el numero de filas: '))
n = int(input('Dime el numero de columnas: '))

A = []
for i in range(m):
	A.append([0] * n)
	
B = []
for i in range(m):
	B.append([0] * n)
	
print("Lectura de la matriz A")
for i in range(m):
	for j in range(n):
		A[i][j] = float(input("Dame el componente (%d,%d): " %(i,j)))
		
print("Lectura de la matriz B")
for i in range(m):
	for j in range(n):
		B[i][j] = float(input("Dame le componente (%d,%d): " %(i,j)))
		
C = []
for i in range(m):
	C.append([0] * n)
	
for i in range(m):
	for j in range(n):
		C[i][j] = A[i][j] + B[i][j]
		
print("Suma: ")
for i in range(m):
	for j in range(n):
		print(C[i][j])
