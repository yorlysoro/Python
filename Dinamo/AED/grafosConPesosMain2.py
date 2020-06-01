from grafosConPesos import *

a = "a"
b = "b"
c = "c"
d = "d"
e = "e"
f = "f" 
g = "g" 
h = "h"

grafo = Grafo()
agregar(grafo, a)
agregar(grafo, b)
agregar(grafo, c)
agregar(grafo, d)
agregar(grafo, e)
agregar(grafo, f)
agregar(grafo, g)
agregar(grafo, h)

relacionar(grafo, a, c, 1)
relacionar(grafo, a, b, 3)
relacionar(grafo, b, d, 1)
relacionar(grafo, b, g, 5)
relacionar(grafo, c, f, 5)
relacionar(grafo, c, d, 2)
relacionar(grafo, d, f, 2)
relacionar(grafo, d, e, 4)
relacionar(grafo, e, h, 1)
relacionar(grafo, e, g, 2)
relacionar(grafo, f, h, 3)



def imprimir (elemento):
    print elemento 

print caminoMinimo(grafo, e, a)


