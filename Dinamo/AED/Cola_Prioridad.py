class Nodo:
	def __init__(self, elemento, prioridad):
		self.elemento = elemento
		self.siguiente = None
		self.prioridad = prioridad
		

class Cola():
	def __init__(self):
		self.primero = None
		self.ultimo = None
	def Cola_Vacia(self):
		if self.primero == None:
			return True
		else:
			return False
	def Insert(self,Elemento, Prioridad):
		if self.Cola_Vacia():
			self.primero = self.ultimo = Nodo(Elemento, Prioridad)
		else:
			aux = self.ultimo
			if Prioridad >= aux.prioridad:
				self.ultimo = Nodo(Elemento, Prioridad)
				aux.siguiente = self.ultimo
			else:
				recorre = self.primero
				while recorre.siguiente:
					if recorre.prioridad == Prioridad:
						while recorre.siguiente:
							if recorre.siguiente.prioridad != Prioridad:
								NodoNuevo = Nodo(Elemento, Prioridad)
								NodoNuevo.siguiente = recorre.siguiente
								recorre.siguiente = NodoNuevo
								break
							recorre = recorre.siguiente
						break
					recorre = recorre.siguiente
	def Recorrer(self):
		aux = self.primero
		while aux.siguiente:
			print(aux.elemento,"con prioridad", aux.prioridad)
			aux = aux.siguiente
		print(aux.elemento,"con prioridad", aux.prioridad)
	def Remove(self):
		aux = self.primero
		eliminado = aux.elemento
		self.primero = aux.siguiente
		del aux
		return eliminado
	def Search(self, Elemento):
		aux = self.primero
		try:
			while aux.elemento != Elemento:
				aux = aux.siguiente
			return True
		except AttributeError:
			return False
			
cola = Cola()
cola.Insert(18,1)
cola.Insert(20,1)
cola.Insert(22,1)
cola.Recorrer()
cola.Insert(22,2)
cola.Insert(24,2)
cola.Insert(26,2)
cola.Recorrer()
cola.Insert(16,1)
cola.Recorrer()
print("Remove =", cola.Remove())
cola.Recorrer()
print(cola.Search(20))
print(cola.Search(10))
