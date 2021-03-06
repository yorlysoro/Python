class Nodo:
	def __init__(self,dato):
		self.dato = dato
		self.izquierda = None
		self.derecha = None
		
class Arbol:
	def __init__(self):
		self.raiz = None
		
	def Insertar(self,dato):
		if self.raiz == None:
			self.raiz = Nodo(dato)
			print("Se inserto", dato, "como la raiz del arbol")
		else:
			result, padre, lado, nivel = True, 0, "", 1
			aux = self.raiz
			while True:
				nivel += 1
				if aux.dato < dato:
					if aux.derecha != None:
						padre = aux.dato
						aux = aux.derecha
					else:
						aux.derecha = Nodo(dato)
						lado = "derecha"
						break
				elif aux.dato > dato:
					if aux.izquierda != None:
						padre = aux.dato
						aux = aux.izquierda
					else:
						aux.izquierda = Nodo(dato)
						lado = "izquierda"
						break
				else:
					result = False
					break
			if result:
				print("Se inserto el dato", dato, "como hijo",lado,"de", aux.dato,"en el nivel", nivel)
			else:
				print("El dato", dato, "ya existe como hijo de", padre)
	def Enhebrar_Der(self,arbol):
		if arbol == None:
			return
		else:
			if arbol.derecha == None:
				arbol.derecha = arbol
				print(arbol.derecha.dato,"apunta a", arbol.dato)
			else:
				self.Enhebrar_Der(arbol.derecha)
				self.Enhebrar_Der(arbol.izquierda)
				
#			if arbol.derecha.derecha == None
#				arbol.derecha.derecha = arbol
#				print(arbol.derecha.dato,"apunta a", arbol.dato, "por su derecha")
	def get_arbol(self):
		return self.raiz
arbol = Arbol()
arbol.Insertar(10)
arbol.Insertar(12)
arbol.Insertar(9)
arbol.Insertar(8)
arbol.Insertar(11)
arbol.Insertar(13)
arbol.Insertar(16)
arbol.Insertar(14)
arbol.Enhebrar_Der(arbol.get_arbol())
