import sys
def trace(out = sys.stdout):
    def decorator(fun):
	@wraps(fun)
	def wrapper(*a, **k):
	    print >> out, "**>>", fun.__name__, a, k
	    res = fun(*a, **k)
	    print >> out, "**<<", fun.__name__
	    return res
	return wrapper
    return decorator
@trace(sys.stderr)
def mi_funcion():
    print "Hola Mundo!"

@trace()
def mi_funcion():
    print "Hola Mundo!"