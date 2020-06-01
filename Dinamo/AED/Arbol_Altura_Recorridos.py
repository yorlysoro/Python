from Arboles_Recorridos import Arbol

class Arbol_Altura_Recorridos(Arbol):
	def Recorre_Arbol(self,arbol):
		if arbol == None:
			return
		else:
			print(arbol.dato)
			self.Recorre_Arbol(arbol.derecho)
			self.Recorre_Arbol(arbol.izquierdo)

	def Nodos(self,arbol):
		Izquierdos = 0
		Derechos = 0
		if arbol == None:
			return 0
		else:
			Derechos = self.Nodos(arbol.derecho)
			Izquierdos = self.Nodos(arbol.izquierdo)
			return 1 + Derechos + Izquierdos
	 
	def Altura(self,arbol,nivel):
		if arbol == None and nivel == 0:
			return -1
		else:
			if arbol == None:
				return 0
			else:
				Altura1 = self.Altura(arbol.derecho,nivel+1)
				Altura2 = self.Altura(arbol.izquierdo,nivel+1)
				if Altura2 or nivel <= Altura1:
					return Altura1
				elif Altura1 or nivel <= Altura2:
					return Altura2
				else:
					return nivel
#arbol = Arbol_Altura_Recorridos()
#arbol.insertar(8)
#arbol.insertar(2)
#arbol.insertar(4)
#arbol.insertar(10)
#arbol.insertar(9)
#arbol.insertar(12)
#arbol.insertar(14)
#arbol.insertar(9)
#arbol.Recorre_Arbol(arbol.get_arbol())
#print("Nodos =",arbol.Nodos(arbol.get_arbol()))
#print("Altura =", arbol.Altura(arbol.get_arbol(),1))
