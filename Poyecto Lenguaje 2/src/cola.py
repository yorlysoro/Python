from archivos import existeArchivo
__name__="cola"
class Nodo(object):
	def __init__(self, cedula, sueldoNeto, mes):
		self.__cedula = cedula
		self.__sueldoNeto = sueldoNeto
		self.__mes = mes
		self.siguiente = None
	@property
	def get_Nodo(self):
		return (self.__cedula, self.__sueldoNeto, self.__mes)
	

class Cola(object):
	def __init__(self):
		self.__primero = None
		self.__ultimo = None

	@property
	def get_Primero(self):
		return self.__primero
	@property
	def get_Ultimo(self):
		return self.__ultimo
	
	def set_Primero(self, primero):
		self.__primero = primero

	def set_ultimo(self, ultimo):
		self.__ultimo = ultimo


def encolar(cola, cedula, sueldoNeto, mes):
	aux = Nodo(cedula, sueldoNeto, mes)
	aux.siguiente = None
	ultimo = cola.get_Ultimo()
	if(cola.get_Primero() == None):
		cola.set_Primero(aux)
	else:
		ultimo.siguiente = aux
	cola.set_ultimo(aux)


def crearFifo(cola):
	nArch = "../txt/FIFO.txt"
	FIFO = None
	if(existeArchivo(nArch)):
		FIFO = open(nArch, "a")
	else:
		FIFO = open(nArch, "w")
		FIFO.write("			Total Cobrado\n")
		FIFO.write("Trabajador		"+"Cobrado		"+"MES\n")
	while(cola.get_Primero() != None):
		aux = cola.get_Primero()
		datos = aux.get_Nodo()
		FIFO.write(datos[0]+"		"+str(datos[1])+"		"+datos[2]+"\n")
		cola.set_Primero(aux.siguiente)
		del aux	
	FIFO.close()