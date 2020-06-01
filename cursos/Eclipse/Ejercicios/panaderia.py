
class Panaderia:
	def __init__(self, panes, pastitas):
		self.panes = panes
		self.pastas = pastitas
		print("En la tiendo hay", self.panes, "panes y", self.pastas, "pastas aunque estas no se venden")
	def vender(self):
		if self.panes > 0:
			print("Vendido un pan!")
			self.panes -= 1
		else:
			print("Lo sentimos no quedan panes por vender")
	def cocer(self, piezas):
		self.panes += piezas
		print("Quedan ", self.panes, "panes")
		
panaderia1 = Panaderia(3,4)
panaderia2 = Panaderia(1,2)


panaderia2.vender()
panaderia2.vender()

panaderia2.cocer(1)
panaderia2.vender()
