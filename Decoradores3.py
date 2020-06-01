class Clasecilla(object):
    @property
    def propiedad(self):
	print "Propiedad"
    @staticmethod
    def estatico():
	print "Metoto estatico"
    
    @classmethod
    def declase(cls):
	print "Metodo de clase:" , cls
	
Clasecilla.estatico()
Clasecilla.declase()
obj = Clasecilla()
obj.propiedad
obj.estatico()
obj.declase()