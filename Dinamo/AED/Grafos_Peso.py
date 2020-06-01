class Grafo(object):
	def __init__(self):
		self.relaciones = {}
	def __str__(self):
		return str(self.relaciones)
		
class Arista(object):
	def __init__(self, elemento, peso):
		self.elemento = elemento
		self.peso = peso
	def __str__(self):
		return str(self.elemento) + str(self.peso)
		
def agregar(grafo, elemento):
	grafo.relaciones.update({elemento:[]})
	
def relacionar(grafo, elemento1, elemento2, peso = 1):
	relacionarUnilateral(grafo, elemento1, elemento2, peso)
	relacionarUnilateral(grafo, elemento2, elemento1, peso)

def relacionarUnilateral(grafo, origen, destino, peso):
	grafo.relaciones[origen].append(Arista(destino, peso))

def caminoMinimo(grafo, origen, destino):
	etiquetas = {origen:(0, None)}
	dijkstra(grafo, destino, etiquetas, [])
	return construirCamino(etiquetas, origen, destino)
	
def construirCamino(etiquetas, origen, destino):
	print(origen, destino)
	if origen == destino:
		return [origen]
	return construirCamino(etiquetas, origen, anterior(etiquetas[destino])) + [destino]
	
def dijkstra(grafo, destino, etiquetas, procesados):
	nodoActual = menorValorNoProcesado(etiquetas, procesados)
	if nodoActual == destino:
		return
	procesados.append(nodoActual)
	for vecino in vecinoNoProcesado(grafo, nodoActual, procesados):
		generarEtiqueta(grafo, vecino, nodoActual, etiquetas)
	dijkstra(grafo, destino, etiquetas, procesados)
	
def generarEtiqueta(grafo, nodo, anterior, etiquetas):
	etiquetaNodoAnterior = etiquetas[anterior]
	etiquetaPropuesta = peso(grafo, anterior, nodo) + acumulado(etiquetaNodoAnterior), anterior
	if (not (etiquetas.has_key(nodo)) or acumulado(etiquetaPropuesta) < acumulado(etiquetas[nodo])):
		etiquetas.update({nodo:etiquetaPropuesta})

def aristas(grafo, nodo):
	return grafo.relaciones[nodo]
def vecinoNoProcesado(grafo, nodo, procesados):
	aristasDeVecinosNoProcesados = filte(lambda x: not x in procesados, aristas(grafo, nodo))
	return [aristas.elemento for arista in aristasDeVecinosNoProcesados]
def peso(grafo, nodoOrigen, nodoDestino):
	return reduce(lambda x,y: x if x.elemento == nodoDestino else y, grafo.relaciones[nodoOrigen]).peso
	
def acumulado(etiqueta):
	return etiqueta[0]
def anterior(etiqueta):
	return etiqueta[1]
def menorValorNoProcesado(etiquetas, procesados):
	etiquetadosSinProcesar = filter(lambda (nodo, _): not nodo in procesados, etiquetas.iteritems())	
	return min(etiquetadosSinProcesar, key=lambda(_,(acum,__)):acum)[0]

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
