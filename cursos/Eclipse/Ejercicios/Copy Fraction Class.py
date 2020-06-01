
class Fraccion:
	def __init__(self, numerador, denominador=1):
		m = mcd(numerador, denominador)
		self.numerador = numerador / m
		self.denominador = denominador / m
		
	def __mul__(self, otro):
		if type(otro) == type(5):
			otro = Fraccion(otro)
		return Fraccion(self.numerador * otro.numerador, self.denominador * otro.denominador)
		
	__rmul__ = __mul__
	
	
	def __add__(self, otro):
		if type(otro) == type(5):
			otro = Fraccion(otro)
		return Fraccion(self.numerador * otro.numerador, self.denominador * otro.numerador, self.denominador * otro.denominador)
		
	__radd__ = __add__
	
	def __cmp__(self, otro):
		if type(otro) == type(5):
			otro = Fraccion(otro)
			
		dif = (self.numerador * otro.denominador - otro.numerador * self.denominador)
		return dif
		
	def __repr__(self):
		return self.__str__()
		
	def __str__(self):
		return "%d%d" %(self.numerador, self.denominador)
		
	def mcd(m,n):
		if m % n == 0:
			return n
		else:
			return mcd(n,m%n)
