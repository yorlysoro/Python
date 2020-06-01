class Grafo:
    def __init__(self, elemento):
        self.elemento = elemento
        self.sig = []

class Arista:
    def __init__(self, Relacion, peso):
        self.Relacion = Relacion
        self.peso = peso

class Lista_Grafos:
    def __init__(self):
        self.grafos = []

def Agregar(elemento, lG):
    grafo = Grafo(elemento)
    lG.grafos.append(grafo)
    return grafo

def Relacionar(Grafo, sig, peso = 1):
    arista = Arista(sig,peso)
    Grafo.sig.append(arista)

def Pesos(Grafo, Inicio, Final, Recorre = Grafo,pesos = []):
    pass

def Caminos(lG):
    for elements in lG.grafos:
        print(elements.elemento, ":")
        for i in range(len(elements.sig)):
            imprime = elements.sig[i].Relacion
            print(imprime.elemento)


lG = Lista_Grafos()
Guayaquil = Agregar("Guayaquil", lG)
Quito = Agregar("Quito", lG)
Cuenca = Agregar("Cuenca", lG)
Ambato = Agregar("Ambato", lG)
Riobamba = Agregar("Riobamba", lG)

Relacionar(Guayaquil, Quito, 9)
Relacionar(Guayaquil, Ambato, 7)
Relacionar(Guayaquil, Riobamba, 7)
Relacionar(Quito, Guayaquil, 9)
Relacionar(Quito, Cuenca, 8)
Relacionar(Cuenca, Quito, 8)
Relacionar(Cuenca, Ambato, 5)
Relacionar(Cuenca, Riobamba, 5)
Relacionar(Ambato, Guayaquil, 7)
Relacionar(Ambato, Cuenca, 5)
Relacionar(Riobamba, Guayaquil,7)
Relacionar(Riobamba, Cuenca, 5)

print("Caminos: ")

Caminos(lG)
peso = 0
YaRecorridos = []
for elements in lG.grafos:
    for grafo in elements.sig:
        if grafo.Relacion in YaRecorridos:
            continue
        else:
            peso += grafo.peso
        YaRecorridos.append(grafo.Relacion)
print(peso)

origen = Guayaquil
destino = Cuenca

for grafos in lG.grafos:
    for aristas in grafos.sig:
        if aristas.Relacion != origen:
            peso += aristas.peso
            print(aristas.Relacion.elemento)
        if peso > 0:
            print("Peso:", peso)
    peso = 0

