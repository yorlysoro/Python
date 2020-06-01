from grafos import *

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

relacionar(grafo, buenosAires, sanPedro)
relacionar(grafo, buenosAires, sanLuis)
relacionar(grafo, buenosAires, bahiaBlanca)
relacionar(grafo, buenosAires, sanLuis)
relacionar(grafo, sanLuis, mendoza)
relacionar(grafo, sanLuis, villaMaria)
relacionar(grafo, sanLuis, bahiaBlanca)
relacionar(grafo, villaMaria, cordoba)
relacionar(grafo, villaMaria, rosario)
relacionar(grafo, rosario, sanPedro)

def imprimir (elemento):
    print elemento 

profundidadPrimero(grafo, buenosAires, imprimir)
anchoPrimero(grafo, buenosAires, imprimir)


