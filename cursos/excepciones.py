while True:
	try:
		x = int(raw_input("Introduce un numero: "))
		break
	except ValueError:
		print "Huy! No es un numero. Prueba de nuevo"
	