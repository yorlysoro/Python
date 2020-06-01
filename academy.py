pyg = 'ay'

original = raw_input('Escribi una palabra:')

if len(original) > 0 and original.isalpha():
	print original
	palabra = original.lower()
	primera = palabra[0]
	nueva_palabra = palabra + primera + pyg
	nueva_palabra = nueva_palabra[1:len(nueva_palabra)]
else:
	print 'vacio'
