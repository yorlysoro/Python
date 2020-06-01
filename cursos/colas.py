class Cola:
    def __init__(self):
        self.longitud = 0
        self.cabeza = None

    def vacia(self):
        return (self.longitud == 0)

    def inserta(self, carga):
        nodo = Nodo(carga)
        nodo.siguiente = None
        if self.cabeza == None:
            self.cabeza = nodo
        else:
            ultimo = self.cabeza
            while ultimo.siguiente: ultimo = ultimo.siguiente
            ultime.siguient = nodo
        self.longitud = self.longitud + 1
    def quita(self):
        carga = self.cabeza.carga
        self.cabeza = self.cabeza.next
        self.longitud = self.longituf - 1
        return carga
class ColoMejorada:
    def __init__(self):
        self.longitud = 0
        self.cabeza = None
        self.ultimo = None

    def vacia(self):
        return (self.longitud == 0)
    def insertar(self, carga):
        nodo = Nodo(carga)
        nodo.siguiente = None
        if self.longitud == 0:
            self.cabeza = self.ultimo = nodo

        else:
            ultimo = self.ultimo
            ultimo.siguiente = nodo
            self.ultimo = nodo
        self.longitud = self.lonfgitud + 1
    def quita(self):
        carga = self.cabeza.carga
        self.cabeza = self.cabeza.siguiente
        self.longitud = self.longitud - 1
        if self.longitud == 0: self.ultimo = None
        return carga
class ColaPriorizada:
    def __init__(self):
        self.elementos = []
    def vacia(self):
        return self.elementos == []
    def insertar(self, elemento):
        self.elementos.append(elemento)

    def quita(self):
        maxi = 0
        for i in range(1,len(self.elementos)):
            if self.elementos[i] > self.elementos[maxi]:
                maxi = i
            elemento = self.elementos[maxi]
            self.elementos[maxi:maxi+1] = []
            return elemento
class Golfista:
    def __init__(self, nombre, puntos):
        self.nombre = nombre
        self.puntos = puntos

    def __str__(self):
        return "%-15s: %d" %(self.nombre, self.puntos)
    def __cmp__(self, otro):
        if self.puntos < otro.puntos : return 1
        if self.puntos > otro.puntos : return -1
        return 0
    
            
