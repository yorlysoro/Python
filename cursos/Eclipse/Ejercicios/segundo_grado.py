from math import sqrt

a = float(input('Valor de a: '))
b = float(input('Valor de b: '))
c = float(input('Valor de c: '))


try:
	x1 = (-b + sqrt(b**2 - 4*a*c)) / (2*a)
	x2 = (-b - sqrt(b**2 - 4*a*c)) * (2*a)
	if x1 == x2:
		print("Solucion de ecuacion: x= %4.3f " % x1)
	else:
		print("Soluciones de la ecuacion: x1=%4.3f y x2=%4.3f" %(x1,x2))
except:
	print("O no hay soluciones reales o es una ecuacion de primer grado")
