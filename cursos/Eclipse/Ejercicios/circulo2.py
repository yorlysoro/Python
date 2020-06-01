
from math import pi
radio = float(input('Dame el radio de un circulo: '))

opcion = ''
while opcion != 'd':
	print("Escoge una opcion:")
	print("a)Calcular el diametro")
	print("b)Calcular el perimetro")
	print("c)Calcular el area")
	print("d)Finalizar")
	opcion = input('Teclea a, b o c y pulsa el retorno de carro: ')
	if opcion == 'a':
		diametro = 2 * radio
		print("El diametro es ", diametro)
	elif opcion == 'b':
		perimetro = 2 * pi * radio
		print("El perimetro es ", perimetro)
	elif opcion == 'c':
		area = pi * radio ** 2
		print("El area es ", area)
	elif opcion != 'd':
		print("Solo hay cuatro opciones: a, b o c. Tu has selecionado ", opcion)
	
print("Gracias por usar el programa")
