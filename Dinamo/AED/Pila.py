class Pila:
	def __init__(self, MaxPila = 100):
		self.MaxPila = MaxPila
		self.Elementos = []
		self.Cabeza = 0
		
	def Pila_Vacia(self):
		if self.Cabeza == 0:
			return True
		else:
			return False
	def Pila_Llena(self):
		if self.MaxPila == self.Cabeza:
			return True
		else:
			return False
	def Push(self, Elemento):
		if self.Pila_Llena():
			raise IndexError("La pila esta llena")
		else:
			self.Elementos.append(Elemento)
			self.Cabeza += 1
	def Pop(self):
		if self.Pila_Vacia():
			raise IndexError("No hay elementos en la pila")
		else:
			ElementoSacado = self.Elementos.pop()
			self.Cabeza -= 1
			return ElementoSacado

pila = Pila()
pila.Push(21)
pila.Pop()
pila.Pop()
