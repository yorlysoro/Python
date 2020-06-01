class Nodo:
	def __init__(self, dato):
		self.dato = dato
		self.izquierda = None
		self.derecha = None
		
class Arbol:
	def __init__(self):
		self.raiz = None
	def Insertar(self,dato, arbol,lado,padre):
		if self.raiz == None:
			self.raiz = Nodo(dato)
			print("Se inserto", dato,"como raiz del arbol")
			return True
		else:
			aux = arbol
			if aux.dato == padre:
				if lado == 'D':
					if aux.derecha == None:
						aux.derecha = Nodo(dato)
						print("Se inserto", dato,"a la derecha de", padre)
						return True
				else:
					if aux.izquierda == None:
						aux.izquierda = Nodo(dato)
						print("Se inserto", dato, "de lado izquierdo de",padre)
						return True
			if aux.izquierda != None:
				if not self.Insertar(dato,arbol.izquierda,lado,padre):
					if aux.derecha != None:
						if not self.Insertar(dato,arbol.derecha,lado,padre):
							return False
						else:
							return True
					else:
						return False
				else:
					return True
			else:
				return False
#		if arbol.derecha != None:
#			self.Insertar(dato,arbol.derecha,lado,padre)
#		else:
#			self.Insertar(dato,arbol.izquierda,lado,padre)
	def Evalua(self,arbol):
		if arbol.dato == '+' or arbol.dato == '-' or arbol.dato == '*' or arbol.dato == '/':
			ValorIzquierdo = self.Evalua(arbol.izquierda)
			ValorDerecho = self.Evalua(arbol.derecha)
			if arbol.dato == '+':
				return ValorIzquierdo + ValorDerecho
			elif arbol.dato == '-':
				return ValorIzquierdo - ValorDerecho
			elif arbol.dato == '*':
				return ValorIzquierdo * ValorDerecho
			elif arbol.dato == '/':
				return ValorIzquierdo / ValorDerecho
		else:
			return arbol.dato - 0
	def get_arbol(self):
		return self.raiz
		
		
		
arbol = Arbol()
arbol.Insertar('*',arbol.get_arbol(), ' ', ' ')
arbol.Insertar('+',arbol.get_arbol(), 'I', '*')
arbol.Insertar(5,arbol.get_arbol(), 'I', '+')
arbol.Insertar(4,arbol.get_arbol(), 'D', '+')
arbol.Insertar('-',arbol.get_arbol(), 'D', '*')
arbol.Insertar(6, arbol.get_arbol(), 'I', '-')
arbol.Insertar('+', arbol.get_arbol(), 'D', '-')
arbol.Insertar(2, arbol.get_arbol(), 'I', '+')
arbol.Insertar(1, arbol.get_arbol(),'D', '+')
print("El valor de la expresion es:", arbol.Evalua(arbol.get_arbol()))
