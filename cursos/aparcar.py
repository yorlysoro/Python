dia = int(raw_input('Dime que dia es hoy: '))

if 0 < dia <= 15:
	print 'Puedes aparcar en el lado izquierdo de la calle'
else:
	if 15 < dia < 32:
		print 'Puedes aparcar en el lado derecho de la calle'
	else:
		print 'Ningun mes tiene %d dias' % dia
