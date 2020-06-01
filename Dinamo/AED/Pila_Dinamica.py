class Nodo:
	def __init__(self, elemento, abajo):
		self.elemento = elemento
		self.abajo = abajo
	
		
class Pila:
	def __init__(self):
		self.arriba = None
		self.inicio = None
		
	def Pila_Vacia(self):
		if self.inicio == None:
			return True
		else:
			return False
	def Push(self, Elemento):
		if self.Pila_Vacia():
			aux = Nodo(Elemento,None)
			self.inicio = self.arriba = aux
		else:
			aux_abajo = self.arriba
			aux = self.arriba
			self.arriba = Nodo(Elemento,aux_abajo)
			
	def Pop(self):
		try:
			aux = self.arriba
			aux_abajo = self.arriba.abajo
			eliminado = aux.elemento
			self.arriba = aux_abajo
			del aux
			return eliminado
		except AttributeError:
			print("Pila_Vacia")
			
	def Recorrer(self):
		try:
			aux = self.arriba
			while aux.abajo:
				print(aux.elemento, " apunta a ", aux.abajo.elemento)
				aux = aux.abajo
			print(aux.elemento, " apunta a ", aux.abajo)
		except AttributeError:
			print("Pila Vacia")
	def Buscar(self, Elemento):
		aux = self.arriba
		try:
			while aux.elemento != Elemento:
				aux = aux.abajo
			return True
		except AttributeError:
			return False	
pila = Pila()
pila.Pop()
pila.Push(12)
pila.Push(14)
pila.Push(16)
pila.Push(18)
pila.Push(20)
pila.Recorrer()
print("Eliminado: ", pila.Pop())
pila.Recorrer()
print("Eliminado: ", pila.Pop())
pila.Recorrer()
print("Eliminado: ", pila.Pop())
pila.Recorrer()
print("Eliminado: ", pila.Pop())
pila.Recorrer()
print("Eliminado: ", pila.Pop())
pila.Recorrer()
pila.Push(12)
pila.Push(14)
pila.Buscar(12)
pila.Buscar(8)
