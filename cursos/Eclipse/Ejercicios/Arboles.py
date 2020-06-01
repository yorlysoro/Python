from builtins import str
class Arbol:
	def __init__(self, carga, izquierda=None, derecha=None):
		self.carga = carga
		self.izquierda = izquierda
		self.derecha = derecha
		
	def __str__(self):
		from _ast import Str
		return str(self.carga)
	
	def tomaCarga(self): return self.carga
	def tomaIzquierda(self): return self.izquierda
	
	def tomaDerecha(self): return self.derecha
	
	def ajustaCarga(self, carga): self.carga = carga
	def ajustaIzquierda(self, izquierda): self.left = izquierda
	def ajustarDerecha(self, derecha): self.derecha = derecha
	
def total(arbol):
	if arbol == None : return 0
	return total(arbol.izquierda) + total(arbol.derecha) + arbol.carga
	
def imprimeArbol(arbol):
	if arbol == None: return
	print(arbol.carga, imprimeArbol(arbol.izquierda), imprimeArbol(arbol.derecha))
	
def imprimeArbolPosfijo(arbol):
	if arbol == None: return
	imprimeArbolPosfijo(arbol.izquierda)
	imprimeArbolPosfijo(arbol.derecha)
	print(arbol.carga)
	
def imprimeArbolInfijo(arbol):
	if arbol == None: return
	imprimeArbolInfijo(arbol.izquierda)
	print(arbol.carga)
	imprimeArbolInfijo(arbol.derecha)
	
def imprimeArbolSangrado(arbol, nivel=0):
	if arbol == None: return
	imprimeArbolSangrado(arbol.derecha, nivel+1)
	print(' ' * nivel + str(arbol.carga))
	imprimeArbolSangrado(arbol.izquierda, nivel+1)