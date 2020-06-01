from Arboles_Recorridos import Arbol
class Arbol_Busqueda(Arbol):
	def Buscar(self,arbol,dato):
		if arbol == None:
			return
		elif arbol.dato == dato:
			return True
		elif self.Buscar(arbol.izquierdo,dato):
			return True
		elif self.Buscar(arbol.derecho, dato):
			return True
		else:
			return False
	def BuscarII(self,arbol,dato,nivel,padre,lado):
		if arbol == None:
			return "El arbol esta vacio"
		elif arbol.dato == dato:
			print("El dato", dato, "fue encontrado en el nivel", nivel)
			if nivel == 1:
				print("El dato",dato," es la raiz del arbol, no tiene padre")
			else:
				print("El padre del dato", dato,"es", padre,"y es hijo",lado)
			return True
		else:
			nivel += 1
			if self.BuscarII(arbol.derecho,dato,nivel,arbol.dato,"Der"):
				return True
			elif self.BuscarII(arbol.izquierdo,dato,nivel,arbol.dato,"Izq"):
				return True
			else:
				return False
arbol = Arbol_Busqueda()		
arbol.insertar(8)
arbol.insertar(2)
arbol.insertar(4)
arbol.insertar(10)
arbol.insertar(9)
arbol.insertar(12)
arbol.insertar(14)
arbol.insertar(11)
print(arbol.Buscar(arbol.get_arbol(),8))
print(arbol.BuscarII(arbol.get_arbol(),12,1,arbol.get_arbol(),"Der"))
