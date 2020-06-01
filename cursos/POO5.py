class Animal:
	def __init__(self, age, weight):
		self.age = age
		self.__weight = weight
	def __privateMethod(self):
		print self.weight
	def getWeight(self):
		return self.__weight
	def eat(self, kgm):
		self.__weight += kgm
		print "The animal weitghs:", self.__weight, "after eating"

class Bird(Animal):
	def fly(self):
		print "I fly as a bird!"
class Mammal(Animal):
	def fly(self):
		print "I can not fly, I am a mammal!"
class Ostrich(Animal,Bird):
	def fly(self):
		print "I can not fly, I am a Bird but ostrichs do not fly!"
class Platypus1(Mammal, Bird):
	pass
class Platypus2(Bird, Mammal):
	pass

animal1 = Animal(3,0.5)
animal1.eat(0.1)

canary = Bird(1,0.45)
canary.eat(0.02)
canary.fly()

bear = Mammal(10,150)
bear.eat(10)
bear.fly()

ostrichs = Ostrich(5,30)
ostrichs.fly()

platypus = Platypus1(2,3)
platypus.fly()

platypus = Platypus2(2,3)
platypus.fly()

print bear.getWeight()
bear.privateMethod()
