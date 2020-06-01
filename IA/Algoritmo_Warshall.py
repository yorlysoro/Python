
P = list([[i for i in range(4)] for i in range(4)])
A = list([[2,4,0,5],[3,0,8,9],[0,4,2,1],[5,3,0,6]])

print("Inicializada la matriz P: ", P)
print("Inicializada la matriz A: ", A)

for i in range(4):
    for j in range(4):
        if A[i][j] == 0: 
            P[i][j] = 0
        else:
            P[i][j] = 1

for i in range(4):
    for i in range(4):
        for i in range(4):
            P[i][j] = P[i][j] or (iP[i][k] and P[k][j])

print("Matriz P resultante: ", P)

