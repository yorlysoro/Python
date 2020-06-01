class Nodo:
    def __init__(self, ciudad, sig, ady, ndisp):
        self.ciudad = ciudad
        self.sig = sig
        self.ady = ady
        self.ndisp = ndisp
class Arista:
    def __init__(self, numero, orig, dest, enl, adisp):
        self.numero = numero
        self.orig = orig
        self.dest = dest
        self.enl = enl
        self.adisp = adisp


def Grafo(Nodo, sig, ady, principio, ndisp, enl, adisp):
    
