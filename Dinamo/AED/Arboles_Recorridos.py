class Raiz:
	def __init__(self, Dato):
		self.dato = Dato
		self.izquierdo = None
		self.derecho = None
		

class Arbol:
	def __init__(self):
		self.raiz = None
		
		
	def insertar(self, Dato):
		nivel, lado, result, padre = 1, "", True, 0
		if self.raiz == None:
			self.raiz = Raiz(Dato)
		else:
			aux = self.raiz
			while True:
				nivel += 1
				if(aux.dato < Dato):
					if(aux.derecho != None):
						padre = aux.dato
						aux = aux.derecho
					else:
						aux.derecho = Raiz(Dato)
						lado = "Derecho"
						break
				else:
					if(aux.dato > Dato):
						if(aux.izquierdo != None):
							padre = aux.dato
							aux = aux.izquierdo
						else:
							aux.izquierdo = Raiz(Dato)
							lado = "Izquierdo"
							break
					else:
						result = False
						break
			if result:
				print("Se inserto el dato", Dato, "como hijo",lado,"de", aux.dato,"en el nivel",nivel)
			else:
				print("El dato", Dato, "existe como hijo de", padre, "en el nivel", nivel-1)
				
	def get_arbol(self):
		return self.raiz

	def PreOrden(self,arbol):
		if arbol == None:
			return
		else:
			print(arbol.dato)
			self.PreOrden(arbol.izquierdo)
			self.PreOrden(arbol.derecho)
		
	def InOrden(self,arbol):
		if arbol == None:
			return
		else:
			self.InOrden(arbol.izquierdo)
			print(arbol.dato)
			self.InOrden(arbol.derecho)
	def PostOrden(self,arbol):
		if arbol == None:
			return
		else:
			self.PostOrden(arbol.izquierdo)
			self.PostOrden(arbol.derecho)
			print(arbol.dato)
#arbol = Arbol()
#arbol.insertar(8)
#arbol.insertar(2)
#arbol.insertar(4)
#arbol.insertar(10)
#arbol.insertar(9)
#arbol.insertar(12)
#arbol.insertar(14)
#arbol.insertar(9)
#arbol.PreOrden(arbol.get_arbol())
#arbol.InOrden(arbol.get_arbol())
#arbol.PostOrden(arbol.get_arbol())
