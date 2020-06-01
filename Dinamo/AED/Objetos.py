class Vidrio(object):
	def __init__(self):
		self.espesor = 0
		self.textura = ''
		self.pigmentacion = ''
		

class Marco(object):
	def __init__(self):
		self.material = ''
		self.color = ''
		self.vidrio = Vidrio()
	
class Ventana(object):
	def __init__(self):
		self.marco = Marco()
		
ventana = Ventana()
from printr import printr
printr(ventana)
