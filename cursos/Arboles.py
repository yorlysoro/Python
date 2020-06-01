class Arbol:
    def __init__(self, carga, izquierda=None, derecha=None):
        self.carga = carga
        self.izquierad = izquierad
        self.derecha = derecha

    def __str__(self):
        return str(self.carga)
    def tomaCarga(self): return self.carga
    def tomaIzquierda(self): return self.izquierda

    def tomaDerecha(self): return self.derecha
    def ajustaCarga(self, carga): self.carga = carga
    def ajustaIzquierda(self, izquierda): self.left = izquierda
    def ajustaDerecha(self, derecha): self.derecha = derecha

    def total(arbol):
        if arbol == None : return 0
        return total(arbol.izquieda) + total(arbol.derecha) + arbol.carga
    def imprimeArbol(arbol):
        if arbol == None : return
        print arbol.carga,
        imprimeArbol(arbol.izquierda)
        imprimeArbol(arbol.derecha)

    def imprimeArbolPostfijo(arbol):
        if arbol == None: return
        imprimeArbolPostfijo(arbol.izquierda)
        print arbol.carga,
        imprimeArbolInfijo(arbol.derecha)

    def imprimeArbolSangrado(arbol, nivel=0):
        if arbol == None: return
        imprimeArbolSangrado(arbol.derecha, nivel+1)
        print ' ' * nivel + str(arbol.carga)
        imprimeArbolSangrado(arbol.izquierda, nivel+1)

    
