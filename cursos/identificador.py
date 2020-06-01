car = raw_input('Dame un caracter: ')

if 'a' <= car.lower() <= 'z' or car == '_':
	print "Este caracter es valido en un identificador en python"
else:
	if not(car < '0' or '9' < car):
		print "Un digito es valido en un identificador en python"
		print "siempre que no seael primer caracter"
	else:
		print "Caracter no valido para forma un identificador en python"
