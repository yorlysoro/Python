class Pila:
    """Representa una pila con operaciones de apilar, desapilar y
    verificar si esta vacia"""
    def __init__(self):
        """crea una pila vacia"""
        self.items = []

    def apilar(self, x):
        """Agrega elementos a la pila"""
        self.items.append(x)

    def desapilar(self):
        """Devuelve el elemento tope y lo elimina de la pila
        si la pila esta vacia levante una excepcion."""
    	try:
         return self.items.pop()
        except IndexError:
            raise ValueError("La pila esta vacia")
	def es_vacia(self):
     """Devuelve True si la lista esta vacia, False si no"""
     return self.items == []


pila = Pila()

p.es_vacia()
