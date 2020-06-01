class Nodo:
	def __init__(self, elemento):
		self.elemento = elemento
		self.siguiente = None
		self.anterior = None
		
class Lista:
	def __init__(self):
		self.inicio = None
		self.final = None
		
	def Lista_Vacia(self):
		if self.inicio == None:
			return True
		else:
			return False
			
	def Insertar(self, Elemento):
		if self.Lista_Vacia():
			self.Insertar_Inicio(Elemento)
		else:
			aux = self.final
			self.final = Nodo(Elemento)
			aux.siguiente = self.final
			self.final.anterior = aux
	def Insertar_Inicio(self, Elemento):
		if self.Lista_Vacia():
			self.inicio = self.final = Nodo(Elemento)
		else:
			aux = self.inicio
			self.inicio = Nodo(Elemento)
			self.inicio.siguiente = aux
			aux.anterior = self.inicio
	def Remover(self, Elemento):
		if self.Lista_Vacia():
			print("La lista esta vacia")
		elif self.inicio.elemento == Elemento and self.final.elemento == Elemento:
			aux = self.inicio = self.final
			self.inicio.siguiente = self.final.siguiente = None
			self.inicio = self.final = None
			self.inicio.anterior = self.final.anterior = None
			eliminado = aux.elemento
			del aux
			return eliminado
		elif self.inicio.elemento == Elemento:
			aux = self.inicio
			eliminado = aux.elemento
			self.inicio = aux.siguiente
			self.inicio.siguiente = aux.siguiente.siguiente
			self.inicio.anterior = aux.anterior
			del aux
			return eliminado
		elif self.final.elemento == Elemento:
			aux = self.final
			eliminado = aux.elemento
			aux.anterior.siguiente = aux.siguiente
			self.final = aux.anterior
			del aux
			return eliminado
		else:
			aux = self.inicio
			while aux.siguiente:
				if aux.elemento == Elemento:
					eliminado = aux.elemento
					aux.anterior.siguiente = aux.siguiente
					aux.siguiente.anterior = aux.anterior
					del aux
					return eliminado  
				else:
					aux = aux.siguiente
					if aux.siguiente == None:
						print("No se encontro el elemento", Elemento)
						
	def Recorrer(self):
		if self.Lista_Vacia():
			print("Lista Vacia")
		else:
			aux = self.inicio
			while aux.siguiente:
				print(aux.elemento)
				aux = aux.siguiente
			print(aux.elemento)
			
	def Recorrer_Inversa(self):
		aux = self.final
		while aux.anterior:
			print(aux.elemento)
			aux = aux.anterior
		print(aux.elemento)
		
lista = Lista()
for i in range(0,19,2):
	lista.Insertar(i)
lista.Recorrer()
lista.Remover(0)
lista.Recorrer()
lista.Remover(18)
lista.Recorrer()
lista.Remover(20)
lista.Remover(4)
lista.Remover(12)
lista.Remover(14)
lista.Recorrer()
lista.Recorrer_Inversa()
