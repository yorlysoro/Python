
a = float(input('Valor de a: '))
b = float(input('Valor de b: '))

try:
	x = -b/a
	print("Solucion: ", x)
except:
	if b != 0:
		print("La ecuacion no tiene solucion")
	else:
		print("La ecuacion tiene infinitas soluciones")
