Q = list([[i*0 for i in range(4)] for i in range(4)])

W = [[25,4,8,9],[11,15,4,0],[8,7,13,0],[0,12,35,48]]

print("Matriz Q inicializada: ", Q)
print("Matriz W inicializada: ", W)

for i in range(4):
    for j in range(4):
        if W[i][j] == 0:
            Q[i][j] == 0
        else:
            Q[i][j] = W[i][j]

print("Matriz Q Actualizada: ", Q)
for k in range(4):
    for i in range(4):
        for j in range(4):
            Q[i][j] = Q[i][j] + Q[k][j]

print("Matriz Q Final: ", Q)

