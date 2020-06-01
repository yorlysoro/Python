import random

for i in range(10):
    x = random.random()
    print x

def listaAleatorios(n):
    s = [0] * n
    for i in range(n):
        s[i] = random.random()
        print s[i]
    return s

listaAleatorios(8)
