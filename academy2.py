def distancia_desde_cero(args):
	if type(args) == int or type(args) == float:
		return abs(args)
	else:
		return "none"

print distancia_desde_cero(-12.5)
