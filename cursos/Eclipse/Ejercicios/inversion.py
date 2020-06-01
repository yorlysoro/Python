cadena = input("Introduce una cadena: ")

inversion =  ''
for caracter in cadena:
	inversion = caracter + inversion
	
print ("Su inversion es: ", inversion)