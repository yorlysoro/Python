class Nodo:
		def __init__(self):
			self.dato = None
			self.izquierda = None
			self.derecha = None
			self.padre = None
			self.FE = 0

class AVL:
	
	def __init__(self):
		self.raiz  = None
	
	def insertar(self, raiz,dato):
		padre = None
		actual = raiz
		while(actual != None and dato != actual.dato):
			padre = actual
			if dato < actual.dato:
				actual = actual.izquierda
			elif dato > actual.dato:
				actual = actual.derecha
		if actual != None:
			return
		if padre == None:
			raiz = Nodo()
			raiz.dato = dato
			raiz.izquierda = raiz.derecha = None
			raiz.padre = None
			raiz.FE = 0
			if self.raiz == None:
				self.raiz = raiz
		elif dato < padre.dato:
			actual = Nodo()
			padre.izquierda = actual
			actual.dato = dato
			actual.izquierda = actual.derecha = None
			actual.padre = padre
			actual.FE = 0
			self.Equilibrar(raiz, padre, "Izq", True)
		elif dato > padre.dato:
			actual = Nodo()
			padre.derecha = actual
			actual.dato = dato
			actual.izquierda = actual.derecha = None
			actual.padre = padre
			actual.FE = 0
			self.Equilibrar(raiz,padre,"Der",True)
	
	def Equilibrar(self, raiz,padre,rama,dato):
		salir = False
		while(padre and not salir):
			if dato:
				if rama == "Izq":
					padre.FE -= 1
				else:
					padre.FE +=1
			else:
				if rama == "Izq":
					padre.FE += 1
				else:
					padre.FE -= 1
			if padre.FE == 0:
				salir = True
			elif padre.FE == -2:
				if padre.izquierda.FE == 1:
					self.RDD(raiz,padre)
				else:
					self.RSD(raiz,padre)
				salir = True
			elif padre.FE == 2:
				if padre.derecha.FE == -1:
					self.RDI(raiz,padre)
				else:
					self.RSI(raiz,padre)
				salir = True
			if padre.padre:
				if padre.padre.derecha == padre:
					rama = "Der"
				else:
					rama = "Izq"
			padre = padre.padre
	
	def RDD(self, raiz, padre):
		Padre = padre.padre
		A = padre
		B = A.izquierda
		C = B.derecha
		CI = C.izquierda
		CD = C.derecha
		if Padre:
			if Padre.derecha == A:
				Padre.derecha = C
			else:
				Padre.izquierda
		else:
			padre = C
		B.derecha = CI
		A.izquierda = CD
		C.izquierda = B
		C.derecha = A
		C.padre = Padre
		A.padre = B.padre = C
		if CI:
			CI.padre = B
		if CD:
			CD.padre = A
		if C.FE == -1:
			B.FE =0
			A.FE = 1
		elif C.FE == 0:
			B.FE = 0
			A.FE = 0
		elif C.FE == 1:
			B.FE = -1
			A.FE = 0
		C.FE = 0
		
	def RDI(self,raiz,padre):
		Padre = padre.padre
		A = padre
		B = A.derecha
		C = B.izquierda
		CI = C.izquierda
		CD = C.derecha
		if Padre:
			if Padre.derecha == A:
				Padre.derecha = C
			else:
				Padre.izquierda = C
		else:
			raiz = C
		A.derecha = CI
		B.izquierda = CD
		C.izquierda = A
		C.derecha = B
		C.padre = Padre
		A.padre = B.padre = C
		if CI:
			CI.padre = A
		if CD:
			CD.padre = B
		if C.FE == -1:
			A.FE = 0
			B.FE = 1
		elif C.FE == 0:
			A.FE = 0
			B.FE = 0
		elif C.FE == 1:
			A.FE = -1
			B.FE = 0
		C.FE = 0
	
	def RSD(self, raiz, padre):
		Padre = padre.padre
		A = padre
		B = A.izquierda
		C = B.derecha
		if Padre:
			if Padre.derecha == A:
				Padre.derecha = B
			else:
				Padre.izquierda = B
		else:
			raiz = B
		A.izquierda = C
		B.derecha = A
		A.padre = B
		if C:
			C.padre = A
		B.padre = padre
		A.FE = 0
		B.FE = 0
		
	def RSI(self,raiz,padre):
		Padre = padre.padre
		A = padre
		B = A.derecha
		C = B.izquierda
		if Padre:
			if Padre.derecha == A:
				Padre.derecha = B
			else:
				Padre.izquierda = B
		else:
			raiz = B
		A.derecha = C
		B.izquierda = A
		A.padre = B
		if C:
			C.padre = A
		B.padre = Padre
		A.FE = 0
		B.FE = 0
		
	def Es_Hoja(selfl, nodo):
		return not nodo.derecha and not nodo.izquierda
	
	def Eliminar_Nodo(self,raiz,dato):
		padre = None
		actual = raiz
		
		while(actual != None):
			if dato == actual.dato:
				if self.Es_Hoja(actual):
					if padre:
						if padre.derecha == actual:
							padre.derecha = None
						elif padre.izquierda == actual:
							padre.izquierda = None
					del actual
					actual = None
					if (padre.derecha == actual and padre.FE == 1) or (padre.izquierda == actual and padre.FE == -1)	:
						padre.FE = 0
						actual = padre
						padre = actual.padre
					if padre:
						if padre.derecha == actual:
							self.Equilibrar(raiz,padre,"Der", False)
						else:
							self.Equilibrar(raiz,padre,"Izq", False)
				else:
					padre = actual
					if actual.derecha:
						nodo = actual.derecha
						while nodo.izquierda:
							padre = nodo
							nodo = nodo.izquierda
					else:
						nodo = actual.izquierda
						while nodo.derecha:
							padre = nodo
							nodo = nodo.derecha
				aux = actual.dato
				actual.dato = nodo.dato
				nodo.dato = aux
				actual = nodo
			else:
				padre = actual
				if dato > actual.dato:
					actual = actual.derecha
				elif dato < actual.dato:
					actual = actual.izquierda
	def get_arbol(self):
		return self.raiz
	def Recorrer(self,raiz, lado,padre):
		if raiz == None:
			return
		else:
			print(raiz.dato, "como hijo de", padre.dato,"por la", lado)
			self.Recorrer(raiz.izquierda,"izquierda", raiz)
			self.Recorrer(raiz.derecha,"derecha", raiz)
			
avl = AVL()
avl.insertar(avl.get_arbol(),8)
avl.insertar(avl.get_arbol(),2)
avl.insertar(avl.get_arbol(),4)
avl.insertar(avl.get_arbol(),10)
avl.insertar(avl.get_arbol(),9)
avl.insertar(avl.get_arbol(),12)
avl.insertar(avl.get_arbol(),14)
print("Se muestra el arbol")
avl.Recorrer(avl.get_arbol(),"raiz",avl.get_arbol())
print("Se elimina un elemento")
avl.Eliminar_Nodo(avl.get_arbol(), 9)
print("El arbol despues de eliminar")
avl.Recorrer(avl.get_arbol(),"raiz",avl.get_arbol())
