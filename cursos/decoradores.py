def mi_decorador(funcion):
	def nueva(*args):
		print "Llamada a la funcion", funcion.__name__
		retorno = funcion(*args)
		return retorno
	return nueva
	
print mi_decorador(nueva)("hola")
