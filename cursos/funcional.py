def money(country):
	def spain():
		print "Euro"
	def japan():
		print "Yen"
	def eeuu():
		print "dollar"
	functor_money = ["es":spain,
										"jp": japan,
										"us": eeuu]
	return functor_money[country]
	
f = money("us")
money("us")()
f()

f = money("jp")
f()
