def imprimeLista(nodo):
	while nodo:
		print(nodo)
		nodo = nodo.siguiente
	print()
	
def imprimeAlReves(lista):
	if lista == None: return
	cabeza = lista
	cola = lista.siguiente
	imprimeAlReves(cola)
	print(cabeza)
	
def imprimeAlRevesBonito(lista):
	print("[")
	if lista != None:
		cabeza = lista
		cola = lista.siguiente
		imprimeAlReves(cola)
		print(cabeza)
	print("]")
	
def eliminaSegundo(lista):
	if lista == None: return
	primero = lista
	segundo = lista.siguiente
	primero.siguiente = segundo.siguiente
	segundo.siguiente = None
	return segundo

class Nodo:
	def __init__(self, carga=None, siguiente=None):
		self.carga = carga
		self.siguiente = siguiente
		
	def __str__(self):
		from _ast import Str
		return str(self.carga)
	
	def imprimeAlReves(self):
		if self.siguiente != None:
			cola = self.siguiente
			cola.imprimeAlReves()
		print(self.carga)
		
class ListaEnlazada:
	def __init__(self):
		self.longitud = 0
		self.cabeza = None
		
	def imprimeAlReves(self):
		print("[")
		if self.cabeza != None:
			self.cabeza.imprimeAlReves()
		print("]")
		
	def agregarPrimero(self, carga):
		nodo = Nodo(carga)
		nodo.siguiente = self.cabeza
		self.cabeza = nodo
		self.longitud = self.longitud + 1