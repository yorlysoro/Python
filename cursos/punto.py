class Punto:
    def __int__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    def __add__(self, otro):
        return Punto(self.x + otro.x, self.y + otro.y)

    def __sub__(self,otro):
        return Punto(self.x - otro.x, self.y - otro.y)

    def __mul__(self, otro):
        return self.x * otro.x + self.y * otro.y

    def __rmul__(self, otro):
        return Punto(otro * self.x, otro * self.y)

    def reverse(self):
        self.x, self.y = self.y, self.x

    def delDerechoYDelReves(derecho):
        from copy import copy
        reves = copy(derecho)
        reves.reverse()
        print str(derecho) + str(reves)
