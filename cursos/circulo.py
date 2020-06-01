from math import pi
radio = float(raw_input('Dame el radio de un circulo: '))
opcion = ''
while opcion < 'a' or opcion > 'c':
	print 'Escoge una opcion: '
	print 'a) Calcular el diametro'
	print 'b) Calcular el perimetro'
	print 'c) Calcular el area'

	opcion = raw_input('Teclea a, b, o c y pulsa el retorn de carro: ')

	if opcion == 'a':
		diametro = 2 * radio
		print 'El diametro es ', diametro
		
	else:
		if opcion == 'b':
			perimetro = 2 * pi * radio
			print 'El perimetro es ', perimetro
		else:
			if opcion == 'c':
				area = pi * radio ** 2
				print 'El area es', area
			else:
				print 'Solo hay tres opciones: a, b, c'
				print 'Tu has tecleado', opcion
