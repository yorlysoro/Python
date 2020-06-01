print("Nodo Actual", Nodo.dato)
		if Nodo.dato == dato:
			print("Es el nodo a eliminar")
			if Nodo.derecho == None and Nodo.izquierdo == None:
				print("Se elimino el nodo hoja", Nodo.dato)
				Nodo = None
				del Nodo
				return True
			else:
				if Nodo.izquierdo == None:
					print("Tiene un solo hijo, el derecho", Nodo.derecho.dato)
					Nodo.dato = Nodo.derecho.dato
					print("El hijo derecho", Nodo.dato, "ocupo su lugar")
					Nodo_Eliminar = Nodo.derecho
					Nodo.derecho = Nodo_Eliminar.derecho
					Nodo.izquierdo = Nodo_Eliminar.izquierdo
					del Nodo_Eliminar
					return True
				else:
					if Nodo.derecho == None:
						print("Tiene solo un hijo, el izquierdo", Nodo.izquierdo.dato)
						Nodo.dato = Nodo.izquierdo.dato
						print("El hijo izquierdo", Nodo.dato)
						Nodo_Eliminar = Nodo.izquierdo
						Nodo.derecho = Nodo_Eliminar.derecho
						Nodo.izquierdo = Nodo_Eliminar.izquierdo
						del Nodo_Eliminar
						return True
					else:
						print("El dato a eliminar tiene 2 hijos")
						NodoAuxPadre = Nodo
						NodoAuxActual = Nodo.derecho
						while NodoAuxActual.izquierdo:
							NodoAuxPadre = NodoAuxActual
							NodoAuxActual = NodoAuxActual.izquierdo
						Nodo.dato = NodoAuxActual.dato
						if NodoAuxPadre == Nodo:
							NodoAuxPadre.derecho = NodoAuxActual.derecho
						else:
							NodoAuxPadre.izquierdo = NodoAuxActual.derecho
		else:
			if Nodo.dato < dato:
				Eliminar(Nodo.derecho, dato)
			else:
				Eliminar(Nodo.izquierdo, dato)
