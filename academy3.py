def costo_hotel(noches):
	return 140 * noches
def costo_del_vuelo(ciudad):
	if ciudad == 'Cordoba':
		return 821
	elif ciudad == 'Iguazu':
		return 941
	elif ciudad == 'Ushuaia':
		return 1280
	elif ciudad == 'Bariloche':
		return 1848

costo_del_vuelo('Cordoba')
