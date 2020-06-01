from collections import *
class Grafo(object):
    def __init__(self):
        self.relaciones = {}
    def __str__(self):
        return str(self.relaciones)

def agregar(grafo, elemento):
   grafo.relaciones.update({elemento:[]})

def relacionar(grafo, elemento1, elemento2):
    relacionarUnilateral(grafo, elemento1, elemento2)
    relacionarUnilateral(grafo, elemento2, elemento1)

def relacionarUnilateral(grafo, origen, destino):
    grafo.relaciones[origen].append(destino)

def profundidadPrimero(grafo, elementoInicial, funcion, elementosRecorridos = []):
    if elementoInicial in elementosRecorridos:
        return
    funcion(elementoInicial)
    elementosRecorridos.append(elementoInicial)
    for vecino in grafo.relaciones[elementoInicial]:
        profundidadPrimero(grafo, vecino, funcion, elementosRecorridos)

def anchoPrimero(grafo, elementoInicial, funcion, cola = deque(), elementosRecorridos = []):
    if not elementoInicial in elementosRecorridos:
        funcion(elementoInicial)
        elementosRecorridos.append(elementoInicial)
        if len(grafo.relaciones[elementoInicial]) > 0:
          cola.extend(grafo.relaciones[elementoInicial])
    if len(cola) != 0:
        anchoPrimero(grafo, cola.popleft(), funcion, cola, elementosRecorridos)
def imprimir(elemento):
    print(elemento)

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
agregar(grafo, sanPedro)
agregar(grafo, rosario)
agregar(grafo, cordoba)
agregar(grafo, villaMaria)
agregar(grafo, bahiaBlanca)
agregar(grafo, mendoza)

relacionar(grafo, buenosAires, sanPedro)
relacionar(grafo, buenosAires, sanLuis)
relacionar(grafo, buenosAires, bahiaBlanca)
relacionar(grafo, sanLuis, mendoza)
relacionar(grafo, sanLuis, villaMaria)
relacionar(grafo, sanLuis, bahiaBlanca)
relacionar(grafo, villaMaria, cordoba)
relacionar(grafo, villaMaria, rosario)
relacionar(grafo, rosario, sanPedro)
print("Recorrido Primero en profundidad")
profundidadPrimero(grafo, buenosAires, imprimir)
print("Recorrido Primero en Ancho")
anchoPrimero(grafo, buenosAires, imprimir)
