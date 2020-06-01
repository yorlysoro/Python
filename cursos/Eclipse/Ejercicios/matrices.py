from builtins import int
m = int(input("Dame el numero de filas: "))
n = int(input("Dame el numero de columnas: "))

M = []
for i in range(m):
	M.append([0] * n)
	
	
	
for i in range(m):
	for j in range(n):
		M[i][j] = float(input("Dame el componente(%d, %d): " %(i,j))) 