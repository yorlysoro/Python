from grafosConPesos import *

buenosAires = "BuenosAires"
sanPedro = "San Pedro"
rosario = "Rosario"
cordoba = "Cordoba"
villaMaria = "Villa Maria"
sanLuis = "San Luis"
mendoza = "Mendoza"
bahiaBlanca = "Bahia Blanca"



grafo = Grafo()
agregar(grafo, buenosAires)
agregar(grafo, sanLuis)
agregar(grafo, sanPedro)
agregar(grafo, rosario)
agregar(grafo, cordoba)
agregar(grafo, villaMaria)
agregar(grafo, bahiaBlanca)
agregar(grafo, mendoza)

relacionar(grafo, buenosAires, sanPedro, 175)
relacionar(grafo, buenosAires, sanLuis, 790)
relacionar(grafo, buenosAires, bahiaBlanca, 660)


relacionar(grafo, sanLuis, mendoza,260)
relacionar(grafo, sanLuis, villaMaria,350)
relacionar(grafo, sanLuis, bahiaBlanca,800)
relacionar(grafo, villaMaria, cordoba,150)
relacionar(grafo, villaMaria, rosario,245)
relacionar(grafo, rosario, sanPedro,160)

def imprimir (elemento):
    print elemento 

print caminoMinimo(grafo,buenosAires,villaMaria)

