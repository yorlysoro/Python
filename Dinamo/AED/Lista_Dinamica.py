class Nodo:
	def __init__(self, elemento):
		self.elemento = elemento
		self.siguiente = None
		
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
			aux.siguiente = self.final = Nodo(Elemento)
	def Insertar_Inicio(self, Elemento):
		if self.Lista_Vacia():
			self.inicio = self.final = Nodo(Elemento)
		else:
			aux = self.inicio
			self.inicio = Nodo(Elemento)
			self.inicio.siguiente = aux
	def Remover(self, Elemento):
		if self.Lista_Vacia():
			print("La lista esta vacia")
		elif self.inicio.elemento == Elemento and self.final.elemento == Elemento:
			aux = self.inicio = self.final
			self.inicio = self.final = aux.siguiente
			eliminado = aux.elemento
			del aux
			return eliminado
		elif self.inicio.elemento == Elemento:
			aux = self.inicio
			eliminado = aux.elemento
			self.inicio = aux.siguiente
			del aux
			return eliminado
		elif self.final.elemento == Elemento:
			aux = self.final
			recorrer = self.inicio
			eliminado = aux.elemento
			while recorrer.siguiente:
				if recorrer.siguiente == aux:
					recorrer.siguiente = recorrer.siguiente.siguiente
					self.final = recorrer
				else:
					recorrer = recorrer.siguiente
			del aux
			return eliminado
		else:
			aux = self.inicio
			aux_anterior = self.inicio
			while aux.siguiente:
				if aux.elemento == Elemento:
					eliminado = aux.elemento
					aux_anterior.siguiente = aux.siguiente
					del aux
					return eliminado  
				else:
					if aux_anterior.siguiente.elemento != Elemento:
						aux_anterior = aux_anterior.siguiente
					aux = aux.siguiente
					if aux.siguiente == None:
						print("No se encontro el elemento", Elemento)
	def Recorrer(self):
		if self.Lista_Vacia():
			print("Lista Vacia")
		else:
			aux = self.inicio
			while aux.siguiente:
				print(aux.elemento, " ")
				aux = aux.siguiente
			print(aux.elemento)
	def Consultar(self, Elemento):
		try:
			aux = self.inicio
			while aux.elemento != Elemento:
				aux = aux.siguiente
			return True
		except AttributeError:
			return False

lista = Lista()
lista.Remover(15)
lista.Insertar(20)
lista.Insertar(25)
lista.Recorrer()
lista.Remover(25)
lista.Recorrer()
lista.Remover(20)
lista.Recorrer()
for i in range(0,19,2):
	lista.Insertar(i)
lista.Recorrer()
lista.Remover(20)	
lista.Remover(0)
lista.Remover(18)
lista.Recorrer()
lista.Remover(12)
lista.Recorrer()
lista.Remover(4)
lista.Remover(14)
lista.Recorrer()
lista.Insertar_Inicio(12)
lista.Recorrer()
print(lista.Consultar(12))
print(lista.Consultar(16))
print(lista.Consultar(14))

				
