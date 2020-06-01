
from math import sqrt

x = float(input('Introduce un numero positivo: '))
while x < 0:
	x = float(input('Introduce numero positivo: '))
	
print("La raiz cuadrada de %f es %f " %(x,sqrt(x)))
