class Nodo:
	def __init__(self, elemento):
		self.elemento = elemento
		self.siguiente = None
		
class Cola():
	def __init__(self):
		self.primero = None
		self.ultimo = None
	def Cola_Vacia(self):
		if self.primero == None:
			return True
		else:
			return False
	def Insert(self,Elemento):
		if self.Cola_Vacia():
			self.primero = self.ultimo = Nodo(Elemento)
			self.ultimo.siguiente = self.primero
		else:
			aux = self.ultimo
			aux.siguiente = self.ultimo = Nodo(Elemento)
			self.ultimo.siguiente = self.primero
	def Recorrer(self):
		aux = self.primero
		while aux.siguiente != self.primero:
			print(aux.elemento)
			aux = aux.siguiente
		print(aux.elemento)
	def Remove(self):
		aux = self.primero
		eliminado = aux.elemento
		self.primero = aux.siguiente
		self.ultimo.siguiente = self.primero
		del aux
		return eliminado
	def Search(self, Elemento):
		aux = self.primero
		while aux.elemento != Elemento:
			aux = aux.siguiente
			if aux == self.primero:
				break
		return aux.elemento == Elemento

cola = Cola()
cola.Insert(18)
cola.Insert(20)
cola.Insert(30)
cola.Insert(40)
cola.Recorrer()	
print("Eliminado: ", cola.Remove())
cola.Recorrer()
cola.Insert(52)
print(cola.Search(20))
print(cola.Search(40))
print(cola.Search(5))

