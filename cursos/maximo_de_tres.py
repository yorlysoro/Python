a = int(raw_input('Dame el primer numero: '))
b = int(raw_input('Dame el segundo numero: '))
c = int(raw_input('Dame el tercer numero: '))

if a >= b and a >= c:
	maximo = a
if b >= a and b >= c:
	maximo = b
if c >= a and c >= b:
	maximo = c
print 'El maximo es ', maximo
