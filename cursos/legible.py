print 'Programa para el calculo del perimetro y el area de un rectangulo'

altura = float(raw_input('Dame la altura (en metros): '))
anchura = float(raw_input('Dame la anchura (en metros): '))

area = altura * anchura
perimetro = 2 * altura + 2 * anchura

print 'el perimetro es de %6.2f metros.' % perimetro
print 'El area es de %6.2f metros cuadrados.' % area
