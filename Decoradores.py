def trace(fun):
    def wrapper(*a,**k):
	print "**>>:", fun.__name__, a, k
	res = fun(*a, **k)
	print "**<<:", fun.__name__
	return res
    return wrapper



@trace
def mi_funcion():
    print "Hola Mundo!"
    
mi_funcion()