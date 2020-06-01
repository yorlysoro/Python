
#rectangulo.py
#Programa: rectangulo.py
#Proposito: Calcula el perimetro y el area de un rectangulo a partir
#de su altura y anchura.
#Autor:
#John Cleese
#Fecha:
#1/1/2001

# Peticion de los datos (en metros)
altura = float(raw_input('Dame la altura (en metros): '))
anchura = float(raw_input('Dame la anchura (en metros): '))

# Calculo del area y del perimetro
area = altura * anchura
perimetro = 2 * altura + 2 * anchura

# Impresion de resultados por pantalla
print 'El perimetro es de %6.2f metros' % perimetro # solo dos decimales.
print 'El area es de %6.2f metros cuadrados' % area

create_line(100,100,900,900)
