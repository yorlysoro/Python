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
    relacionarUnilateral(grafo, elemento1, elemento2, peso)

def relacionarUnilateral(grafo, origen, destino, peso):
    grafo.relaciones[origen].append(Arista(destino,peso))

def caminoMinimo(grafo, origen, destino):
    etiquetas = {origen: (0, None)}
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
    etiquetaPropuesta = peso(grafo,anterior, nodo) + acumulado(etiquetaNodoAnterior), anterior
    if not etiquetas.has_key(nodo) or acumulado(etiquetaPropuesta) < acumulado(etiquetas[nodo]):
        etiquetas.update({nodo:etiquetaPropuesta})

def aristas(grafo, nodo):
    return grafo.relaciones[nodo]

def vecinoNoProcesado(grafo, nodo, procesados):
    aristasDeVecinosNoProcesados = filter(lambda x: not x in procesados, aristas(grafo, nodo))
    return [arista.elemento for arista in aristasDeVecinosNoProcesados]

def peso(grafo, nodoOrigen, nodoDestino):
    return reduce(lambda x,y: x if x.elemento == nodoDestino else y, grafo.relaciones[nodoOrigen]).peso

def acumulado(etiqueta):
    return etiqueta[0]

def anterior(etiqueta):
    return etiqueta[1]

def menorValorNoProcesado(etiquetas, procesados):
    etiquetadosSinProcesar = filter(lambda(nodo,_): not nodo in procesados, etiqueta.iteritems())
    return min(etiquetadosSinProcesar, key = labmda(_, (acum, __)): acum)[0]

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

relacionar(grafo, buenosAires, sanPedro, 175)
relacionar(grafo, buenosAires, sanLuis, 790)
relacionar(grafo, buenosAires, bahiaBlanca, 660)
relacionar(grafo, sanLuis, mendoza, 260)
relacionar(grafo, sanLuis, villaMaria, 350)
relacionar(grafo, sanLuis, bahiaBlanca, 800)
relacionar(grafo, villaMaria, cordoba, 150)
relacionar(grafo, villaMaria, rosario, 245)
relacionar(grafo, rosario, sanPedro, 160)


