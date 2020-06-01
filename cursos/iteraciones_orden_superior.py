def cuadrado(n):
	return n ** 2
	
l = [1, 2, 3]
l2 = map(cuadrado, l)

print l2

def es_par(n):
	return (n % 2.0 == 0)
	
l = [1, 2, 3]
l2 = filter(es_par, l)

print l2

def sumar(x, y):
	return x + y
	
l = [1, 2, 3]
l2 = reduce(sumar, l)
print l2
