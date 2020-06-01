class Hora:
    def __init__(self, horas=0, minutos=0, segundos=0):
        self.horas = horas
        self.minutos = minutos
        self.segundos = segundos

    def __str__(self):
        return str(self.horas) + ":" + str(self.minutos) + ":" + str(self.segundos)
    def convierteASegundos(self):
        minutos = self.horas * 60 + self.minutos
        segundos = self.minutos * 60 + self.segundos
        return segundos
    def incrementa(self, segs):
        segs = segs + self.segundos
        self.horas = self.horas + segs/3600
        segs = segs % 3600
        self.minutos = self.minutos + segs/60
        segs = segs % 60
        self.segundos = segs

    def haceHora(segs):
        hora = Hora()
        hora.horas = segs/3600
        segs = seg - hora.horas * 3600
        hora.minutos = segs/60
        hora.segundos = segs
        return hora

    
