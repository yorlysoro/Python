def fx(x):
	fx = 1.0 / x
	return fx
def Trapecio(inferior,superior,n,integral):
	dx = (superior - inferior) / n
	suma1 = fx(inferior) + fx(superior)
	suma = 0.0
	for i in range(1, n-1):
		x = inferior + i * dx
		suma = suma + fx(x)
	integral = (suma1 + 2 * suma) * dx * 0.5
	return integral
	
inferior, superior, n, integral = 1.0, 9.0, 10, 0.0
integral = Trapecio(inferior,superior,n,integral)
print("La integral es %9.5f" %(integral))
